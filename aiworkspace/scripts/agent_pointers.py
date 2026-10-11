"""Make sure every AI tool used on this repo reads AGENTS.md at startup.

Each coding agent loads its own instruction file when a session starts (Claude Code reads
CLAUDE.md, Gemini CLI reads GEMINI.md, Cursor reads .cursor/rules/, ...). If that file doesn't
point at AGENTS.md, the agent may never see the harness rules. This script asks which tools
you use and writes a short "read AGENTS.md first" block into each tool's file, as a failsafe.

    python aiworkspace/scripts/agent_pointers.py                       # interactive: pick from a list
    python aiworkspace/scripts/agent_pointers.py --tools claude,gemini  # non-interactive
    python aiworkspace/scripts/agent_pointers.py --file docs/AI.md      # any other tool's file
    python aiworkspace/scripts/agent_pointers.py --list                 # show supported tools

Existing content in those files is kept. The pointer goes in a marked block that a re-run
replaces in place, and a block the harness installer already wrote is left alone.
Standard library only (Python 3.8+).
"""

import argparse
import os
import sys
from pathlib import Path

# Same markers as the harness installer (tools/install.py), so either tool can manage the block.
BLOCK_START = "<!-- aiworkspace:start (managed by the aiworkspace installer; edits inside this block are replaced on upgrade) -->"
BLOCK_END = "<!-- aiworkspace:end -->"
_BLOCK_START_PREFIX = "<!-- aiworkspace:start"
POINTER_MARKER = "<!-- aiworkspace:pointer -->"

# key: (display name, instruction file relative to repo root, or None when AGENTS.md is read natively,
#       frontmatter to write when the file is created)
TOOLS = {
    "claude": ("Claude Code", "CLAUDE.md", ""),
    "gemini": ("Gemini CLI", "GEMINI.md", ""),
    "copilot": ("GitHub Copilot", ".github/copilot-instructions.md", ""),
    "cursor": ("Cursor", ".cursor/rules/aiworkspace.mdc",
               "---\ndescription: aiworkspace harness, read AGENTS.md first\nalwaysApply: true\n---\n\n"),
    "windsurf": ("Windsurf", ".windsurf/rules/aiworkspace.md", "---\ntrigger: always_on\n---\n\n"),
    "cline": ("Cline", ".clinerules/aiworkspace.md", ""),
    "codex": ("OpenAI Codex", None, ""),
}


def parse_selection(text: str) -> list:
    """Turn '1, gemini, 3' into tool keys, in order, without duplicates."""
    keys = list(TOOLS)
    chosen = []
    for token in (t.strip().lower() for t in text.split(",")):
        if not token:
            continue
        if token.isdigit() and 1 <= int(token) <= len(keys):
            key = keys[int(token) - 1]
        elif token in TOOLS:
            key = token
        else:
            raise ValueError(f"unknown choice: {token!r} (use a number or one of: {', '.join(keys)})")
        if key not in chosen:
            chosen.append(key)
    return chosen


def pointer_text(rel_file: str) -> str:
    link = Path(os.path.relpath("AGENTS.md", Path(rel_file).parent or ".")).as_posix()
    return (
        f"{POINTER_MARKER}\n"
        "# Agent instructions\n\n"
        f"This repository uses the aiworkspace harness. **Before doing anything else, read [`AGENTS.md`]({link}) "
        "at the repository root and follow it.** It is the single source of truth for how to work here; "
        "this file only makes sure you find it.\n\n"
        "- If `aiworkspace/host.md` reads `host_mode: unset`, run the setup skill "
        "(`aiworkspace/skills/productivity/setup/SKILL.md`) before any other work.\n"
        "- Never edit production code directly. Work in `aiworkspace/workspaces/<workspace>/processing/` "
        "(AGENTS.md Directive #6).\n"
        "- Never advance a lifecycle step without explicit human approval (AGENTS.md Directive #7).\n"
    )


def merge(existing, content: str) -> tuple:
    """Return (new_text, status) for a file that should carry the pointer block."""
    block = f"{BLOCK_START}\n{content.rstrip()}\n{BLOCK_END}\n"
    if existing is None:
        return block, "created"
    start = existing.find(_BLOCK_START_PREFIX)
    end = existing.find(BLOCK_END, start) if start != -1 else -1
    if start == -1 or end == -1:
        return existing.rstrip("\n") + "\n\n" + block, "updated"
    current = existing[start:end + len(BLOCK_END)]
    if POINTER_MARKER not in current:
        return existing, "already points to AGENTS.md"  # the installer's fuller block; leave it
    merged = existing[:start] + block.rstrip("\n") + existing[end + len(BLOCK_END):]
    return merged, "unchanged" if merged == existing else "updated"


def ensure_pointers(root: Path, tools: list, extra_files=(), dry_run: bool = False) -> dict:
    """Write pointer blocks for the given tools; return {file: status}."""
    if not (root / "AGENTS.md").exists():
        raise ValueError(f"no AGENTS.md in {root}; install the harness first")
    targets = []  # (rel_file, frontmatter)
    results = {}
    for key in tools:
        _, rel_file, frontmatter = TOOLS[key]
        if rel_file is None:
            results["AGENTS.md"] = "read natively, nothing to create"
        else:
            targets.append((rel_file, frontmatter))
    targets += [(Path(f).as_posix(), "") for f in extra_files]

    for rel_file, frontmatter in targets:
        path = root / rel_file
        existing = path.read_text(encoding="utf-8") if path.exists() else None
        text, status = merge(existing, pointer_text(rel_file))
        if existing is None:
            text = frontmatter + text
        results[rel_file] = status
        if not dry_run and status in ("created", "updated"):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")
    return results


def _ask() -> tuple:
    keys = list(TOOLS)
    print("Which AI tools will work in this repository?")
    for i, key in enumerate(keys, start=1):
        name, rel_file, _ = TOOLS[key]
        print(f"  {i}. {name:<15} -> {rel_file or 'reads AGENTS.md natively'}")
    print("  o. Other (enter a file path)")
    answer = input("Choose one or more, comma-separated (e.g. 1,2): ").strip()
    others = []
    tokens = [t.strip() for t in answer.split(",") if t.strip()]
    if any(t.lower() == "o" for t in tokens):
        path = input("Path of that tool's instruction file, relative to the repo root: ").strip()
        if path:
            others.append(path)
    return parse_selection(",".join(t for t in tokens if t.lower() != "o")), others


def main() -> int:
    parser = argparse.ArgumentParser(description="Point each AI tool's startup file at AGENTS.md.")
    parser.add_argument("--tools", help=f"comma-separated: {', '.join(TOOLS)}")
    parser.add_argument("--file", action="append", default=[], help="another tool's instruction file (repeatable)")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2],
                        help="repository root (default: the repo this script is installed in)")
    parser.add_argument("--dry-run", action="store_true", help="show what would change without writing")
    parser.add_argument("--list", action="store_true", help="list supported tools and exit")
    args = parser.parse_args()

    if args.list:
        for key, (name, rel_file, _) in TOOLS.items():
            print(f"{key:<9} {name:<15} {rel_file or '(reads AGENTS.md natively)'}")
        return 0
    try:
        if args.tools is not None or args.file:
            tools, others = parse_selection(args.tools or ""), args.file
        elif sys.stdin.isatty():
            tools, others = _ask()
        else:
            print("error: not interactive; pass --tools and/or --file (see --list)", file=sys.stderr)
            return 2
        if not tools and not others:
            print("Nothing selected.")
            return 0
        results = ensure_pointers(args.root, tools, others, dry_run=args.dry_run)
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        return 2
    prefix = "would be " if args.dry_run else ""
    for rel_file, status in results.items():
        shown = prefix + status if status in ("created", "updated") else status
        print(f"  {rel_file}: {shown}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
