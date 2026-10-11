---
type: skill
name: resources
title: Resources (Step 1)
description: Catalog or request the input context, schemas, and raw data a workspace needs for Step 1. Use when starting Step 1 work, or when resources/ is empty or incomplete for the task at hand.
tags: [skill, productivity, lifecycle, step-1]
timestamp: 2026-10-04T00:00:00+02:00
---

# Resources (Step 1)

## Trigger
Use at the start of Step 1 — after Step 0 planning (`productivity/plan`) has determined what this workspace/feature actually needs, or any time `resources/` is checked and found empty or incomplete for the task at hand.

## Process
1. **Check what Step 0 already determined.** If a `planning/project-plan.md` or `planning/features/<slug>/spec.md` exists, read it first — it says what input context, schemas, or data this stage actually needs, so this step isn't guessing.
2. **Inspect `resources/`.** List what's already there against what the plan calls for.
3. **If anything required is missing** — per `AGENTS.md` Directive #1, ask the user for it. Never fabricate schemas, sample data, or API contracts to fill a gap.
4. **If everything needed is present**, confirm that with the user before moving on — don't silently assume completeness.
5. **Present & gate** — once resources are confirmed sufficient, wait for explicit human confirmation before `processing/` work begins. Never auto-advance.

## Notes
- This skill never writes to production code.
- If no Step 0 planning exists yet for this ask, say so and offer to run `productivity/plan` first rather than guessing what belongs here.
