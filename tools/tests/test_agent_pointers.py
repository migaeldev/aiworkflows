"""Tests for aiworkspace/scripts/agent_pointers.py. Run: python -m unittest discover tools/tests"""

import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
HARNESS = TOOLS.parent
sys.path.insert(0, str(HARNESS / "aiworkspace" / "scripts"))
sys.path.insert(0, str(TOOLS))

import agent_pointers as ap  # noqa: E402
import install  # noqa: E402


class PointerTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def read(self, rel):
        return (self.root / rel).read_text(encoding="utf-8")


class SelectionTest(unittest.TestCase):
    def test_accepts_numbers_and_keys(self):
        keys = list(ap.TOOLS)
        self.assertEqual(ap.parse_selection("1, gemini"), [keys[0], "gemini"])

    def test_deduplicates_and_keeps_order(self):
        self.assertEqual(ap.parse_selection("cursor,cursor,claude"), ["cursor", "claude"])

    def test_rejects_unknown_choice(self):
        with self.assertRaises(ValueError):
            ap.parse_selection("notepad")


class WritePointerTest(PointerTestCase):
    def test_creates_tool_file_linking_to_agents_md(self):
        result = ap.ensure_pointers(self.root, ["gemini"])
        self.assertEqual(result, {"GEMINI.md": "created"})
        text = self.read("GEMINI.md")
        self.assertIn("](AGENTS.md)", text)
        self.assertIn(ap.BLOCK_START, text)

    def test_nested_file_uses_relative_link(self):
        ap.ensure_pointers(self.root, ["copilot"])
        self.assertIn("](../AGENTS.md)", self.read(".github/copilot-instructions.md"))

    def test_cursor_rule_is_always_applied(self):
        ap.ensure_pointers(self.root, ["cursor"])
        text = self.read(".cursor/rules/aiworkspace.mdc")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("alwaysApply: true", text)
        self.assertIn("](../../AGENTS.md)", text)

    def test_windsurf_rule_is_always_on(self):
        ap.ensure_pointers(self.root, ["windsurf"])
        self.assertIn("trigger: always_on", self.read(".windsurf/rules/aiworkspace.md"))

    def test_keeps_existing_content_and_is_idempotent(self):
        (self.root / "GEMINI.md").write_text("# Ours\n\nUse tabs.\n", encoding="utf-8")
        self.assertEqual(ap.ensure_pointers(self.root, ["gemini"]), {"GEMINI.md": "updated"})
        self.assertEqual(ap.ensure_pointers(self.root, ["gemini"]), {"GEMINI.md": "unchanged"})
        text = self.read("GEMINI.md")
        self.assertTrue(text.startswith("# Ours\n\nUse tabs.\n"))
        self.assertEqual(text.count(ap.BLOCK_START), 1)

    def test_leaves_existing_harness_block_alone(self):
        # CLAUDE.md written by the installer already carries the (fuller) harness block.
        installed = f"{ap.BLOCK_START}\n# CLAUDE.md\nRead AGENTS.md.\n{ap.BLOCK_END}\n"
        (self.root / "CLAUDE.md").write_text(installed, encoding="utf-8")
        self.assertEqual(ap.ensure_pointers(self.root, ["claude"]), {"CLAUDE.md": "already points to AGENTS.md"})
        self.assertEqual(self.read("CLAUDE.md"), installed)

    def test_codex_needs_no_file(self):
        self.assertEqual(ap.ensure_pointers(self.root, ["codex"]), {"AGENTS.md": "read natively, nothing to create"})
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["AGENTS.md"])

    def test_custom_file(self):
        ap.ensure_pointers(self.root, [], extra_files=["docs/AI.md"])
        self.assertIn("](../AGENTS.md)", self.read("docs/AI.md"))

    def test_dry_run_writes_nothing(self):
        self.assertEqual(ap.ensure_pointers(self.root, ["gemini"], dry_run=True), {"GEMINI.md": "created"})
        self.assertFalse((self.root / "GEMINI.md").exists())

    def test_requires_agents_md(self):
        (self.root / "AGENTS.md").unlink()
        with self.assertRaises(ValueError):
            ap.ensure_pointers(self.root, ["gemini"])


class MarkerCompatibilityTest(unittest.TestCase):
    def test_markers_match_the_installer(self):
        # Both tools manage the same block, so a later install/upgrade replaces it cleanly.
        self.assertEqual(ap.BLOCK_START, install.BLOCK_START)
        self.assertEqual(ap.BLOCK_END, install.BLOCK_END)


if __name__ == "__main__":
    unittest.main()
