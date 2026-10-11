"""Tests for bootstrap.sh / bootstrap.ps1. Run: python -m unittest discover tools/tests

Exercises each script end to end (shallow clone + install.py --dry-run) against a throwaway
local git repo, so no network access is required.
"""

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

HARNESS = Path(__file__).resolve().parent.parent.parent


class BootstrapTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        tmp = Path(self._tmp.name)
        self.repo = tmp / "repo-src"
        shutil.copytree(HARNESS, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__", ".idea"))
        self._git("init", "--quiet", "-b", "master")
        self._git("add", "-A")
        self._git("commit", "--quiet", "-m", "fixture")
        self.target = tmp / "host"
        self.target.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def _git(self, *args):
        env = {
            "GIT_AUTHOR_NAME": "test", "GIT_AUTHOR_EMAIL": "test@example.com",
            "GIT_COMMITTER_NAME": "test", "GIT_COMMITTER_EMAIL": "test@example.com",
        }
        subprocess.run(["git", "-C", str(self.repo), *args], check=True, env=env,
                        capture_output=True, text=True)


@unittest.skipUnless(shutil.which("sh"), "no POSIX sh on this machine")
class BootstrapShTest(BootstrapTestCase):
    def run_script(self, *args, env=None, cwd=None):
        return subprocess.run(["sh", str(HARNESS / "tools" / "bootstrap.sh"), *args],
                               capture_output=True, text=True, env=env, cwd=cwd)

    def test_installs_with_explicit_repo_url(self):
        result = self.run_script(str(self.repo), str(self.target), "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Would install aiworkspace harness", result.stdout)
        self.assertFalse((self.target / "aiworkspace").exists())  # --dry-run writes nothing

    def test_installs_for_real(self):
        result = self.run_script(str(self.repo), str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.target / "aiworkspace" / "host.md").exists())

    def test_repo_url_from_environment(self):
        import os
        env = dict(os.environ, AIWORKSPACE_REPO_URL=str(self.repo))
        result = self.run_script(str(self.target), "--dry-run", env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Would install aiworkspace harness", result.stdout)

    def test_target_defaults_to_the_current_directory(self):
        result = self.run_script(str(self.repo), cwd=str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.target / "aiworkspace" / "host.md").exists())

    def test_no_arguments_is_a_usage_error(self):
        result = self.run_script()
        self.assertEqual(result.returncode, 2)
        self.assertIn("usage:", result.stderr)


@unittest.skipUnless(shutil.which("powershell") or shutil.which("pwsh"), "no PowerShell on this machine")
class BootstrapPs1Test(BootstrapTestCase):
    EXE = shutil.which("pwsh") or shutil.which("powershell")

    def run_script(self, *args, env=None, cwd=None):
        return subprocess.run(
            [self.EXE, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
             "-File", str(HARNESS / "tools" / "bootstrap.ps1"), *args],
            capture_output=True, text=True, env=env, cwd=cwd)

    def test_installs_with_explicit_repo_url(self):
        result = self.run_script("-RepoUrl", str(self.repo), "-Target", str(self.target), "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Would install aiworkspace harness", result.stdout)
        self.assertFalse((self.target / "aiworkspace").exists())

    def test_installs_for_real(self):
        result = self.run_script("-RepoUrl", str(self.repo), "-Target", str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.target / "aiworkspace" / "host.md").exists())

    def test_repo_url_from_environment(self):
        import os
        env = dict(os.environ, AIWORKSPACE_REPO_URL=str(self.repo))
        result = self.run_script("-Target", str(self.target), "--dry-run", env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Would install aiworkspace harness", result.stdout)

    def test_missing_repo_url_is_an_error(self):
        result = self.run_script("-Target", str(self.target))
        self.assertNotEqual(result.returncode, 0)

    def test_target_defaults_to_the_current_directory(self):
        result = self.run_script("-RepoUrl", str(self.repo), cwd=str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.target / "aiworkspace" / "host.md").exists())


if __name__ == "__main__":
    unittest.main()
