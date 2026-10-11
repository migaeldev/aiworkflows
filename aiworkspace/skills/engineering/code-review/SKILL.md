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

## Axis B — Spec Fidelity
Does the implementation actually satisfy what was asked, independent of code quality?

- What was the originating ask? Check `planning/features/<slug>/plan.md` (including its Tasks) and the workspace's `definition.md` (scope and directives) if they exist for this work; otherwise the user's original request and `resources/`.
- Does the implementation cover every requirement in that plan — not just the ones that were easiest to build?
- Did anything get silently descoped, simplified, or reinterpreted without flagging it?
- Are there requirements the plan stated that this change doesn't address at all?
- Flag anything that quietly changed the ask rather than fulfilling it.

## Output Format
```markdown
## Code Review Summary

### Standards Findings
[Axis A: assumptions, over-engineering, consistency, collateral damage, tradeoffs, test coverage]

### Spec-Fidelity Findings
[Axis B: requirements met, requirements missed, silent descoping/reinterpretation]

### Critical Issues
[Issues that must be fixed before merge, from either axis]

### Suggestions
[Improvements that would make the code better]

### Simplification Opportunities
[Places where code could be reduced without losing functionality]

### Questions
[Clarifications needed to complete review]
```

## Multi-Agent Review Pattern
Agent Best Practice: Run separate AI agent instances or subagents in parallel—one writing code, another reviewing.

### Why Separate Instances
The agent that wrote the code has inherent biases:
- Attached to its own implementation decisions
- May not question its own assumptions
- Context filled with implementation details, not review perspective

A fresh, isolated agent instance:
- Reviews with fresh eyes
- Questions decisions the writer took for granted
- Catches issues the writer is blind to

### How to Set Up

**Session / Agent 1 - Writer:**
```bash
# Agent Session 1: Implement the feature
```

**Session / Agent 2 - Reviewer:**
```bash
# Agent Session 2 or Subagent invocation:
# "Review the changes in src/feature/.
#  You did NOT write this code. Review critically for:
#  - Hidden assumptions
#  - Missing edge cases
#  - Over-engineering
#  - Security issues
#  - Performance problems"
```

### Review Prompts for Reviewer Instance

```markdown
Review the following code changes as if you're seeing them for the first time.
You did NOT write this code. Be skeptical.

Focus on:
1. What assumptions does this code make that aren't validated?
2. What inputs would break this?
3. Is there a simpler way to achieve the same result?
4. What's missing from the error handling?
5. Are there any security implications?

Be direct about issues. Don't soften criticism.
```

### When to Use Multi-Agent Review
- Security-sensitive code
- Complex business logic
- Code that will be hard to change later
- Before merging significant PRs
- When you want a second opinion

Axis B (Spec Fidelity) benefits most from this pattern specifically, since a
reviewer untainted by implementation bias is better positioned to notice
quiet scope changes than the agent that made them.

## Persisted Output
Write the full Output Format block above to `finalized/review.md` (OKF
`type: audit`) in the workspace currently being reviewed, overwriting any
previous version for this unit of work. Append a one-line summary to that
workspace's `log.md` — pass/fail per axis, plus a relative link to
`review.md` — so review results are a durable, version-controlled record
rather than something that only ever existed in chat scrollback.
