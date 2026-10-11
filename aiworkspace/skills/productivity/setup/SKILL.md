---
type: skill
name: setup
title: Setup (Repository Onboarding)
description: One-time bootstrap for installing aiworkspace into a repository — detect host context, record host_mode in aiworkspace/host.md, then scaffold the first workspace via new-workspace. Use when aiworkspace's files already exist on disk in a repo but haven't been initialized yet, or the user asks to set up/onboard aiworkspace here.
tags: [skill, productivity, setup, onboarding, host-mode]
timestamp: 2026-10-04T00:00:00+02:00
---

# Setup (Repository Onboarding)

## Trigger
Use once per repository, after the `aiworkspace/` files and skills are already present on disk (getting them there is a separate, currently-manual step — see Notes) but before any workspace has been defined. Not re-run routinely.

## Process

1. **Detect host context** — scan the repo root for existing manifests (`package.json`, `requirements.txt`, `go.mod`, etc.) and check whether an `apps/` folder already exists.
2. **Propose a `host_mode`**, don't assume it:
   - `monorepo` if an `apps/<workspace>/`-style structure already fits (or is clearly intended).
   - `bolt-on` if this is an existing codebase with its own structure and no `apps/` pattern.
   - Confirm with the user either way — never silently decide (`AGENTS.md` Directive #1).
3. **Record `host_mode`** in `aiworkspace/host.md` (OKF `type: resource` — see this repo's own `aiworkspace/host.md` for the shape). This is the single source of truth `AGENTS.md` Directive #6 and `productivity/promote` both read.
4. **Grill-me interview** — invoke [`productivity/grill-me`](../grill-me/SKILL.md) to learn: the project's overall purpose, whether one or multiple domain workspaces are expected now, and — **in `bolt-on` mode specifically** — where in the host repo different kinds of production code should land. This seeds the first workspace's Production Target Map (a new section in its `index.md`, used only in `bolt-on` mode).
5. **Scaffold the first workspace by delegating to [`productivity/new-workspace`](../new-workspace/SKILL.md)** — don't duplicate its scaffolding/interview logic here.
6. **Confirm `AGENTS.md`/`CLAUDE.md` reflect the recorded `host_mode`** — in `bolt-on` mode, the immutability wording in both files should already describe "everything outside `aiworkspace/` is read-only except via the Production Target Map" (this repo's own copies already handle the branch; a freshly-bolted-on repo gets these files copied in, per Notes, and should not need further editing here).
7. **Present & gate** — wait for explicit confirmation before any Step 0/1 work begins.

## Notes
- **Getting the files here in the first place (Step A) is still manual.** `aiworkspace` isn't published anywhere yet; a future one-line fetch (e.g. `npx degit <org>/aiworkspace-template aiworkspace`) is planned but not built — see `workflow-improvements-planning-claude.md` §7. For now, this skill assumes `aiworkspace/`, `AGENTS.md`, `CLAUDE.md`, and the `.claude/skills/` adapters are already present (copied in by hand).
- Never write to `apps/[workspace]` or (in `bolt-on` mode) anywhere outside `aiworkspace/` from this skill — scaffolding only.
