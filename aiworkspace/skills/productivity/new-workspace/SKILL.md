---
type: skill
name: new-workspace
title: New Workspace
description: Scaffold a new domain workspace from the template-workspace boilerplate, define its scope via productivity/plan (Project Plan mode), then collect input resources. Use when the user wants to start a new workspace, create a new domain, or scaffold a fresh aiworkspace/workspaces/[name] directory.
tags: [skill, productivity, workspace, scaffolding, okf]
timestamp: 2026-10-04T00:00:00+02:00
---

# New Workspace

## Trigger
Use when the user wants to start a new domain workspace under `aiworkspace/workspaces/`.

## Process

### Step 1 — Name the workspace
Ask for a kebab-case workspace name (e.g. `billing-insights`) if not already given. Confirm `aiworkspace/workspaces/<name>/` does not already exist.

### Step 2 — Scaffold from the template
Copy `aiworkspace/workspaces/template-workspace/` → `aiworkspace/workspaces/<name>/` verbatim: `index.md`, `log.md`, `planning/README.md`, `resources/README.md`, `processing/README.md`, `finalized/README.md`.

Update only the frontmatter (`name`/title placeholders, `timestamp`) in `index.md` and `log.md`. Leave the Domain Identity/Directives section as placeholders — Step 3 fills those in via the plan interview.

This step only creates files under `aiworkspace/workspaces/<name>/`. Never touch production code.

In `index.md`'s Production Application Location section, keep only the subsection matching `host_mode` in `aiworkspace/host.md` and delete the other. In `bolt-on` mode, seed the Production Target Map with whatever `setup`'s interview learned (or leave the example row for `plan` to fill).

### Step 3 — Define the workspace (delegate to `productivity/plan`)
Invoke [`productivity/plan`](../plan/SKILL.md) in **Project Plan mode** (the workspace has no `planning/project-plan.md` yet, so `plan` will determine this automatically). Let `plan` run its own process in full — grill-me interview, the ask-first `goal-driven` offer, research if needed — converging on:
- Domain purpose and directives — written into `planning/project-plan.md` *and* into `index.md`'s Domain Identity section (per `plan`'s step 6 — both stay in sync, not duplicated sources of truth).
- Persona — inherited from the project soul by default; if this workspace needs its own voice or code style, `plan` offers `productivity/persona` at workspace scope.
- Domain directives / constraints — what must never happen in this workspace.
- Success criteria & verification — what "done" looks like for the workspace's first deliverable in `processing/`.

`plan` already appends its own log entry; do not duplicate it here.

### Step 4 — Prompt for resources
Now that the project plan exists and says what this workspace actually needs, tell the user where the workspace was scaffolded and ask them to add any input context, schemas, or raw data to `resources/` that the plan calls for. Explicitly wait for one of:
- confirmation that resources have been added, or
- confirmation that there are none to add.

Do not proceed to Step 5 until the user responds with one of these.

### Step 5 — Present & gate
Present the completed scaffold (files created, filled-in `index.md`, `planning/project-plan.md`) and wait for explicit human confirmation before starting any Step 2 processing work. Never auto-advance `planning/` → `resources/` → `processing/` → `finalized/` → `apps/`.

## Notes
- Never edit production code — see `AGENTS.md` Directive #6.
- Once confirmed, register the new workspace in `aiworkspace/index.md`'s Domain Workspaces table (Production Location: "not yet promoted").
