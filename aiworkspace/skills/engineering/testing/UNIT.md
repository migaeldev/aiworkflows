---
type: resource
name: testing-unit
title: Unit Testing
description: Scope, speed, and tooling conventions for unit tests in this repo.
tags: [testing, unit]
timestamp: 2026-10-04T00:00:00+02:00
---

# Unit Testing

## Scope
One function, class, or module, in isolation. No network, no filesystem, no database, no real external service. If it needs a collaborator, mock or stub it.

## Out of bounds
- Anything that talks to BigQuery, Vertex AI, or a real HTTP endpoint — that's [`INTEGRATION.md`](./INTEGRATION.md) or [`FUNCTIONAL.md`](./FUNCTIONAL.md).
- Testing more than one unit's interaction — that's integration territory, even if it's fast.

## Speed & isolation
Must run fast (milliseconds) and in any order, with no shared state between tests. If a unit test is slow or flaky, something is leaking in a dependency that should have been mocked.

## Tooling (this repo)
- Backend (`apps/feasibility-insights/app/`, Python/Flask): `pytest`, with fixtures for setup — no real BigQuery/Vertex AI clients in a unit test.
- Frontend (`apps/feasibility-insights/ui/`, Next.js): whichever unit test runner the project already uses — confirm with the user before introducing a new one.

## Anti-patterns
- Tests that just check code runs without asserting behavior.
- Tests that duplicate implementation logic instead of checking outcomes.
- Mocking so much that the test no longer exercises real logic.
