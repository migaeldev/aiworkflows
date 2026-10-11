---
type: skill
name: testing
title: "Testing: Pick the Right Type"
description: Decide which test type(s) a change needs — unit, integration, functional, or end-to-end — and link to the right conventions for each. Use when deciding what kind of test to write, or when a feature/PR needs test coverage across layers.
tags: [skill, engineering, testing, quality]
timestamp: 2026-10-04T00:00:00+02:00
---

# Testing: Pick the Right Type

## Trigger
Use when deciding what kind of test a change needs, or when `engineering/code-review`'s Standards axis asks "is this covered?" and you need to know what "covered" means for this layer.

## Decision table

| What's changing | Test type | Reference |
|---|---|---|
| A pure function / isolated class / single module, no I/O | Unit | [`UNIT.md`](./UNIT.md) |
| Two or more real collaborators wired together, still inside one service (e.g. a repository talking to a real local DB) | Integration | [`INTEGRATION.md`](./INTEGRATION.md) |
| One feature/endpoint/use case, external deps mocked at the boundary | Functional | [`FUNCTIONAL.md`](./FUNCTIONAL.md) |
| A cross-service, user-facing flow (e.g. UI → API → data store) | End-to-end | [`E2E.md`](./E2E.md) |

Most non-trivial changes need more than one type — a new endpoint usually wants unit tests for its pure logic *and* a functional test for the endpoint itself. Pick every type that applies, not just one.

## Process
1. Read the decision table above and identify every type that applies to this change.
2. Open each matching reference file and follow its scope/tooling/anti-pattern guidance.
3. Run the loop in [`engineering/test-first`](../test-first/SKILL.md) (write failing test → run → implement → run → refactor) for each test you write — this skill tells you *what kind*, `test-first` tells you *how to write it*.
4. When `engineering/code-review`'s Standards axis checks test coverage, point it at the types you picked here.

## Anti-pattern
Don't reach for e2e to test something a unit test could cover faster and more reliably. Pick the cheapest type that actually exercises the risk.
