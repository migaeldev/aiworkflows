---
type: skill_category
title: Engineering Skills Category
description: Skills related to software engineering, dual-axis code review, debugging, TDD, unit/integration/functional/e2e testing, the mandatory software-engineer practices persona, visual iteration, and frontend development formatted per Google OKF specs.
tags: [skills, engineering, category, okf]
timestamp: 2026-09-09T14:02:14+02:00
---

# Engineering Skills

This category contains skills related to software engineering, code review, test-driven development, debugging, and frontend development. Use these skills for tasks that involve writing, analyzing, reviewing, or debugging code.

## Available Skills

### [`api-interface-design`](./api-interface-design/SKILL.md)
Contract-first design for anything consumed by code outside your direct control — Hyrum's Law, the One-Version Rule, error semantics, and boundary validation.

### [`code-review`](./code-review/SKILL.md)
Review code like a skeptical senior engineer on two axes — standards/quality and spec fidelity. Surface hidden assumptions, check for over-engineering, verify test coverage, and check requirements weren't silently descoped.

### [`codebase-map`](./codebase-map/SKILL.md)
With permission, map the host codebase into `aiworkspace/codebase-map.md` — stack, structure, design patterns, conventions, comment scheme, and change recipes for where/how to make changes. Command: `/map`.

### [`codebase-design`](./codebase-design/SKILL.md)
Shared vocabulary and principles for module depth, interfaces, and seams — the deletion test, "the interface is the test surface," and the design-it-twice parallel sub-agent pattern for exploring alternative interfaces.

### [`deprecation-migration`](./deprecation-migration/SKILL.md)
Code-as-liability mindset for retiring old code paths safely — compulsory vs advisory deprecation, migration patterns (strangler fig, shadow/parallel-run, flag-gated cutover), and zombie-code removal.

### [`diagnose`](./diagnose/SKILL.md)
A disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise → instrument → fix → regression-test.

### [`domain-modeling`](./domain-modeling/SKILL.md)
Keep a codebase's domain language — names for concepts, written down in `GLOSSARY.md` — current as decisions crystallize during design or architecture work.

### [`frontend-design`](./frontend-design/SKILL.md)
Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code and UI design that avoids generic AI aesthetics.

### [`improve-codebase-architecture`](./improve-codebase-architecture/SKILL.md)
Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one is picked. Builds on `codebase-design`, `domain-modeling`, and `productivity/grill-me`.

### [`observability`](./observability/SKILL.md)
Structured logging, RED metrics (Rate/Errors/Duration), tracing, and symptom-based alerting — instrument as you build, not after an incident forces you to.

### [`prototype`](./prototype/SKILL.md)
Build a throwaway prototype to answer a design question — a single-file logic demo for state-model sanity checks, or switchable UI variants on a route for "what should this look like?"

### [`research`](./research/SKILL.md)
Spin up a background agent to investigate a question against high-trust primary sources and capture the findings as a cited Markdown file.

### [`software-engineer`](./software-engineer/SKILL.md)
Mandatory discipline for any code-writing task — plan first, pick the right test type, follow test-first, review on two axes before calling it done.

### [`test-first`](./test-first/SKILL.md)
Write failing tests before implementation. Enables LLM self-correction through feedback loops for complex logic and features.

### [`testing`](./testing/SKILL.md)
Decide which test type(s) a change needs — unit, integration, functional, or end-to-end — with per-type scope, speed, and tooling conventions.

### [`visual-iteration`](./visual-iteration/SKILL.md)
UI feedback loop using screenshots. Provide design mock, implement, screenshot result, and iterate until matching target.

### [`web-performance-audit`](./web-performance-audit/SKILL.md)
Audit frontend code for Core Web Vitals regressions, bundle bloat, render-blocking resources, and wasteful client-side fetching. Measure before guessing; rank by real user impact.
