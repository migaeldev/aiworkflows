# aiworkspace harness

A drop-in, agent-agnostic workflow harness for AI-assisted development. Add it to any repository, run `setup`, and every AI agent working there (Claude Code, Codex, Gemini, Antigravity, …) follows the same gated lifecycle, guardrails, and skills.

Built on **Google's Open Knowledge Format (OKF v0.1)**: every rule, skill, and workspace document is plain Markdown with YAML frontmatter, so it is readable by humans and any agent alike.

---

## What you get

- **A 5-step gated lifecycle** — `planning/` → `resources/` → `processing/` → `finalized/` → `promote`. Agents never advance a step without explicit human approval.
- **A production immutability guardrail** — AI edits happen in a sandboxed `processing/` folder; only a human-issued `promote` touches production code.
- **A skills library** — engineering (codebase mapping, code review, testing, diagnosis, architecture), security audits, productivity (planning, personas, handoffs, context management), and brand onboarding on top of a Material Design 3 template.
- **Project context agents actually use** — a codebase map of where and how to change code, and a `soul.md` persona so agents write in your project's languages, patterns, and voice.
- **Domain workspaces** — each area of work gets its own identity, tone, directives, plans, and audit log.

---

## Install

> Automated install is planned (see the roadmap below). For now it is a manual copy.

1. Copy into the root of the target repository:
   - `aiworkspace/`
   - `AGENTS.md`
   - `CLAUDE.md` *(if the repo already has one, append a pointer to `AGENTS.md` instead of overwriting it)*
2. Open the repo in your agent and run **`/setup`** (or ask it to "set up aiworkspace"). Setup will:
   - detect your stack and propose a `host_mode`,
   - write `aiworkspace/host.md` and `aiworkspace/project.md`,
   - **with your permission**, map the codebase into `aiworkspace/codebase-map.md` (languages, structure, patterns, conventions, comment scheme, and where/how to make each kind of change),
   - onboard your brand, its files, and your UI stack into `aiworkspace/brand/`, or use the neutral template defaults,
   - create `aiworkspace/soul.md`, a persona so agents speak and code *as your project*,
   - scaffold your first workspace via `new-workspace`.

### Host modes

| Mode | Use when | Production code lives in |
| :--- | :--- | :--- |
| `monorepo` | New repo, or one already organized as `apps/<name>/` | `apps/<workspace>/` |
| `bolt-on` | Existing codebase with its own structure | Wherever each workspace's **Production Target Map** says |

---

## The lifecycle

```text
[0: planning/] ──> [1: resources/] ──> [2: processing/] ──> [3: finalized/] ──> [4: promote] ──> [production]
 plan & research     input context      active iteration     audited & gated     human-only
```

| Step | Command | What happens |
| :--- | :--- | :--- |
| — | `/map` | Create or refresh the codebase map (`codebase-map.md`) |
| — | `/brand` | Onboard or change the brand (`brand/`), or choose template defaults |
| — | `/persona` | Create or change the project or a workspace persona (`soul.md`) |
| 0 | `/plan` | Project or Feature/Change plan, via a `grill-me` interview |
| 1 | `/resources` | Collect the context, schemas, and data the plan calls for |
| 2 | `/process` | Iterate on code and content inside `processing/` |
| 3 | `/finalize` | Security audit, API spec (if applicable), docs, tests, dual-axis code review |
| 4 | `/promote` | Human-authorized copy to production |

Full specification: [`aiworkspace/README.md`](./aiworkspace/README.md).

---

## Layout

```text
.
├── AGENTS.md                     # Agent-agnostic operating rules (source of truth)
├── CLAUDE.md                     # Claude Code pointer to AGENTS.md
└── aiworkspace/
    ├── README.md                 # Architecture, lifecycle & slash-command spec
    ├── index.md                  # Registry of workspaces & skills (filled as you go)
    ├── host.md                   # host_mode — written by setup
    ├── project.md                # Project conventions — written by setup
    ├── codebase-map.md           # Where/how to change code — setup, with permission
    ├── brand/                    # Brand values, logos, fonts, tokens, docs & references — /brand (optional)
    ├── soul.md                   # Project persona — /persona
    ├── skills/                   # design / engineering / productivity / security
    └── workspaces/
        └── template-workspace/   # Boilerplate copied by new-workspace
```

---

## Roadmap

- [ ] Installer (`npx degit` / install script) that copies the harness and merges into an existing `CLAUDE.md`/`AGENTS.md` without overwriting
- [ ] `.claude/skills/` adapters so lifecycle commands appear as native Claude Code slash commands
- [ ] Link checker and "no leftover project names" check for the harness itself
