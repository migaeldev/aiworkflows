---
type: resource
name: testing-e2e
title: End-to-End Testing
description: Scope, speed, and tooling conventions for end-to-end tests in this repo.
tags: [testing, e2e]
timestamp: 2026-10-04T00:00:00+02:00
---

# End-to-End Testing

## Scope
A full, cross-service, user-facing flow — e.g. the Next.js Prompt Workbench calling the real Flask API, which calls real (or realistically sandboxed) BigQuery/Vertex AI, and the UI reflecting the result.

## Out of bounds
- Anything that doesn't need a real UI-to-backend round trip — that's [`FUNCTIONAL.md`](./FUNCTIONAL.md) or [`INTEGRATION.md`](./INTEGRATION.md), and will be faster and more reliable.

## Speed & isolation
Expected to be slow and run less often (e.g. before `/finalize` or `/promote`, not on every `/process` iteration). Should still be deterministic — flaky e2e tests erode trust in the whole suite faster than any other type.

## Tooling (this repo)
- A browser-automation-capable runner (e.g. Playwright-style) driving the Next.js Studio UI, against a running Flask API instance — exact tool choice to be confirmed with the user before adoption, not assumed here.

## Anti-patterns
- Duplicating assertions already covered by unit/functional tests — e2e should verify the *integration* works, not re-verify each layer's internal correctness.
- Testing edge cases here that a unit test could cover in milliseconds instead of seconds.
