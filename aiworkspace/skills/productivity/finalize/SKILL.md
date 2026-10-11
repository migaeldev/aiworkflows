---
type: skill
name: finalize
title: Finalize (Step 3)
description: Run every applicable verification gate plus the dual-axis code-review, then move passing content from processing/ to finalized/. Use when the human explicitly asks to finalize, approve, or audit the current processing/ work.
tags: [skill, productivity, lifecycle, step-3]
timestamp: 2026-10-04T00:00:00+02:00
---

# Finalize (Step 3)

## Trigger
Use only when explicitly requested by the human, after they've approved the current `processing/` work. Never self-trigger — `AGENTS.md` Directive #7 requires explicit human instruction for this transition.

## Process
1. **Run every applicable gate** (`AGENTS.md` Step 3). For each gate, log `PASS`, `FAIL`, or `N/A — <reason>` in `log.md`; never skip one silently:
   1. Security Audit *(always)* — run the relevant `security/` skills, log findings.
   2. API Specification *(only if an HTTP/REST API is exposed or changed)* — generate/update an OpenAPI 3.x spec.
   3. Production-Ready Documentation *(always)* — READMEs, plus architecture/deployment notes where warranted.
   4. Verification & Tests *(always)* — run the build/lint/test commands from `aiworkspace/project.md`. If the project has no tests, record what verification was done instead.
2. **Run the dual-axis review** — [`engineering/code-review`](../../engineering/code-review/SKILL.md) (Standards + Spec Fidelity). Its persisted output goes to `finalized/review.md`, with a summary line appended to `log.md`.
3. **If every applicable gate and both axes pass** — move the passing content from `processing/` to `finalized/`.
4. **If anything fails** — report exactly what failed (which gate, which axis) and stay in `processing/`. Do not move partial or failing content.
5. **Propose context updates** — if this work introduced a new pattern, area, entry point, or convention, propose the matching edit to `aiworkspace/codebase-map.md` (and to `soul.md` if the project's style changed). Apply only on approval.
6. **Stop and wait.** Do not proceed to `promote` from this skill — that's `productivity/promote`'s job, triggered separately and explicitly.

## Notes
- This skill never writes to production code.
