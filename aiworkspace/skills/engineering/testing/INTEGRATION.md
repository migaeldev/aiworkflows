---
type: resource
name: testing-integration
title: Integration Testing
description: Scope, speed, and tooling conventions for integration tests.
tags: [testing, integration]
timestamp: 2026-10-04T00:00:00+02:00
---

# Integration Testing

## Scope
Two or more real collaborators wired together, inside a single service boundary — e.g. a repository class against a real local database, or a client wrapper against a real (sandboxed/emulated) external service.

## Out of bounds
- Testing a single isolated function — that's [`UNIT.md`](./UNIT.md).
- Testing a full user-facing flow across services — that's [`E2E.md`](./E2E.md).

## Speed & isolation
Slower than unit tests and allowed to be — they may hit a real local DB, emulator, or sandboxed API. Still shouldn't depend on production data or external services that aren't reproducible in CI.

## Tooling
- Use the runner(s) recorded in `aiworkspace/project.md`.
- Data stores: a disposable local/test database, container, or official emulator — never production tables or datasets.
- Frontend: exercise the app's API layer against a real local/dev backend instance rather than a fully mocked one.

## Anti-patterns
- Mocking the one collaborator the test exists to verify.
- Depending on data that only exists in a specific environment.
