# Install

Requires Python 3.8+ (standard library only) and git.

**Without a checkout**, `tools/bootstrap.sh` (Linux/macOS) and `tools/bootstrap.ps1` (Windows) fetch a shallow clone of this repository into a temp directory, run the installer, and delete the clone again. Run it from inside the repo you want to install into; the target defaults to the current directory:

```bash
curl -fsSL <raw-url-of-tools/bootstrap.sh> | sh -s -- <this-repo-url> --dry-run
```

```powershell
iex "& { $(irm <raw-url-of-tools/bootstrap.ps1>) } -RepoUrl <this-repo-url> --dry-run"
```

Set `AIWORKSPACE_REPO_URL` (sh: env var `AIWORKSPACE_REPO_URL=<this-repo-url>`; PowerShell: `$env:AIWORKSPACE_REPO_URL`) to drop the repo-url argument from every call. That's handy as a saved alias. Drop `--dry-run` to actually install. To target a different directory, append it as an extra argument (sh) or pass `-Target path/to/your-repo` (PowerShell).

**From a checkout** of this repository (also defaults to the current directory):

```bash
python tools/install.py path/to/your-repo --dry-run   # preview a specific target
python tools/install.py --dry-run                     # preview, installing into the current directory
python tools/install.py                               # install into the current directory
```

The installer writes:
- `aiworkspace/`: skills, the workspace template, and starter `host.md`/`project.md`/`index.md`.
- `.claude/skills/`: Claude Code slash-command adapters. Skills already in your repo are kept; a name clash is reported, not overwritten.
- `AGENTS.md` and `CLAUDE.md`: the harness rules go inside a `<!-- aiworkspace:start -->` … `<!-- aiworkspace:end -->` block. An existing file keeps its own content, and the block is appended below it.

Then, inside your repo:

```bash
python aiworkspace/scripts/agent_pointers.py   # pick the AI tools you use; each gets a "read AGENTS.md first" file
```

and open the repo in your agent and run **`/setup`**. See [Onboarding flow](./onboarding.md) for what happens next.

## Pointing every AI tool at `AGENTS.md`

Each coding agent reads its *own* instruction file when a session starts, not necessarily `AGENTS.md`. If that file doesn't send it to `AGENTS.md`, the agent may never see the harness rules: no step gate, no immutability guardrail. `aiworkspace/scripts/agent_pointers.py` is the failsafe. It asks which tools you use, and writes a short "read `AGENTS.md` first" block into each tool's startup file:

| Tool | File written |
| :--- | :--- |
| Claude Code | `CLAUDE.md` (already written by the installer, so left as is) |
| Gemini CLI | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Cursor | `.cursor/rules/aiworkspace.mdc` (`alwaysApply: true`) |
| Windsurf | `.windsurf/rules/aiworkspace.md` (`trigger: always_on`) |
| Cline | `.clinerules/aiworkspace.md` |
| OpenAI Codex | nothing needed (reads `AGENTS.md` natively) |
| Anything else | `--file path/to/its-instructions.md` |

```bash
python aiworkspace/scripts/agent_pointers.py                        # interactive menu
python aiworkspace/scripts/agent_pointers.py --tools gemini,cursor  # non-interactive (agents, CI)
python aiworkspace/scripts/agent_pointers.py --list                 # supported tools
```

Existing content in those files is kept; the pointer goes in the same marked block the installer uses, and re-running only refreshes it. Run it again whenever the team adopts another AI tool. `/setup` also offers it (step 7).

## Why an installer, and not just asking the AI?

Getting the harness into a repo has two parts, and each is done by the tool that suits it:

| Part | Done by | Why |
| :--- | :--- | :--- |
| **Copy the files**, and later upgrade them | `tools/install.py` | Mechanical and exact. It needs no judgment, so it shouldn't need an agent. |
| **Fit the harness to your project** | The AI, via `/setup` | Needs judgment and conversation: your stack, conventions, brand, persona, first workspace. |

You *could* ask an agent to copy the harness in, and the first install would mostly work. The installer is still needed because:

- **Upgrades need memory.** The installer records a hash for every file it writes in `aiworkspace/.harness-manifest.json`, so on the next run it can tell which files are its own and untouched (safe to update), which you edited (left alone and reported), and which the harness has since removed (safe to delete). An agent has no such record. On an upgrade it would either overwrite your edits or leave stale files behind.
- **The result is identical every time.** Over 100+ files, an agent may skip a file, paraphrase a rule, or reorganize something. The installer copies byte for byte.
- **Your files are protected.** Existing `AGENTS.md`/`CLAUDE.md` content stays outside the managed block, and a skill of yours with the same name as a harness command (e.g. your own `/plan`) is reported, not replaced.
- **You can preview it.** `--dry-run` lists every change before anything is written.
- **It needs no tokens.** It takes about a second, needs no permission prompts, and also runs in CI or a plain terminal.
- **Nothing governs the AI yet.** Before install, the rules that keep an agent careful aren't in the repo.

The AI is better at merging *meaning*, e.g. noticing that your existing `CLAUDE.md` says "use npm" while you want pnpm. That's why reconciling agent files is a `/setup` step, not an installer feature. You can also ask your agent to run the installer for you ("run `python tools/install.py ../my-repo --dry-run` and show me"). You keep the installer's guarantees and the agent does the typing.

## Upgrading

Pull the latest harness and run the same command again. `aiworkspace/.harness-manifest.json` records every file the installer wrote, along with its hash, so an upgrade:
- updates or removes harness files you haven't touched;
- reports harness files you **edited** as conflicts and leaves them alone (re-run with `--force` to overwrite);
- replaces only the marked block in `AGENTS.md`/`CLAUDE.md`;
- never touches your project files: `host.md`, `project.md`, `index.md`, workspaces, `brand/`, `codebase-map.md`, `soul.md`.

The installer exits with `1` when there are conflicts, and with `2` on errors (e.g. stale adapters in the harness checkout).

## Host modes

| Mode | Use when | Production code lives in |
| :--- | :--- | :--- |
| `monorepo` | New repo, or one already organized as `apps/<name>/` | `apps/<workspace>/` |
| `bolt-on` | Existing codebase with its own structure | Wherever each workspace's **Production Target Map** says |
