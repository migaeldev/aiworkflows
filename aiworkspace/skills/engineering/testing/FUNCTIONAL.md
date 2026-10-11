---
type: resource
name: testing-functional
title: Functional Testing
description: Scope, speed, and tooling conventions for functional tests.
tags: [testing, functional]
timestamp: 2026-10-04T00:00:00+02:00
---

# Functional Testing

## Scope
One feature or use case, exercised end-to-end *within a single service* — e.g. calling an HTTP endpoint and checking the response, with external dependencies (databases, cloud/AI services, third-party APIs) mocked at the boundary.

## Out of bounds
- Multiple real collaborators without mocking — that's [`INTEGRATION.md`](./INTEGRATION.md).
- Crossing into another service (UI calling the API for real) — that's [`E2E.md`](./E2E.md).

## Speed & isolation
Should still be reasonably fast since external deps are mocked — the slowness of a real network/DB call is exactly what's being avoided here, while still testing the full request→response path of one feature.

## Tooling
- Use the runner(s) recorded in `aiworkspace/project.md`.
- Backend: drive the app through its framework's in-process test client (e.g. Flask/FastAPI `TestClient`, `supertest`, Go `httptest`) with external clients mocked.
- Frontend: component/page-level tests with the API layer mocked.

## Anti-patterns
- Re-testing pure logic already covered by a unit test — assert the feature's behavior, not its internals.
- Mocking so loosely that the test would still pass if the endpoint were broken.
