---
type: skill
name: plan
title: Plan (Step 1)
description: Step 1 of the lifecycle — plan a feature, change, or batch of work inside a defined workspace, covering problem, solution, decisions, an ordered task list, the resources needed, and the testing approach, via a grill-me interview. If the target workspace doesn't exist or isn't defined yet, hand off to productivity/define first. Use for /plan, or when starting any new unit of work, before resources/ or processing/.
tags: [skill, productivity, planning, step-1, tasks, grill-me, goal-driven]
timestamp: 2026-10-11T00:00:00+02:00
---

# Plan (Step 1)

## Trigger
`/plan` (aliases `/step1`, `/research`), or the start of any new unit of work: a feature, fix, change, or batch of tasks. Planning comes before `resources/` is gathered for the ask and before any `processing/` work.

## Process

### 1. Resolve the workspace — define first if needed
Work out which workspace the ask belongs to, from what the user said, the current context, and `aiworkspace/index.md`:

| Situation | Action |
| :--- | :--- |
| No workspaces exist yet | Say so and hand off to [`productivity/define`](../define/SKILL.md), passing the ask along. Resume here after define's gate. |
| The user named a workspace that doesn't exist | Same: hand off to `define` to create it. |
| The workspace exists, but `definition.md` is missing or still the template placeholder | Hand off to `define` to define its core. |
| The ask doesn't fit any existing workspace's scope | Ask: should it go in an existing workspace (which one), or a new one (→ `define`)? |
| One clear match | Confirm it in one line and continue. |

Never plan inside a workspace that hasn't been defined. Its definition is what the plan gets checked against.

### 2. Load context
Read the workspace's `definition.md` and `index.md` (directives, glossary). Then read `aiworkspace/codebase-map.md` (where this kind of change goes and which pattern to copy), the effective `soul.md` persona, and `aiworkspace/project.md`. Skim existing `planning/features/*/plan.md` for overlap or dependencies.

### 3. Check scope against the definition
If the ask falls outside the workspace's defined scope or breaks one of its directives, stop and say so. Offer two ways forward: revise the definition (`/define`, redefine mode) or plan it elsewhere. Don't quietly stretch the scope.

### 4. Name the feature
Agree on a short kebab-case slug (e.g. `csv-export`). Check that `planning/features/<slug>/` doesn't already exist. If it does, this is a revision of that plan, so edit it in place.

### 5. Offer `goal-driven`
Ask: *"Want to frame this with `productivity/goal-driven` (success criteria / constraints / verification / out of scope) first? Recommended, but optional."* Only load it if the user says yes.

### 6. Interview with grill-me
Invoke [`productivity/grill-me`](../grill-me/SKILL.md): one question at a time, each with your recommended answer. Where the codebase or the context files can answer a question, research it instead of asking, and record any findings worth keeping in `planning/research.md` with citations (Directive #2).

Include a constraints question: *"Any constraints this feature must respect beyond the workspace's directives? (performance budget, security/compat limits, must-not-break invariants)"* — this narrows or inherits `definition.md`'s directives rather than repeating them. "None beyond workspace directives" is a valid, explicit answer.

### 7. Write the plan — `planning/features/<slug>/plan.md`
Sections, in order:
1. `## Goal`: only if step 5 was yes.
2. **Problem Statement**
3. **Solution**
4. **User Stories**
5. **Implementation Decisions**: which modules and files are touched, and which existing pattern each change follows (from the codebase map's Change Recipes). For any decision where more than one viable approach existed, record it ADR-style — the decision made, the alternatives considered, and the consequences/trade-offs — not just the choice with no reasoning attached. A decision with only one viable approach doesn't need this; don't manufacture alternatives that were never real.
6. **Constraints**: the quality bar this feature's tasks must not violate — performance budgets, security/compat limits, must-not-break invariants — narrowed from or inheriting the workspace's directives. "None beyond workspace directives" is valid and explicit.
7. **Tasks**: an ordered checklist. Each task is small enough for one `/process` round and has a done-condition, e.g. `- [ ] T1 — Add CsvExporter in internal/export/ (done: unit tests pass)`. `/process` ticks these off.
8. **Resources Needed**: input context, schemas, sample data, and API contracts that Step 2 (`/resources`) must gather.
9. **Testing Decisions**: which test types apply, per [`engineering/testing`](../../engineering/testing/SKILL.md).
10. **Out of Scope**
11. **Further Notes**

Frontmatter: `type: plan`, `scope: feature`, `status: draft`.

### 8. Decision map (large work only)
If the ask doesn't collapse into one plan, add `planning/decisions/<slug>.md` files instead of, or alongside, the plan. Each is OKF `type: resource`, with `status: open | blocked | resolved` and `blocked_by: [...]` pointing at other decision files. The open, unblocked files are the actionable frontier.

### 9. Enrich `index.md` and log
- Write any new domain terms or directives into the workspace `index.md` immediately. It is the glossary.
- Append to `log.md`: the slug, the ask, and where the plan landed.

### 10. Present & gate
Present the plan (and any `index.md`/`log.md` changes) and wait for explicit confirmation before `resources/` work begins (Step 2). Never auto-advance.

## Notes
- Never write to production code from this skill.
- `engineering/code-review`'s Spec-Fidelity axis checks the implementation against this plan and the workspace definition, so keep both specific enough to review against.
- `engineering/software-engineer` requires a plan before any code gets written.
