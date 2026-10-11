"""Consistency checks for the harness repository itself.

    python tools/check_harness.py   # exit 1 if any check fails

Checks:
- links:     every relative Markdown link/image resolves to an existing file or directory
- leftovers: no names from the project the harness was extracted from, and no absolute user paths
- adapters:  .claude/skills/ adapters match the slash-command table (tools/gen_claude_adapters.py --check)
"""

import re
import sys
from pathlib import Path

import gen_claude_adapters as gen

EXCLUDED_DIRS = {".git", ".idea", ".vscode", "__pycache__", "node_modules", ".venv", "venv"}
TEXT_SUFFIXES = {".md", ".py", ".sh", ".ps1", ".json", ".yaml", ".yml", ".toml", ".txt", ".css", ".html", ".js", ".ts"}
# This script and its tests necessarily contain the denylist.
SELF = {"tools/check_harness.py", "tools/test_check_harness.py"}

# Names from the playground the harness was extracted from. Keep these specific: generic
# technologies (Flask, BigQuery, Roboto, …) are legitimate examples in skills and must not be listed.
LEFTOVER_PATTERNS = [
    (r"28\s?east", "original company brand"),
    (r"premier partner", "original company brand"),
    (r"feasibility", "original project/workspace name"),
    (r"insights[ _]engine|insights project|insights repository", "original project name"),
    (r"etl-pipeline|task-management-system|task-engine|pluscode|bulk-feasibility|ui-test-agent", "original workspace name"),
    (r"CLIENT_DAILY_SUMMARY|DESTINATION_TABLE", "original project config"),
    (r"workflow-improvements-planning", "reference to a planning doc that was not extracted"),
    (r"migaelhartzenberg", "personal path"),
    (r"file:///", "absolute file URL"),
    (r"(?<![\w.])/Users/[^/\s]+/|[A-Za-z]:\\Users\\", "absolute user path"),
]
_LEFTOVER_RE = [(re.compile(p, re.IGNORECASE), why) for p, why in LEFTOVER_PATTERNS]

_FENCE_RE = re.compile(r"^\s*(```|~~~)")
_INLINE_CODE_RE = re.compile(r"`[^`]*`")
_LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def _files(root: Path, suffixes) -> list:
    out = []
    for path in sorted(root.rglob("*")):
        rel_parts = path.relative_to(root).parts
        if path.is_file() and path.suffix.lower() in suffixes and not EXCLUDED_DIRS.intersection(rel_parts):
            out.append(path)
    return out


def check_links(root: Path) -> list:
    """Return 'file:line: broken link -> target' for every unresolved relative link."""
    problems = []
    for md in _files(root, {".md"}):
        rel_md = md.relative_to(root).as_posix()
        in_fence = False
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), start=1):
            if _FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for match in _LINK_RE.finditer(_INLINE_CODE_RE.sub("", line)):
                target = match.group(1)
                if target.startswith("#") or _SCHEME_RE.match(target):
                    continue
                path_part = target.split("#", 1)[0]
                if not (md.parent / path_part).exists():
                    problems.append(f"{rel_md}:{lineno}: broken link -> {target}")
    return problems


def check_leftovers(root: Path) -> list:
    """Return 'file:line: leftover name (why): match' for every denylisted name in a text file."""
    problems = []
    for path in _files(root, TEXT_SUFFIXES):
        rel = path.relative_to(root).as_posix()
        if rel in SELF:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            for pattern, why in _LEFTOVER_RE:
                match = pattern.search(line)
                if match:
                    problems.append(f"{rel}:{lineno}: leftover name ({why}): {match.group(0)}")
                    break  # one report per line is enough to find it
    return problems


def check_adapters(root: Path) -> list:
    return [f"{rel}: adapter out of date (run python tools/gen_claude_adapters.py)" for rel in gen.sync(root, check=True)]


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    failed = False
    for name, run in (("links", check_links), ("leftovers", check_leftovers), ("adapters", check_adapters)):
        problems = run(root)
        print(f"{name}: {'ok' if not problems else f'{len(problems)} problem(s)'}")
        for problem in problems:
            print(f"  {problem}")
        failed = failed or bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
