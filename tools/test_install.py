"""Tests for install.py. Run: python -m unittest discover tools"""

import shutil
import tempfile
import unittest
from pathlib import Path

import gen_claude_adapters as gen
import install

HARNESS = Path(__file__).resolve().parent.parent


class InstallTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        tmp = Path(self._tmp.name)
        # A private copy of the harness, so tests can change "the next version".
        self.source = tmp / "harness"
        shutil.copytree(HARNESS, self.source, ignore=shutil.ignore_patterns(".git", "__pycache__", ".idea"))
        self.target = tmp / "host"
        self.target.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def run_install(self, **kwargs):
        return install.install(self.source, self.target, **kwargs)

    def read(self, rel):
        return (self.target / rel).read_text(encoding="utf-8")


class FreshInstallTest(InstallTestCase):
    def test_copies_core_instance_and_adapters(self):
        report = self.run_install()
        self.assertFalse(report.conflicts)
        for rel in ("aiworkspace/README.md",
                    "aiworkspace/skills/productivity/plan/SKILL.md",
                    "aiworkspace/workspaces/template-workspace/definition.md",
                    "aiworkspace/host.md", "aiworkspace/project.md", "aiworkspace/index.md",
                    ".claude/skills/plan/SKILL.md", ".claude/skills/spec/SKILL.md",
                    install.MANIFEST):
            self.assertTrue((self.target / rel).exists(), rel)
        self.assertIn("host_mode: unset", self.read("aiworkspace/host.md"))

    def test_does_not_copy_harness_maintenance_files(self):
        self.run_install()
        for rel in ("tools", "README.md", ".gitignore", ".gitattributes", "VERSION"):
            self.assertFalse((self.target / rel).exists(), rel)

    def test_creates_agent_files_as_marked_blocks(self):
        self.run_install()
        agents = self.read("AGENTS.md")
        self.assertTrue(agents.startswith(install.BLOCK_START))
        self.assertIn("Core Agent Directives", agents)
        self.assertIn(install.BLOCK_END, self.read("CLAUDE.md"))

    def test_appends_to_existing_agent_file_without_losing_content(self):
        (self.target / "CLAUDE.md").write_text("# My project\n\nUse tabs.\n", encoding="utf-8")
        self.run_install()
        claude = self.read("CLAUDE.md")
        self.assertTrue(claude.startswith("# My project\n\nUse tabs.\n"))
        self.assertEqual(claude.count(install.BLOCK_START), 1)

    def test_dry_run_writes_nothing(self):
        report = self.run_install(dry_run=True)
        self.assertTrue(report.created)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_refuses_to_install_into_itself(self):
        with self.assertRaises(ValueError):
            install.install(self.source, self.source)

    def test_refuses_when_adapters_are_stale(self):
        (self.source / ".claude" / "skills" / "plan" / "SKILL.md").write_text("stale", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.run_install()

    def test_hand_written_skill_with_same_name_is_a_conflict(self):
        mine = self.target / ".claude" / "skills" / "plan" / "SKILL.md"
        mine.parent.mkdir(parents=True)
        mine.write_text("---\nname: plan\n---\nmine\n", encoding="utf-8")
        report = self.run_install()
        self.assertIn(".claude/skills/plan/SKILL.md", report.conflicts)
        self.assertEqual(mine.read_text(encoding="utf-8"), "---\nname: plan\n---\nmine\n")
        self.run_install(force=True)
        self.assertIn(gen.MARKER, mine.read_text(encoding="utf-8"))


class UpgradeTest(InstallTestCase):
    def setUp(self):
        super().setUp()
        self.run_install()

    def test_reinstall_is_a_no_op(self):
        report = self.run_install()
        self.assertEqual((report.created, report.updated, report.removed, report.conflicts), ([], [], [], []))

    def test_preserves_instance_files(self):
        (self.target / "aiworkspace" / "host.md").write_text("host_mode: bolt-on\n", encoding="utf-8")
        ws = self.target / "aiworkspace" / "workspaces" / "billing" / "index.md"
        ws.parent.mkdir(parents=True)
        ws.write_text("mine", encoding="utf-8")
        self.run_install()
        self.assertEqual(self.read("aiworkspace/host.md"), "host_mode: bolt-on\n")
        self.assertEqual(ws.read_text(encoding="utf-8"), "mine")

    def test_updates_changed_core_file(self):
        skill = self.source / "aiworkspace" / "skills" / "productivity" / "caveman" / "SKILL.md"
        skill.write_text(skill.read_text(encoding="utf-8") + "\nNew rule.\n", encoding="utf-8")
        report = self.run_install()
        self.assertEqual(report.updated, ["aiworkspace/skills/productivity/caveman/SKILL.md"])
        self.assertIn("New rule.", self.read("aiworkspace/skills/productivity/caveman/SKILL.md"))

    def test_locally_edited_core_file_is_a_conflict_unless_forced(self):
        rel = "aiworkspace/skills/productivity/caveman/SKILL.md"
        (self.target / rel).write_text("local edit", encoding="utf-8")
        skill = self.source / rel
        skill.write_text(skill.read_text(encoding="utf-8") + "\nNew rule.\n", encoding="utf-8")
        report = self.run_install()
        self.assertEqual(report.conflicts, [rel])
        self.assertEqual(self.read(rel), "local edit")
        # Still owned: the next run reports the same conflict instead of adopting the edit.
        self.assertEqual(self.run_install().conflicts, [rel])
        self.run_install(force=True)
        self.assertIn("New rule.", self.read(rel))

    def test_removes_core_file_dropped_from_harness(self):
        rel = "aiworkspace/skills/productivity/caveman/SKILL.md"
        shutil.rmtree(self.source / "aiworkspace" / "skills" / "productivity" / "caveman")
        report = self.run_install()
        self.assertIn(rel, report.removed)
        self.assertFalse((self.target / rel).exists())

    def test_keeps_dropped_core_file_if_locally_edited(self):
        rel = "aiworkspace/skills/productivity/caveman/SKILL.md"
        (self.target / rel).write_text("local edit", encoding="utf-8")
        shutil.rmtree(self.source / "aiworkspace" / "skills" / "productivity" / "caveman")
        report = self.run_install()
        self.assertIn(rel, report.conflicts)
        self.assertTrue((self.target / rel).exists())

    def test_replaces_marked_block_in_place(self):
        claude = self.target / "CLAUDE.md"
        claude.write_text("# Mine\n\n" + claude.read_text(encoding="utf-8") + "\n## After\n", encoding="utf-8")
        (self.source / "CLAUDE.md").write_text("# New harness text\n", encoding="utf-8")
        self.run_install()
        text = claude.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Mine\n"))
        self.assertTrue(text.rstrip().endswith("## After"))
        self.assertIn("# New harness text", text)
        self.assertEqual(text.count(install.BLOCK_START), 1)


if __name__ == "__main__":
    unittest.main()
