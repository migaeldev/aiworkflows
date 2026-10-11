# CLAUDE.md

This repository uses the `aiworkspace` harness. [`AGENTS.md`](./AGENTS.md) is the single source of truth for agent rules — read it first. This file only restates the rules Claude Code must never miss.

## Critical Operating Rules

- **Initialize first.** If [`aiworkspace/host.md`](./aiworkspace/host.md) reads `host_mode: unset`, run `/setup` ([`productivity/setup`](./aiworkspace/skills/productivity/setup/SKILL.md)) before any other lifecycle work.
- **Immutability guardrail (host-mode aware).**
  - `monorepo`: never directly edit, create, or delete files inside `apps/[workspace]`.
  - `bolt-on`: never directly edit, create, or delete anything outside `aiworkspace/` (and `.claude/`) except via that workspace's `index.md` Production Target Map.
  - All code changes happen in `aiworkspace/workspaces/[workspace]/processing/`. Only a human-issued `promote` moves code to production.
- **Mandatory step gate.** After finishing work in a lifecycle step, present it and wait for explicit confirmation. Never auto-advance `define` → `plan` → `resources/` → `processing/` → `finalized/` → production.
- **Define before plan.** `/plan` needs a defined workspace. If it doesn't exist or `definition.md` is still the placeholder, run `/define` (alias `/spec`) first.
- **Project conventions.** Follow [`aiworkspace/project.md`](./aiworkspace/project.md) for package manager, stack, test commands, comment policy, git commit policy, and project-specific directives.
- **Commit policy gates auto-commits.** `productivity/process`'s per-task commit step only runs the way `project.md`'s **Commit policy** (`auto` / `ask` / `manual`) says — never commit assuming `auto`; check the setting (or ask once if `unset`) first.
- **Be the project.** Adopt the persona in `aiworkspace/soul.md`, with the active workspace's `soul.md` layered on top, when they exist. Before changing host code, check `aiworkspace/codebase-map.md` for where the change belongs and how to write it.
- **Brand check before UI work.** If Brand in `project.md` is `pending`, ask whether to onboard the brand first ([`design/brand-onboarding`](./aiworkspace/skills/design/brand-onboarding/SKILL.md)). Otherwise use `brand/brand.md` or the template defaults in `design/brand-guidelines`.
- **Software-engineer skill on code tasks.** Before writing or modifying code, load [`aiworkspace/skills/engineering/software-engineer/SKILL.md`](./aiworkspace/skills/engineering/software-engineer/SKILL.md).
- **Humanizer skill on generated prose.** Before finalizing any written content for a human reader (docs, READMEs, commit messages, PR/issue descriptions, plan/definition narrative, chat responses), load [`aiworkspace/skills/productivity/humanizer/SKILL.md`](./aiworkspace/skills/productivity/humanizer/SKILL.md) to strip AI writing tells. Code, config, data, and verbatim quoted material are out of scope.

## Where things are

- Lifecycle & architecture: [`aiworkspace/README.md`](./aiworkspace/README.md)
- Workspaces & skills registry: [`aiworkspace/index.md`](./aiworkspace/index.md)
- Skills: [`aiworkspace/skills/README.md`](./aiworkspace/skills/README.md)
- Slash commands (`/setup`, `/map`, `/brand`, `/persona`, `/define`, `/plan`, `/process`, `/finalize`, …): see "Slash Commands & Aliases" in [`aiworkspace/README.md`](./aiworkspace/README.md)
