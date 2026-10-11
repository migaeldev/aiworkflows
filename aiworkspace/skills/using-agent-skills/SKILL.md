---
type: skill
name: using-agent-skills
title: Using Agent Skills
description: Meta-skill that routes a task to the right skill or specialist agent — not a category member, a top-level entry point. Use whenever it isn't immediately obvious which skill in aiworkspace/skills/ applies, or whether to load a skill directly versus spawn a specialist from aiworkspace/agents/.
tags: [skill, meta, router]
timestamp: 2026-10-11T00:00:00+02:00
---

# Using Agent Skills

A router, not a worker. This skill doesn't do anything itself — it decides what else should.

## Trigger
Consult this first whenever the right skill (or whether to also spawn a specialist agent) isn't obvious from the task alone. `AGENTS.md`'s "Entry Point & Knowledge Architecture" lists it as the first thing to check in that situation.

## Decision table: task shape → what to load

| Task shape | Load |
| :--- | :--- |
| New workspace, or the domain is unclear | [`productivity/define`](../productivity/define/SKILL.md) |
| New feature, change, or batch of work | [`productivity/plan`](../productivity/plan/SKILL.md) |
| Writing or modifying code | [`engineering/software-engineer`](../engineering/software-engineer/SKILL.md) (pulls in testing, test-first, review) |
| Something's broken or regressed | [`engineering/diagnose`](../engineering/diagnose/SKILL.md) |
| About to merge, or you want a second opinion | spawn from [`aiworkspace/agents/`](../../agents/README.md) — see below for which one |
| Security-sensitive change | `agents/security-auditor`, or the specific `security/*` skill directly if the scope is already narrow |
| Frontend or perf-sensitive change | `agents/performance-auditor` |
| Gathering input context for a planned feature | [`productivity/resources`](../productivity/resources/SKILL.md) |
| Ready to gate work into `finalized/` | [`productivity/finalize`](../productivity/finalize/SKILL.md) |
| Human asked to ship | [`productivity/promote`](../productivity/promote/SKILL.md) |
| Need to stress-test a plan or design before committing to it | [`productivity/grill-me`](../productivity/grill-me/SKILL.md) |
| Ending a session, handing off to another agent | [`productivity/handoff`](../productivity/handoff/SKILL.md) |
| Authoring a brand-new skill | [`productivity/write-a-skill`](../productivity/write-a-skill/SKILL.md) |

If more than one row matches, load the earlier-listed one first — most of these cascade into the others (e.g. `software-engineer` already pulls in `testing` and `code-review` at the right moments).

## Skill vs. agent
Both halves of the registry can address the same work; the difference is who's doing it:

- **Load a skill directly** (from `aiworkspace/skills/`) when *you* are doing the work — writing the code, planning the feature, diagnosing the bug. You carry full context from the conversation, which is exactly what you want for execution.
- **Spawn a specialist agent** (from `aiworkspace/agents/`) when you want an *isolated* second opinion from someone who "wasn't in the room" — a reviewer with no attachment to the implementation decisions, no context filled with how the sausage got made. Use this before merging significant work, for security- or performance-sensitive changes, or any time self-review risks confirming your own blind spots.

The roster and spawn instructions live in [`aiworkspace/agents/README.md`](../../agents/README.md); each agent persona names which skill(s) it loads, so the two registries stay in sync rather than duplicating content.
