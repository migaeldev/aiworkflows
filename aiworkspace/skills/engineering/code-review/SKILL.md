---
type: skill
name: code-review
title: Code Review
description: Review code like a skeptical senior engineer on two axes — standards/quality and spec fidelity. Use when reviewing PRs, after generating significant code, or before merging changes.
tags: [skill, engineering, code-review, quality]
timestamp: 2026-09-09T14:02:14+02:00
---

# Code Review Skill

## Trigger
Use when reviewing code changes, PRs, or after generating significant code.

## Mindset
Review code as a skeptical senior engineer who has seen LLMs make subtle mistakes. The errors won't be syntax - they'll be conceptual: wrong assumptions, missing edge cases, over-engineering, and silent behavior changes.

## Rationalizations
| Excuse | Why it's wrong | Do this instead |
| :--- | :--- | :--- |
| "The diff is small" | Diff size doesn't predict risk — a one-line change can invert a condition or silently descope a requirement | Run both axes regardless of size |
| "I wrote it carefully the first time" | The writer is attached to their own decisions and blind to their own assumptions | Review it anyway, or get a fresh second opinion (see Specialist Roster below) |
| "Spec fidelity doesn't matter if the code is clean" | Clean code that solves the wrong problem is still wrong | Run Axis B independently of Axis A — both must pass |

## Two Axes
A review answers two independent questions, and conflating them hides findings:
- **Axis A — Standards**: is this good code, independent of what it was asked to do?
- **Axis B — Spec Fidelity**: is this the thing that was actually asked for?

Run both. A change can pass one and fail the other — clean code that solves the wrong problem is still wrong, and a faithful implementation with sloppy execution still needs work.

## Axis A — Standards

### 1. Surface Hidden Assumptions
- What assumptions does this code make about inputs, state, or environment?
- Are these assumptions documented or validated?
- Would a different developer reading this code make the same assumptions?
- Flag any assumption that isn't explicitly checked or documented.

### 2. Check for Over-Engineering
- Could this be done in fewer lines without sacrificing clarity?
- Are there abstractions that only have one implementation?
- Are there config options that will never be used?
- Is there a "clever" solution where a simple one would work?
- **Ask yourself: "Could this 1000-line solution be 100 lines?"**

### 3. Verify Consistency
- Does this change conflict with patterns used elsewhere in the codebase?
- Are similar things done similarly?
- Does naming follow existing conventions?
- Are there now two ways to do the same thing?

### 4. Identify Collateral Damage
- Were any comments removed or changed that shouldn't have been?
- Was any code modified that's unrelated to the task?
- Were any imports, exports, or dependencies changed unnecessarily?
- Is there dead code left behind from a refactor?

### 5. Evaluate Tradeoffs
- What are the performance implications?
- What are the maintenance implications?
- What could go wrong? What are the failure modes?
- Is error handling appropriate (not too much, not too little)?

### 6. Test Coverage
- Are the happy paths tested?
- Are edge cases tested?
- Are error conditions tested?
- Do tests actually verify behavior or just check that code runs?
- Which test type(s) apply here? See `engineering/testing`'s router for what "covered" means per layer.

### 7. Change Sizing
- Is this diff reviewable in one sitting? Treat ~100 changed lines as a soft ceiling before a split is worth considering — past that, review quality drops regardless of reviewer care.
- If it's oversized, is that because it's doing more than one thing (splittable: separate the mechanical rename from the behavior change) or because the change is genuinely atomic (not splittable: say so and note why)?
- Flag an oversized, splittable diff as a finding rather than reviewing it anyway and hoping nothing was missed.

## Axis B — Spec Fidelity
Does the implementation actually satisfy what was asked, independent of code quality?

- What was the originating ask? Check `planning/features/<slug>/plan.md` (including its Tasks and Constraints) and the workspace's `definition.md` (scope and directives) if they exist for this work; otherwise the user's original request and `resources/`.
- Does the implementation cover every requirement in that plan — not just the ones that were easiest to build?
- Did anything get silently descoped, simplified, or reinterpreted without flagging it?
- Are there requirements the plan stated that this change doesn't address at all?
- Does the change respect the plan's Constraints section (performance budget, security/compat limits, must-not-break invariants)? A constraint that was quietly weakened to make something easier is a finding, not a tradeoff.
- Flag anything that quietly changed the ask rather than fulfilling it.

## Severity Labels
Tag every finding with one of these — they replace "is this critical or just a suggestion" guesswork with a shared vocabulary:
- **CRITICAL** — must be fixed before merge (either axis).
- **NIT** — a style/polish point; correct as-is, this would just be cleaner. Fine to merge without fixing.
- **OPTIONAL** — a real improvement, not required. The author's call whether to take it.
- **FYI** — informational only; no action implied, just context worth knowing.

## Output Format
```markdown
## Code Review Summary

### Standards Findings
[Axis A: assumptions, over-engineering, consistency, collateral damage, tradeoffs, test coverage, change sizing — each tagged CRITICAL/NIT/OPTIONAL/FYI]

### Spec-Fidelity Findings
[Axis B: requirements met, requirements missed, silent descoping/reinterpretation — each tagged CRITICAL/NIT/OPTIONAL/FYI]

### Critical Issues
[Every CRITICAL finding from either axis, collected here so they can't be missed]

### Suggestions
[NIT/OPTIONAL findings — improvements that would make the code better but don't block merge]

### Simplification Opportunities
[Places where code could be reduced without losing functionality]

### Questions
[Clarifications needed to complete review]
```

## Multi-Agent Review Pattern
The agent that wrote the code has inherent biases — attached to its own decisions, unlikely to question its own assumptions, context filled with implementation details rather than review perspective. A fresh, isolated agent instance reviews with no such baggage.

### Specialist Roster
Rather than writing a one-off reviewer prompt each time, spawn one of the standing personas in [`aiworkspace/agents/README.md`](../../../agents/README.md) as a **fresh** subagent (no shared context with the writer), framed "you did not write this code":

| Persona | Loads | Scope |
| :--- | :--- | :--- |
| `code-reviewer` | this skill | dual-axis Standards + Spec Fidelity |
| `test-engineer` | `engineering/testing` + `test-first` | coverage and test quality |
| `security-auditor` | the applicable `security/*` skills | OWASP, injection, DoS, transport |
| `performance-auditor` | `engineering/web-performance-audit` | Core Web Vitals, bundle size, render blocking |

### When to Use
- Security-sensitive code → `security-auditor`
- Frontend/perf-sensitive code → `performance-auditor`
- Complex business logic, code that will be hard to change later, or before merging significant PRs → `code-reviewer` (and `test-engineer` if coverage is in doubt)
- Any time you want a second opinion untainted by implementation bias

Axis B (Spec Fidelity) benefits most from this pattern specifically, since a reviewer untainted by implementation bias is better positioned to notice quiet scope or constraint changes than the agent that made them.

## Persisted Output
Write the full Output Format block above to `finalized/review.md` (OKF
`type: audit`) in the workspace currently being reviewed, overwriting any
previous version for this unit of work. Append a one-line summary to that
workspace's `log.md` — pass/fail per axis, plus a relative link to
`review.md` — so review results are a durable, version-controlled record
rather than something that only ever existed in chat scrollback.
