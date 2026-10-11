"""Install or upgrade the aiworkspace harness in a target repository.

Run from a checkout of the harness:
    python tools/install.py <target-repo>             # install, or upgrade an existing install
    python tools/install.py <target-repo> --dry-run   # show what would change, write nothing
    python tools/install.py <target-repo> --force     # also overwrite files you edited locally

What gets written:
- Core files (skills, workspace template, aiworkspace/README.md, Claude Code adapters) are
  copied and tracked by hash in aiworkspace/.harness-manifest.json. On upgrade, untouched core
  files are updated or removed. Files you edited locally are reported as conflicts and left
  alone unless --force.
- Project files (host.md, project.md, index.md) are created only if missing, never overwritten.
  Workspaces, brand/, codebase-map.md, and soul.md are never touched.
- AGENTS.md and CLAUDE.md get the harness text inside a marked block: appended to an existing
  file, or replaced in place on upgrade. Text outside the block is never changed.
"""

import argparse
import hashlib
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

import gen_claude_adapters as gen

MANIFEST = "aiworkspace/.harness-manifest.json"
BLOCK_START = "<!-- aiworkspace:start (managed by the aiworkspace installer; edits inside this block are replaced on upgrade) -->"
BLOCK_END = "<!-- aiworkspace:end -->"
_BLOCK_START_PREFIX = "<!-- aiworkspace:start"

CORE_DIRS = ["aiworkspace/skills", "aiworkspace/workspaces/template-workspace"]
CORE_FILES = ["aiworkspace/README.md"]
INSTANCE_FILES = ["aiworkspace/host.md", "aiworkspace/project.md", "aiworkspace/index.md"]
BLOCK_FILES = ["AGENTS.md", "CLAUDE.md"]
IGNORED_NAMES = {".DS_Store", "__pycache__", "Thumbs.db"}


@dataclass
class Report:
    created: list = field(default_factory=list)
    updated: list = field(default_factory=list)
    removed: list = field(default_factory=list)
    conflicts: list = field(default_factory=list)
    version: str = ""


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def core_files(source: Path) -> dict:
    """Map each core file (relative posix path) to its bytes."""
    files = {}
    for rel_dir in CORE_DIRS:
        for path in sorted((source / rel_dir).rglob("*")):
            if path.is_file() and not IGNORED_NAMES.intersection(path.relative_to(source).parts):
                files[path.relative_to(source).as_posix()] = path.read_bytes()
    for rel in CORE_FILES:
        files[rel] = (source / rel).read_bytes()
    # Only generated adapters ship; other skills in the harness's own .claude/ stay behind.
    for skill_md in sorted((source / ".claude" / "skills").glob("*/SKILL.md")):
        if gen.MARKER in skill_md.read_text(encoding="utf-8"):
            files[skill_md.relative_to(source).as_posix()] = skill_md.read_bytes()
    return files


def merge_block(existing, content: str) -> str:
    """Return file text with the harness block created, appended, or replaced in place."""
    block = f"{BLOCK_START}\n{content.rstrip()}\n{BLOCK_END}\n"
    if existing is None:
        return block
    start = existing.find(_BLOCK_START_PREFIX)
    end = existing.find(BLOCK_END, start) if start != -1 else -1
    if start == -1 or end == -1:
        return existing.rstrip("\n") + "\n\n" + block
    after = existing[end + len(BLOCK_END):]
    return existing[:start] + block.rstrip("\n") + after


def _version(source: Path) -> str:
    version_file = source / "VERSION"
    return version_file.read_text(encoding="utf-8").strip() if version_file.exists() else "unknown"


def _commit(source: Path):
    try:
        result = subprocess.run(["git", "-C", str(source), "rev-parse", "--short", "HEAD"],
                                capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def _remove_empty_parents(path: Path, stop: Path) -> None:
    parent = path.parent
    while parent != stop and parent.is_dir() and not any(parent.iterdir()):
        parent.rmdir()
        parent = parent.parent


def install(source: Path, target: Path, dry_run: bool = False, force: bool = False) -> Report:
    source, target = source.resolve(), target.resolve()
    if target == source or source in target.parents:
        raise ValueError("target must be a different repository than the harness itself")
    if not target.is_dir():
        raise ValueError(f"target directory does not exist: {target}")
    stale = gen.sync(source, check=True)
    if stale:
        raise ValueError("Claude Code adapters are out of date; run `python tools/gen_claude_adapters.py` "
                         "in the harness first:\n  " + "\n  ".join(stale))

    report = Report(version=_version(source))
    manifest_path = target / MANIFEST
    old = json.loads(manifest_path.read_text(encoding="utf-8"))["files"] if manifest_path.exists() else {}
    owned = {}

    def write(rel: str, data: bytes) -> None:
        if not dry_run:
            path = target / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

    # Core files: create, update if untouched since last install, otherwise report a conflict.
    new = core_files(source)
    for rel, data in new.items():
        path, new_hash = target / rel, _sha(data)
        if not path.exists():
            write(rel, data)
            report.created.append(rel)
            owned[rel] = new_hash
            continue
        current = _sha(path.read_bytes())
        if current == new_hash:
            owned[rel] = new_hash
        elif (rel in old and current == old[rel]) or force:
            write(rel, data)
            report.updated.append(rel)
            owned[rel] = new_hash
        else:
            report.conflicts.append(rel)
            if rel in old:
                owned[rel] = old[rel]  # still ours, but locally edited: keep flagging it

    # Core files dropped from the harness: delete if untouched, otherwise leave and report.
    for rel, old_hash in old.items():
        path = target / rel
        if rel in new or not path.exists():
            continue
        if _sha(path.read_bytes()) == old_hash or force:
            if not dry_run:
                path.unlink()
                _remove_empty_parents(path, target)
            report.removed.append(rel)
        else:
            report.conflicts.append(rel)

    # Project files: seed once, never overwrite.
    for rel in INSTANCE_FILES:
        if not (target / rel).exists():
            write(rel, (source / rel).read_bytes())
            report.created.append(rel)

    # AGENTS.md / CLAUDE.md: managed block only.
    for rel in BLOCK_FILES:
        path = target / rel
        existing = path.read_text(encoding="utf-8") if path.exists() else None
        merged = merge_block(existing, (source / rel).read_text(encoding="utf-8"))
        if merged != existing:
            write(rel, merged.encode("utf-8"))
            (report.created if existing is None else report.updated).append(rel)

    if not dry_run:
        manifest = {"version": report.version, "source_commit": _commit(source), "files": owned}
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def _print_report(report: Report, target: Path, dry_run: bool) -> None:
    changed = report.created or report.updated or report.removed or report.conflicts
    verb = "Would install" if dry_run else "Installed" if changed else "Checked"
    print(f"{verb} aiworkspace harness {report.version} in {target}")
    for label, items in (("created", report.created), ("updated", report.updated), ("removed", report.removed)):
        if items:
            print(f"\n{label} ({len(items)}):")
            for rel in items:
                print(f"  {rel}")
    if report.conflicts:
        print(f"\nconflicts ({len(report.conflicts)}): edited locally or not created by the harness, left unchanged")
        for rel in report.conflicts:
            print(f"  {rel}")
        print("Review them, then re-run with --force to overwrite.")
    if not changed:
        print("Already up to date.")
    host = target / "aiworkspace" / "host.md"
    if not dry_run and host.exists() and "host_mode: unset" in host.read_text(encoding="utf-8"):
        print("\nNext: open the repository in your agent and run /setup.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Install or upgrade the aiworkspace harness in a repository.")
    parser.add_argument("target", type=Path, help="path to the repository to install into")
    parser.add_argument("--dry-run", action="store_true", help="show what would change without writing")
    parser.add_argument("--force", action="store_true", help="overwrite locally edited harness files")
    args = parser.parse_args()

    source = Path(__file__).resolve().parent.parent
    try:
        report = install(source, args.target, dry_run=args.dry_run, force=args.force)
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        return 2
    _print_report(report, args.target.resolve(), args.dry_run)
    return 1 if report.conflicts else 0


if __name__ == "__main__":
    sys.exit(main())
