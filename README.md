# aiworkspace harness

A drop-in, agent-agnostic workflow harness for AI-assisted development. Add it to any repository, run `setup`, and every AI agent working there (Claude Code, Codex, Gemini, Antigravity, …) follows the same gated lifecycle, guardrails, and skills.

Built on **Google's Open Knowledge Format (OKF v0.1)**: every rule, skill, and workspace document is plain Markdown with YAML frontmatter, so it is readable by humans and any agent alike.

---

## Quickstart

No checkout needed: this fetches a shallow clone into a temp directory, runs the installer, and cleans up. Run it from inside the repo you want to install into; the target defaults to the current directory.

**Linux / macOS:**

```bash
curl -fsSL https://raw.githubusercontent.com/migaeldev/aiworkflows/master/tools/bootstrap.sh \
  | sh -s -- https://github.com/migaeldev/aiworkflows
```

**Windows (PowerShell):**

```powershell
iex "& { $(irm https://raw.githubusercontent.com/migaeldev/aiworkflows/master/tools/bootstrap.ps1) } -RepoUrl https://github.com/migaeldev/aiworkflows"
```

Add `--dry-run` to preview first. See [Install](docs/install.md) for the from-a-checkout form, what the installer writes, and how to upgrade.

---

## What you get

- **A 6-step gated lifecycle**: `define` → `plan` → `resources/` → `processing/` → `finalized/` → `promote`. Agents never advance a step without explicit human approval.
- **A production immutability guardrail**: AI edits happen in a sandboxed `processing/` folder; only a human-issued `promote` touches production code.
- **A skills library**: engineering (codebase mapping, code review, testing, diagnosis, architecture), security audits, productivity (planning, personas, handoffs, context management), and brand onboarding on top of a Material Design 3 template.
- **Project context agents actually use**: a codebase map of where and how to change code, and a `soul.md` persona so agents write in your project's languages, patterns, and voice.
- **Domain workspaces**: each area of work gets its own identity, tone, directives, plans, and audit log.

---

## Learn more

- [Install](docs/install.md): the bootstrap one-liner and the from-a-checkout form, pointing other AI tools at `AGENTS.md`, why there's an installer at all, upgrading, and host modes.
- [Onboarding flow](docs/onboarding.md): the full path from an empty install to your first planned feature, and what `/setup` asks and writes at each step.
- [The lifecycle](docs/lifecycle.md): the six-step pipeline and its slash commands.
- [Layout](docs/layout.md): what lives where in this repository.
- [Maintaining the harness](docs/maintaining.md): regenerating Claude Code adapters and running the tool tests.
