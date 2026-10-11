---
type: skill
name: finalize
title: Finalize (Step 4)
description: Run every applicable verification gate plus the dual-axis code-review, then move passing content from processing/ to finalized/. Use when the human explicitly asks to finalize, approve, or audit the current processing/ work.
tags: [skill, productivity, lifecycle, step-4]
timestamp: 2026-10-04T00:00:00+02:00
---

# Finalize (Step 4)

## Trigger
Use only when explicitly requested by the human, after they've approved the current `processing/` work. Never self-trigger — `AGENTS.md` Directive #7 requires explicit human instruction for this transition.

## Rationalizations
| Excuse | Why it's wrong | Do this instead |
| :--- | :--- | :--- |
| "This test is flaky, I'll mark it pass" | A flaky test is an unverified claim, not a passing one — marking it PASS is exactly the "silence the check to go green" failure mode this gate exists to catch | Log it `FAIL` with the flake noted, or fix the flake first |
| "Security audit doesn't apply here" | That might be true, but it's a claim that needs a reason, not an assumption | Log `N/A — <specific reason>`, never a silent skip |
| "Docs can come later" | "Later" is outside this gate's visibility — once content moves to `finalized/`, nothing forces it to happen | Write them now, or don't move this content yet |

## Process
1. **Run every applicable gate** (`AGENTS.md` Step 4). For each gate, log `PASS`, `FAIL`, or `N/A — <reason>` in `log.md`; never skip one silently:
   1. Security Audit *(always)* — run the relevant `security/` skills, log findings.
   2. API Specification *(only if an HTTP/REST API is exposed or changed)* — generate/update an OpenAPI 3.x spec.
   3. Production-Ready Documentation *(always)* — READMEs, plus architecture/deployment notes where warranted. Also confirm any multi-approach decision in the plan's Implementation Decisions is recorded ADR-style (alternatives considered, consequences) — a bare assertion of the choice made isn't sufficient documentation for a decision that had real alternatives.
   4. Verification & Tests *(always)* — run the build/lint/test commands from `aiworkspace/project.md`. If the project has no tests, record what verification was done instead. Also confirm the plan's **Constraints** section wasn't silently violated or weakened to get a green run.
   - **Evidence rule**: every `PASS` must cite the evidence that earned it — the test command and its output, the build log excerpt, the specific file/section reviewed, the specific audit findings file. A `PASS` with no citation is itself a `FAIL` on this meta-gate and must be redone. No check may be silenced, skipped, or marked passing just to force a green run.
2. **Run the dual-axis review** — [`engineering/code-review`](../../engineering/code-review/SKILL.md) (Standards + Spec Fidelity, including the plan's Constraints). Its persisted output goes to `finalized/review.md`, with a summary line appended to `log.md`.
3. **If every applicable gate and both axes pass** — move the passing content from `processing/` to `finalized/`.
4. **If anything fails** — report exactly what failed (which gate, which axis) and stay in `processing/`. Do not move partial or failing content.
5. **Propose context updates** — if this work introduced a new pattern, area, entry point, or convention, propose the matching edit to `aiworkspace/codebase-map.md` (and to `soul.md` if the project's style changed). Apply only on approval.
6. **Stop and wait.** Do not proceed to `promote` from this skill — that's `productivity/promote`'s job, triggered separately and explicitly.

## Notes
- This skill never writes to production code.
