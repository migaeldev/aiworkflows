---
type: skill
name: process
title: Process (Step 2)
description: Run one iteration of Step 2 work in processing/ — loading engineering/software-engineer whenever code is involved. Re-invocable; each run is one more round, not an auto-advance. Use when actively iterating in processing/.
tags: [skill, productivity, lifecycle, step-2]
timestamp: 2026-10-04T00:00:00+02:00
---

# Process (Step 2)

## Trigger
Use for each round of active iteration inside `aiworkspace/workspaces/<domain>/processing/`. This skill is re-invocable — call it again for the next round. It never advances to `finalized/` on its own.

## Process
1. **Confirm scope.** If this unit of work has a Step 0 plan (`planning/project-plan.md` or a `planning/features/<slug>/spec.md`), work against it. If not, per `engineering/software-engineer`'s mandated behavior #1, that skill will require one before code gets written — this skill doesn't bypass that.
2. **If the work involves writing or modifying code**, load [`engineering/software-engineer`](../../engineering/software-engineer/SKILL.md) — mandatory per `AGENTS.md` Directive #8, not optional here either.
3. **Do the round of work** — generation, editing, refinement — entirely inside `processing/`. Never touch `apps/[workspace]` directly (Directive #6).
4. **Report what changed** this round and what's left, rather than silently continuing to the next round unprompted.
5. **Stop.** Do not move anything to `finalized/` from this skill. That's `productivity/finalize`'s job, triggered separately and explicitly.

## Notes
- Calling this skill repeatedly is the expected pattern for iterating — "done" is a human judgment call, not something this skill decides.
