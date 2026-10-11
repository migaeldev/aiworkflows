---
type: skill
name: process
title: Process (Step 3)
description: Run one round of Step 3 work in processing/ — take the next tasks from the feature's plan.md, do them, tick them off, and load engineering/software-engineer whenever code is involved. Re-invocable; each run is one more round, not an auto-advance. Use for /process, or when actively iterating in processing/.
tags: [skill, productivity, lifecycle, step-3]
timestamp: 2026-10-04T00:00:00+02:00
---

# Process (Step 3)

## Trigger
Use for each round of active iteration inside `aiworkspace/workspaces/<domain>/processing/`. This skill is re-invocable — call it again for the next round. It never advances to `finalized/` on its own.

## Process
1. **Confirm scope.** Work against the feature's `planning/features/<slug>/plan.md`, taking the next unchecked task(s) from its **Tasks** list unless the user names others. If not, per `engineering/software-engineer`'s mandated behavior #1, that skill will require one before code gets written — this skill doesn't bypass that.
2. **If the work involves writing or modifying code**, load [`engineering/software-engineer`](../../engineering/software-engineer/SKILL.md) — mandatory per `AGENTS.md` Directive #8, not optional here either.
3. **Do the round of work** — generation, editing, refinement — entirely inside `processing/`. Never touch production code directly (Directive #6).
4. **Tick off tasks** in `plan.md` whose done-condition is met. If a task turned out wrong or new work surfaced, propose the change to the task list instead of silently drifting from the plan.
5. **Report what changed** this round and which tasks are left, rather than silently continuing to the next round unprompted.
6. **Stop.** Do not move anything to `finalized/` from this skill. That's `productivity/finalize`'s job, triggered separately and explicitly.

## Notes
- Calling this skill repeatedly is the expected pattern for iterating — "done" is a human judgment call, not something this skill decides.
