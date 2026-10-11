"""Tests for check_harness.py. Run: python -m unittest discover tools"""

import tempfile
import unittest
from pathlib import Path

import check_harness as check


class CheckTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


class LinkCheckTest(CheckTestCase):
    def test_reports_broken_relative_link_with_line_number(self):
        self.write("docs/a.md", "# A\n\nSee [b](./b.md) and [c](../c.md).\n")
        self.write("docs/b.md", "# B\n")
        problems = check.check_links(self.root)
        self.assertEqual(problems, ["docs/a.md:3: broken link -> ../c.md"])

    def test_ignores_external_anchor_and_code_links(self):
        self.write("a.md",
                   "[web](https://example.com) [mail](mailto:x@y.z) [top](#top)\n"
                   "`[inline](missing.md)`\n"
                   "```\n[fenced](missing.md)\n```\n")
        self.assertEqual(check.check_links(self.root), [])

    def test_strips_anchor_and_title_from_target(self):
        self.write("a.md", '[b](b.md#section "Title")\n')
        self.write("b.md", "# B\n")
        self.assertEqual(check.check_links(self.root), [])

    def test_checks_images_and_directories(self):
        self.write("a.md", "![logo](img/logo.png) [dir](sub/)\n")
        (self.root / "sub").mkdir()
        self.assertEqual(check.check_links(self.root), ["a.md:1: broken link -> img/logo.png"])

    def test_skips_excluded_directories(self):
        self.write(".git/x.md", "[b](nope.md)\n")
        self.write("node_modules/x.md", "[b](nope.md)\n")
        self.assertEqual(check.check_links(self.root), [])


class LeftoverNamesTest(CheckTestCase):
    def test_flags_project_specific_names_case_insensitively(self):
        self.write("skills/x.md", "Use the 28EAST palette.\nSee apps/feasibility-insights/app.\n")
        problems = check.check_leftovers(self.root)
        self.assertEqual(len(problems), 2)
        self.assertTrue(problems[0].startswith("skills/x.md:1: leftover name"))
        self.assertTrue(problems[1].startswith("skills/x.md:2: leftover name"))

    def test_flags_absolute_user_paths(self):
        self.write("x.md", "[logo](file:///Users/someone/logo.svg)\nC:\\Users\\someone\\x\n")
        self.assertEqual(len(check.check_leftovers(self.root)), 2)

    def test_allows_generic_technology_examples(self):
        self.write("x.md", "e.g. Flask `TestClient`, BigQuery `ScalarQueryParameter`, `billing-insights`.\n")
        self.assertEqual(check.check_leftovers(self.root), [])

    def test_personal_path_pattern_is_path_bound_not_a_bare_substring(self):
        # The same name legitimately appears in this fork's distribution URL (a GitHub
        # account, not a leftover filesystem path) and must not be flagged there.
        self.write("x.md", "Clone https://github.com/MigaelHartzenberg-Coder/aiworkspace.\n")
        self.assertEqual(check.check_leftovers(self.root), [])

    def test_still_flags_the_personal_path_itself(self):
        self.write("y.md", "See /Users/migaelhartzenberg/Projects/old-repo\nC:\\Users\\migaelhartzenberg\\x\n")
        self.assertEqual(len(check.check_leftovers(self.root)), 2)

    def test_scans_text_files_but_not_binaries_or_its_own_sources(self):
        self.write("tools/x.py", "NAME = '28east'\n")
        (self.root / "logo.png").write_bytes(b"\x89PNG 28east")
        self.write("tools/check_harness.py", "DENY = ['28east']\n")
        self.write("tools/test_check_harness.py", "'28east'\n")
        problems = check.check_leftovers(self.root)
        self.assertEqual([p.split(":")[0] for p in problems], ["tools/x.py"])


if __name__ == "__main__":
    unittest.main()
