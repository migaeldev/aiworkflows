---
type: skill
name: process
title: Process (Step 3)
description: Run one round of Step 3 work in processing/ — take the next tasks from the feature's plan.md, do them, tick them off, and load engineering/software-engineer whenever code is involved. Re-invocable; each run is one more round, not an auto-advance. `/process auto` runs every remaining task in one approved pass, still test-driven and halting on failure. Use for /process or /process auto, or when actively iterating in processing/.
tags: [skill, productivity, lifecycle, step-3, auto-mode]
timestamp: 2026-10-04T00:00:00+02:00
---

# Process (Step 3)

## Trigger
Use for each round of active iteration inside `aiworkspace/workspaces/<domain>/processing/`. This skill is re-invocable — call it again for the next round. It never advances to `finalized/` on its own. `/process auto` runs the same discipline across every remaining task in one pass (see "Auto mode" below).

## Process
1. **Confirm scope.** Work against the feature's `planning/features/<slug>/plan.md`, taking the next unchecked task(s) from its **Tasks** list unless the user names others. If not, per `engineering/software-engineer`'s mandated behavior #1, that skill will require one before code gets written — this skill doesn't bypass that.
2. **If the work involves writing or modifying code**, load [`engineering/software-engineer`](../../engineering/software-engineer/SKILL.md) — mandatory per `AGENTS.md` Directive #8, not optional here either.
3. **Do the round of work** — generation, editing, refinement — entirely inside `processing/`. Never touch production code directly (Directive #6).
4. **Tick off tasks** in `plan.md` whose done-condition is met. If a task turned out wrong or new work surfaced, propose the change to the task list instead of silently drifting from the plan.
   - **Commit at task granularity — per the configured Commit Policy.** This is `engineering/software-engineer`'s mandated behavior #7; this skill is where it actually fires. Not a git-backed workspace, or no VCS in use → skip this and say so. Otherwise, read `aiworkspace/project.md`'s **Commit policy**:
     - **`unset`** — ask the user once which mode they want (`auto` / `ask` / `manual` — see `project.md`'s Git Workflow section for what each means), record the answer in `project.md`, then proceed under it for this and every future task.
     - **`auto`** — commit the task's change immediately, one atomic commit per task (or per tight group of trivial tasks), referencing the task ID (e.g. `T1 — Add CsvExporter`). No per-commit confirmation needed.
     - **`ask`** — propose the commit (message + files) and wait for a yes before running it. A "no" or no response means the change stays uncommitted; move on to the next task rather than re-asking.
     - **`manual`** — never run `git commit`. Note in this round's report that the task's change is ready, with a suggested commit message, and leave committing to the user.
5. **Report what changed** this round and which tasks are left, rather than silently continuing to the next round unprompted.
6. **Stop.** Do not move anything to `finalized/` from this skill. That's `productivity/finalize`'s job, triggered separately and explicitly.

## Auto mode
`/process auto` trades the per-round pause for a single upfront approval, then runs steps 1-4 above repeatedly across *every* remaining unchecked task in `plan.md` — each task still goes through `software-engineer`'s discipline when code is involved, still gets its own test-first loop, and still gets ticked off individually. It is not a way to skip rigor, only a way to skip asking between tasks that don't need it.

- **Halt immediately** on a test failure, a gate-shaped problem, or a task that needs a decision `plan.md` doesn't cover. Report exactly what happened and which task it stopped on, then wait — don't guess and keep going.
- **Never** moves anything to `finalized/` (unchanged from step 6) — that boundary doesn't move just because this mode is faster.
- **Commit policy under `ask`**: stopping to ask before every commit would defeat the point of auto mode. Say so up front as part of the single approval ("this run will commit each task as it completes — ok?") and, once approved, commit each task automatically for the rest of that run — same as `auto` policy, but only for this invocation; the project's setting in `project.md` stays `ask` for ordinary `/process` rounds. `manual` policy stays `manual` even in auto mode — tasks are noted as ready, nothing gets auto-committed.
- **At the end** (whether it finished everything or halted partway), report everything that changed across all rounds and which tasks remain, same as single-round mode would after its last round.

## Notes
- Calling this skill repeatedly is the expected pattern for iterating — "done" is a human judgment call, not something this skill decides.
