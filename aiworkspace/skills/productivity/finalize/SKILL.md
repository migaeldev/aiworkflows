---
type: skill
name: finalize
title: Finalize (Step 3)
description: Run the four mandatory verification gates plus the dual-axis code-review, then move passing content from processing/ to finalized/. Use when the human explicitly asks to finalize, approve, or audit the current processing/ work.
tags: [skill, productivity, lifecycle, step-3]
timestamp: 2026-10-04T00:00:00+02:00
---

# Finalize (Step 3)

## Trigger
Use only when explicitly requested by the human, after they've approved the current `processing/` work. Never self-trigger — `AGENTS.md` Directive #7 requires explicit human instruction for this transition.

## Process
1. **Run the four mandatory gates** (`AGENTS.md` Step 3):
   1. Security Audit Logging — run the relevant `security/` skills, log findings in `log.md`.
   2. OpenAPI Specs Generation — for any HTTP/REST APIs touched.
   3. Production-Ready Documentation — architecture notes, READMEs, deployment specs.
   4. Final System Verification & Tests — compilation/syntax checks, test suites, zero errors.
2. **Run the dual-axis review** — [`engineering/code-review`](../../engineering/code-review/SKILL.md) (Standards + Spec Fidelity). Its persisted output goes to `finalized/review.md`, with a summary line appended to `log.md`.
3. **If every gate and both axes pass** — move the passing content from `processing/` to `finalized/`.
4. **If anything fails** — report exactly what failed (which gate, which axis) and stay in `processing/`. Do not move partial or failing content.
5. **Stop and wait.** Do not proceed to `promote` from this skill — that's `productivity/promote`'s job, triggered separately and explicitly.

## Notes
- This skill never writes to `apps/[workspace]`.
