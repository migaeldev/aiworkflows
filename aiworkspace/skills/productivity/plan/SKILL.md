---
type: skill
name: plan
title: Plan (Step 0)
description: Step 0 of the lifecycle — determine whether this is a Project Plan or a Feature/Change Plan, interview with grill-me, optionally frame with goal-driven, research where needed, and write the plan before resources/ work begins. Use when starting new work in a workspace, before writing to resources/ or processing/.
tags: [skill, productivity, planning, step-0, grill-me, goal-driven]
timestamp: 2026-10-04T00:00:00+02:00
---

# Plan (Step 0)

## Trigger
Use at the start of any new unit of work in a domain workspace — before `resources/` is populated for a new ask, and before any `processing/` work begins. This is Step 0 of the lifecycle, upstream of `resources/`.

## Two plan types
Determine which applies before doing anything else — confirm with the user rather than assuming (Directive #1):

| | Project Plan | Feature/Change Plan |
|---|---|---|
| Scope | Whole workspace/domain | One feature, fix, or unit of work |
| Cadence | Once at workspace inception; rarely revised | Every time this skill runs for a new ask |
| Output | `planning/project-plan.md` | `planning/features/<slug>/spec.md` |
| Trigger | `productivity/new-workspace` delegates here | Any planning request once a project plan already exists |

If `planning/project-plan.md` doesn't exist yet, this is a Project Plan. If it exists, default to Feature/Change Plan and ask the user to name the feature/slug.

## Process

1. **Determine plan type** — per the table above, confirming rather than assuming.
2. **Ask about `goal-driven`** — before interviewing, ask: *"Want to frame this with `productivity/goal-driven` (success criteria / constraints / verification / out of scope) first? Recommended, but optional."* Only load it if the user says yes. Never auto-load it.
3. **Interview** — invoke [`productivity/grill-me`](../grill-me/SKILL.md) one-question-at-a-time, every time, regardless of the answer to step 2. If `goal-driven` was loaded, use its template to shape the plan's `## Goal` section.
4. **Research where needed** — for changes to host code, start with `aiworkspace/codebase-map.md` (if present) so the plan names the right modules and follows existing patterns. Otherwise, if a question can be answered by exploring the codebase or external sources, do that instead of asking. Record findings in `planning/research.md` with citations (Directive #2 — never hallucinate).
5. **Write the plan**:
   - **Project Plan** sections: `## Goal` (optional, only if step 2 was yes) → Domain Purpose & Identity → Success Criteria → Constraints & Directives → Known Unknowns.
   - **Feature/Change Plan** sections: `## Goal` (optional) → Problem Statement → Solution → User Stories → Implementation Decisions → Testing Decisions → Out of Scope → Further Notes.
6. **Enrich `index.md`** — write any new domain terminology, constraints, or purpose details straight into the domain's `index.md` Domain Identity/Directives section now. That file is the glossary — there's no separate one. If the interview shows this workspace needs a different voice or code style from the project soul, offer to run [`productivity/persona`](../persona/SKILL.md) at workspace scope rather than writing persona details into `index.md`.
7. **Decision map for large work only** — if the ask doesn't collapse into one plan document, add `planning/decisions/<slug>.md` files instead (or alongside): OKF `type: resource`, each with `status: open | blocked | resolved` and `blocked_by: [...]` referencing other decision files. Unblocked + open files are the actionable frontier.
8. **Log it** — append an entry to the domain's `log.md` recording what kind of plan was written, for what ask, and where the plan document landed.
9. **Present & gate** — present the plan document (and any `index.md`/`log.md` changes) and wait for explicit human confirmation before `resources/` work begins (Project Plan) or `processing/` work begins on that feature (Feature/Change Plan). Never auto-advance.

## Notes
- Never write to production code from this skill.
- `engineering/code-review`'s Spec-Fidelity axis checks implementations against whatever this skill produced — keep plans specific enough to review against.
- `engineering/software-engineer` requires this skill to have run before code gets written.
