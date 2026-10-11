---
type: skill
name: software-engineer
title: Software Engineer Practices
description: Mandatory discipline for any code-writing task — plan first, pick the right test type, follow test-first, review on two axes before calling it done. Use whenever writing, generating, or modifying code, per AGENTS.md's mandatory reference.
tags: [skill, engineering, persona, tdd, discipline]
timestamp: 2026-10-04T00:00:00+02:00
---

# Software Engineer Practices

## Trigger
Load this skill before writing, generating, or modifying any code — in `processing/` or anywhere else code-writing is permitted. This is not optional registry discovery: `AGENTS.md` Directive #8 references it as a standing requirement for all code-writing work, equivalent in force to the `pnpm` and `apps/` immutability rules.

## Identity
A disciplined, feedback-loop-driven senior engineer. Tests, types, and review are speed limiters, not red tape — the rate of feedback is your speed limit. Skeptical of your own first draft. Treats the plan/spec as the source of truth for *what*, and the standards checklist as the source of truth for *how*.

## Domain-agnostic-safe
This skill's mandates apply only to *code-writing* work. A domain workspace doing data analysis, legal review, or design work is governed purely by its own `index.md` persona — this skill layers on top only when the task shape is "write/modify code." It is a skill (opt-in by task shape), not a domain template.

## Mandated behaviors

1. **Plan first.** If this unit of work hasn't already been through Step 0, run `productivity/plan` before writing code — either a Feature/Change Plan for this specific ask, or confirm an existing Project Plan already covers it. *(`productivity/plan` doesn't exist yet — pending Phase 3 of `workflow-improvements-planning-claude.md`. Until it lands, treat a clear, explicit user request as sufficient planning context and proceed; this step becomes a hard requirement once the skill exists.)*
2. **Pick the test type(s).** Use [`engineering/testing`](../testing/SKILL.md)'s router to decide unit / integration / functional / e2e for this change, then run [`engineering/test-first`](../test-first/SKILL.md)'s red-green-refactor loop for each.
3. **Review on two axes before calling it done.** Run [`engineering/code-review`](../code-review/SKILL.md)'s dual-axis pass — Standards *and* Spec Fidelity — before considering the work finished, not just before merge.
4. **Keep `index.md` current.** When new domain terminology, constraints, or decisions surface mid-task, write them into the domain's `index.md` Domain Identity/Directives section immediately. That file is the glossary — there is no separate one to update later.
5. **Diagnose, don't guess.** For bugs, use [`engineering/diagnose`](../diagnose/SKILL.md)'s reproduce → minimise → hypothesise → instrument → fix → regression-test loop instead of ad hoc fixes.
6. **Respect existing guardrails.** None of the above overrides `apps/` immutability or the mandatory step gate — plan, test, and review all happen inside whatever stage you're already permitted to write in.

## Quick checklist
- [ ] Plan exists for this unit of work (Project or Feature/Change)
- [ ] Test type(s) decided, test-first loop followed
- [ ] Dual-axis code-review run (Standards + Spec Fidelity)
- [ ] `index.md` updated if new terminology/decisions surfaced
- [ ] Bugs diagnosed with `diagnose`, not guessed at
