---
type: skill
name: define
title: Define (Step 0)
description: Step 0 of the lifecycle — create a domain workspace (or redefine an existing one) and define its core in definition.md, covering purpose, scope, users, success criteria, directives, production target, known unknowns, and candidate features, via a grill-me interview. Use for /define or /spec, when the user wants a new workspace or domain, when productivity/setup scaffolds the first workspace, or when productivity/plan finds that the target workspace doesn't exist or isn't defined yet.
tags: [skill, productivity, lifecycle, step-0, workspace, scaffolding, grill-me]
timestamp: 2026-10-11T00:00:00+02:00
---

# Define (Step 0)

## What it's for
A workspace's **definition** is its core: why it exists, what is and isn't in scope, who it serves, what "good" looks like, and the rules it must never break. It's written once when the workspace is created, and revised rarely. Everything later in the lifecycle is checked against it: every `/plan` for a feature or task, every `finalize` review.

| | Define (Step 0) | Plan (Step 1) |
| :--- | :--- | :--- |
| Scope | The whole workspace | One feature, change, or batch of tasks |
| Cadence | Once at creation; rarely revised | Every new ask |
| Output | `definition.md` + `index.md` core sections | `planning/features/<slug>/plan.md` |

## Trigger
- `/define` (aliases `/spec`, `/step0`, `/new-workspace`), or a request to create or (re)define a workspace.
- `productivity/setup`, when scaffolding the first workspace.
- [`productivity/plan`](../plan/SKILL.md) hands off here when the target workspace doesn't exist, or its `definition.md` is still the template placeholder.

## Process

### 1. Resolve the workspace
- **Name given and it exists, with a filled-in `definition.md`** → **redefine mode**. Summarize the current definition, ask what's changing and why, edit only those sections, then go to step 7.
- **Name given and it exists, but `definition.md` is still the placeholder** → skip to step 3.
- **Name given and it doesn't exist, or no name given** → ask for (or confirm) a kebab-case name (e.g. `billing-insights`). Check that `aiworkspace/workspaces/<name>/` doesn't exist yet.
- **Handed over from `plan`** → say so ("there's no workspace for this yet, so let's define one first"), and carry the user's original ask into the interview as the first candidate feature.

### 2. Scaffold from the template
Copy `aiworkspace/workspaces/template-workspace/` → `aiworkspace/workspaces/<name>/` verbatim. Replace the `<workspace>`/`<Workspace Title>` placeholders and timestamps in the frontmatter of `index.md`, `log.md`, and `definition.md`. In `index.md`'s Production Application Location section, keep only the subsection that matches `host_mode` in `aiworkspace/host.md` and delete the other.

This only creates files under `aiworkspace/workspaces/<name>/`. Never touch production code.

### 3. Offer `goal-driven`
Ask: *"Want to frame this workspace with `productivity/goal-driven` (success criteria / constraints / verification / out of scope) first? Recommended, but optional."* Only load it if the user says yes.

### 4. Research before asking
Read what's already known, so the interview doesn't ask questions the repo already answers:
- `aiworkspace/project.md`, `aiworkspace/codebase-map.md` (modules, entry points, and change recipes relevant to this domain), `aiworkspace/soul.md`, and `aiworkspace/brand/brand.md` if the workspace has UI.
- The other workspaces' definitions in `aiworkspace/index.md`, to find overlaps and boundaries.
- Record any findings worth keeping in `planning/research.md`, with citations (Directive #2).

### 5. Interview with grill-me
Invoke [`productivity/grill-me`](../grill-me/SKILL.md): one question at a time, each with your recommended answer, skipping what step 4 settled. Converge on:
1. **Purpose**: one sentence on why this workspace exists.
2. **Scope**: what's in, and what's explicitly out, especially relative to neighboring workspaces.
3. **Users & stakeholders**: who uses its output, and who approves it.
4. **Success criteria**: observable, checkable outcomes that say the workspace is doing its job.
5. **Constraints & directives**: rules this workspace must never break (data, security, compliance, performance, dependencies).
6. **Production target**:
   - `monorepo` → confirm `apps/<name>/`.
   - `bolt-on` → which host-repo paths its output lands in. Seed the Production Target Map, using the codebase map's Module Map and Change Recipes to propose paths.
7. **Persona**: does this workspace speak or code differently from the project soul? If yes, note it for step 8.
8. **Known unknowns**: open questions and risks.
9. **Candidate features**: the first few things to `/plan`, in rough priority order.

### 6. Write the definition
- **`definition.md`**: fill in every section of the template. Include the `## Goal` section only if step 3 was yes. Mark unresolved items as open questions, never guesses.
- **`index.md`**: keep it in sync without duplicating the full definition. Fill in Domain Purpose (one line), Domain Directives (the numbered list from step 5.5), any glossary terms already named, and the Production Target Map in bolt-on mode.

### 7. Persona, registry, log
- If step 5.7 said the workspace has its own voice or code style, offer [`productivity/persona`](../persona/SKILL.md) at workspace scope.
- **New workspace**: add a row to `aiworkspace/index.md`'s Domain Workspaces table (Production Location: "not yet promoted").
- **Redefine**: update its registry row if the purpose changed.
- Append to the workspace's `log.md`: defined or redefined, what changed, and why.

### 8. Present & gate
Present `definition.md`, the `index.md` changes, and the registry row, and wait for explicit confirmation. Then suggest the next step: `/plan` for the top candidate feature (or the ask that `plan` handed over). Never auto-advance.

## Notes
- Redefining a workspace can invalidate existing plans. After a redefine, list any `planning/features/*/plan.md` that now fall out of scope or conflict, and ask the user how to handle them.
- This skill never writes to production code.
