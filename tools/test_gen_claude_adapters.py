"""Unit tests for gen_claude_adapters. Run: python -m unittest discover tools"""

import json
import tempfile
import unittest
from pathlib import Path

import gen_claude_adapters as gen

TABLE = """\
## ⌨️ Slash Commands & Aliases (Canonical List)

| Stage | Primary | Aliases | Delegates to |
| :--- | :--- | :--- | :--- |
| Onboarding | `/setup` | — | [`skills/productivity/setup/SKILL.md`](./skills/productivity/setup/SKILL.md) |
| Step 0 — Define | `/define` | `/spec`, `/step0` | [`skills/productivity/define/SKILL.md`](./skills/productivity/define/SKILL.md) |
| Step 5 — Promote | `/promote` | `/deploy` | [`skills/productivity/promote/SKILL.md`](./skills/productivity/promote/SKILL.md) |

Every alias resolves to exactly the same skill as its primary.
"""


def make_repo(tmp: Path) -> Path:
    """Build a minimal harness tree with the commands in TABLE."""
    (tmp / "aiworkspace").mkdir()
    (tmp / "aiworkspace" / "README.md").write_text(TABLE, encoding="utf-8")
    for name in ("setup", "define", "promote"):
        skill = tmp / "aiworkspace" / "skills" / "productivity" / name
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            f'---\ntype: skill\nname: {name}\ndescription: Does {name}: the "{name}" step.\n---\n\n# {name}\n',
            encoding="utf-8",
        )
    return tmp


class ParseCommandsTest(unittest.TestCase):
    def test_parses_primary_aliases_and_target(self):
        commands = gen.parse_commands(TABLE)
        self.assertEqual([c.primary for c in commands], ["setup", "define", "promote"])
        self.assertEqual(commands[0].aliases, [])
        self.assertEqual(commands[1].aliases, ["spec", "step0"])
        self.assertEqual(commands[1].target, "aiworkspace/skills/productivity/define/SKILL.md")
        self.assertEqual(commands[1].stage, "Step 0 — Define")

    def test_missing_table_raises(self):
        with self.assertRaises(ValueError):
            gen.parse_commands("# no table here\n")


class RenderTest(unittest.TestCase):
    def setUp(self):
        self.define, = [c for c in gen.parse_commands(TABLE) if c.primary == "define"]
        self.promote, = [c for c in gen.parse_commands(TABLE) if c.primary == "promote"]

    def frontmatter(self, text: str) -> dict:
        head = text.split("---\n")[1]
        out = {}
        for line in head.strip().splitlines():
            key, _, value = line.partition(": ")
            out[key] = value
        return out

    def test_primary_is_model_invocable_and_points_at_skill(self):
        text = gen.render_primary(self.define, 'Does define: the "define" step.')
        fm = self.frontmatter(text)
        self.assertEqual(fm["name"], "define")
        self.assertEqual(json.loads(fm["description"]), 'Does define: the "define" step.')
        self.assertNotIn("disable-model-invocation", fm)
        self.assertIn("aiworkspace/skills/productivity/define/SKILL.md", text)
        self.assertIn("$ARGUMENTS", text)
        self.assertIn(gen.MARKER, text)

    def test_human_only_primary_disables_model_invocation(self):
        fm = self.frontmatter(gen.render_primary(self.promote, "Promote."))
        self.assertEqual(fm["disable-model-invocation"], "true")

    def test_alias_disables_model_invocation_and_names_primary(self):
        text = gen.render_alias("spec", self.define)
        fm = self.frontmatter(text)
        self.assertEqual(fm["name"], "spec")
        self.assertEqual(fm["disable-model-invocation"], "true")
        self.assertIn("/define", json.loads(fm["description"]))
        self.assertIn("aiworkspace/skills/productivity/define/SKILL.md", text)


class SyncTest(unittest.TestCase):
    def test_writes_all_adapters_then_check_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_repo(Path(tmp))
            self.assertEqual(len(gen.sync(root, check=False)), 6)
            names = sorted(p.name for p in (root / ".claude" / "skills").iterdir())
            self.assertEqual(names, ["define", "deploy", "promote", "setup", "spec", "step0"])
            self.assertEqual(gen.sync(root, check=True), [])

    def test_check_reports_drift_without_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_repo(Path(tmp))
            gen.sync(root, check=False)
            adapter = root / ".claude" / "skills" / "define" / "SKILL.md"
            adapter.write_text("edited by hand", encoding="utf-8")
            self.assertEqual(gen.sync(root, check=True), [".claude/skills/define/SKILL.md"])
            self.assertEqual(adapter.read_text(encoding="utf-8"), "edited by hand")

    def test_removes_stale_generated_adapter_but_keeps_hand_written_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_repo(Path(tmp))
            skills = root / ".claude" / "skills"
            (skills / "old-alias").mkdir(parents=True)
            (skills / "old-alias" / "SKILL.md").write_text(f"---\n---\n{gen.MARKER}\n", encoding="utf-8")
            (skills / "mine").mkdir()
            (skills / "mine" / "SKILL.md").write_text("---\nname: mine\n---\nhand written\n", encoding="utf-8")
            gen.sync(root, check=False)
            self.assertFalse((skills / "old-alias").exists())
            self.assertTrue((skills / "mine" / "SKILL.md").exists())


if __name__ == "__main__":
    unittest.main()
