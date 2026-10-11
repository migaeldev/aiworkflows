---
type: skill
name: codebase-design
title: Codebase Design Vocabulary
description: Shared vocabulary and principles for talking about module depth, interfaces, and seams — module, interface, depth, seam, adapter, leverage, locality — plus the deletion test and the design-it-twice pattern for exploring alternative interfaces. Also carries this repo's per-stack conventions (Python and Go hexagonal layout, frontend API/UI separation, testing, function design, logging). Use when reviewing architecture, naming a refactor, deciding whether a seam is real, or writing new code in any of this repo's stacks.
tags: [skill, engineering, architecture, vocabulary, design, python, go, frontend, testing, logging]
timestamp: 2026-10-05T12:00:00+02:00
---

# Codebase Design Vocabulary

## Trigger
Load this skill whenever discussing module boundaries, proposing a refactor, or deciding whether an abstraction earns its place — most often from [`engineering/improve-codebase-architecture`](../improve-codebase-architecture/SKILL.md), but also standalone whenever a reviewer needs shared nouns to talk about shape rather than syntax.

## Vocabulary
Use these terms exactly. Drifting into "component," "service," "API," "boundary," "layer," or "wrapper" when one of these is meant erodes the vocabulary's value — the whole point is that everyone means the same thing by the same word.

- **Module** — a unit of code with a boundary: a function, class, file, or package, considered as a whole.
- **Interface** — everything a module's callers must know to use it: its signature, its contract, its side effects, its failure modes. Not just the type signature — the *test surface*, too.
- **Implementation** — everything a module's callers don't need to know: the internals behind the interface.
- **Depth** — the ratio of functionality to interface complexity. A module is **deep** when a simple interface hides substantial implementation (e.g. a filesystem call, a compiler pass). A module is **shallow** when the interface is nearly as complex as the implementation — it costs almost as much to learn the interface as to write the logic yourself.
- **Seam** — a place in the code where behavior can be substituted without editing the module itself (per Michael Feathers). Seams are what make a module testable in isolation and swappable in production.
- **Adapter** — the concrete thing plugged into a seam: a database client, an HTTP client, a stub, a fake.
- **Leverage** — how much value one well-placed interface returns across all its call sites. High leverage: one interface change fixes N callers. Low leverage: an abstraction with exactly one caller.
- **Locality** — how close the code that causes a bug is to the code that exhibits it. High locality: the bug and the fix live in the same module. Low locality: the real problem is in how a function is *called*, not in the function itself — pulling a "pure" function out for testability without fixing this doesn't help.

## Principles

### The deletion test
To tell whether a module is shallow (and should be collapsed) or deep (and should stay), ask: if this module were deleted and its one caller inlined, would complexity concentrate in one place, or would it just move sideways? **"Concentrates" is the signal that the module was shallow** — it existed to split code, not to hide anything. **"Moves" means it was deep** — something real was hidden, and deleting it only relocates the hiding.

### The interface is the test surface
A module's interface isn't just what callers see — it's the surface a test has to drive. When a module's interface is narrow but its implementation does real work, tests are cheap to write and stay valid as the implementation changes. When a module is shallow, tests end up asserting on implementation details because there's nothing else to assert on, and they break on every refactor that doesn't change behavior.

### One adapter = hypothetical seam, two = real
A seam justifies itself when it has **two or more adapters that actually exist** — e.g. a real HTTP client in production and a fake in tests, or two real backends. A seam with exactly one real adapter ("we might swap databases someday") is a hypothetical seam: it pays the abstraction cost today for a benefit that may never arrive. Don't introduce a seam speculatively; introduce it when the second adapter is already needed.

## The design-it-twice pattern
When a deepened module's interface isn't obviously right, don't commit to the first shape. Spawn two (or three) parallel sub-agents, each handed the same problem statement and constraints but told nothing about the others' approach. Ask each to produce a candidate interface plus a one-paragraph rationale. Then compare: where they agree, that's probably the real shape; where they disagree, the disagreement usually points at an underspecified constraint worth resolving before writing code. This is cheap relative to building the wrong interface and discovering it three call sites later.

## Language & Stack Conventions
The vocabulary above is language-agnostic; these are how this repo applies it per stack. New code in any of these stacks should hold itself to the matching section, not just the abstract principles.

### Python — hexagonal (`cmd/` + `internal/`)
This is the layout [`apps/feasibility-insights/app`](../../../../apps/feasibility-insights/app) already uses, and the standard for any new Python service in this repo:

- **`cmd/<entrypoint>/main.py`** holds driving adapters only — wiring, not logic. `cmd/api/main.py` (Flask, Cloud Run Service) and `cmd/cli/main.py` (batch runner, Cloud Run Job) are two real adapters driving the same core, which is exactly what justifies that seam (see "one adapter = hypothetical seam, two = real" above) — neither should contain business logic the other would have to duplicate.
- **`internal/logic/`** is the hexagon's interior. `internal/logic/insights_engine.py`'s `run_insights_pipeline` is a deep module done right: a narrow interface (`client_name`, `relative_period`, `overwrite`) hides BigQuery extraction, Gemini generation, normalization, and a MERGE — deleting it would concentrate that complexity elsewhere, not remove it, which is the deletion test's "moves, don't inline" signal for keeping a module.
- **`internal/config.py`** is the one adapter between the process environment and everything else. Nothing outside it should call `os.environ.get(...)` directly — that's the seam, and it's why `_normalize_table`'s table-name construction lives there instead of being copy-pasted at each call site.
- **`internal/sql/`** is the driven-adapter side for BigQuery: parameterized `.sql` templates loaded through `load_and_format_sql`, not strings built ad hoc in `internal/logic/`.
- Keep the pure helpers pure. `format_duration_human`, `truncate_to_complete_sentences`, and `safe_format_prompt` in `insights_engine.py` take plain data in and return plain data out, with no BigQuery, Gemini, or Flask imports — that's what makes them cheap to unit-test and safe to change independently of the pipeline around them.

### Go — same hexagonal convention
No Go service has landed in this repo yet, but when one does, it follows the identical shape as Python, with Go's own compiler-enforced seam added on top:

- **`cmd/<entrypoint>/main.go`** per driving adapter (HTTP server, worker, scheduler, CLI) — same role as `cmd/api/main.py` / `cmd/cli/main.py`, just compiled.
- **`internal/`** holds everything not meant to be imported outside the module. Go enforces this at compile time — a free depth guarantee Python and TypeScript don't have, so lean on it instead of re-deriving access discipline by convention.
- Package `internal/` by what a module *does* (`internal/logic`, `internal/store`, `internal/config`), not by technical layer (`internal/models`, `internal/handlers`, a catch-all `internal/services`) — same locality principle as the Python layout, just with Go package names instead of Python module names.
- Define ports as small, consumer-defined interfaces at the point of use ("accept interfaces, return structs" — idiomatic Go), not a wide interface declared in the producer's package. `type InsightsStore interface { Save(ctx context.Context, i Insight) error }` is a seam; a twelve-method `Repository` interface is usually a shallow module wearing an interface as a costume.
- The two-adapters rule applies unchanged: a real store and a fake store implementing the same port justify the interface. If only one concrete implementation will ever exist, keep the concrete type and skip the interface — an interface with one implementation is the hypothetical seam this skill's principles already warn against, Go or not.

### Frontend — split API logic from UI
[`apps/feasibility-insights/ui/src/app/page.tsx`](../../../../apps/feasibility-insights/ui/src/app/page.tsx) currently calls `fetch()` directly inside the page component — API logic and UI logic sharing one module, the same shallow-seam problem as above, just in TypeScript. Treat this as the anti-pattern to avoid in new frontend work, not as the pattern to copy:

- Give API calls their own module behind a narrow interface — one file per backend resource (e.g. `src/lib/api/insights.ts` exporting `generateInsights(params): Promise<InsightsResult>`), consumed from components via a hook (`useInsights()`) or an event handler. A raw `fetch(` inside a `.tsx` file is a smell on sight.
- This buys two real adapters almost for free: the real `fetch`-backed implementation, and a fake/mock implementation for component tests — satisfying "one adapter = hypothetical seam, two = real" the moment a test is written against the interface instead of against `page.tsx`.
- Pick one pattern (a thin `ApiClient` class, or plain exported functions per resource) and apply it consistently across the UI rather than inventing a new shape per page — consistency matters more than which pattern wins.
- Shape API responses into domain terms inside the API module, not in JSX. A component's props are its interface, and that interface should already speak the vocabulary above (`InsightsResult`), not raw wire-format JSON.

### Testing
[`engineering/testing`](../testing/SKILL.md) decides unit vs. integration vs. functional vs. e2e; this skill only adds the design angle on top: **depth determines what's worth testing.** A deep module's narrow interface is cheap to test thoroughly and stays valid across internal refactors. A shallow module resists good tests — tests end up asserting on implementation details — which is itself a signal to deepen the module, not to write more mocks.

- **Python**: unit-test the pure functions in `internal/logic/` directly, with no mocking required, since they take plain data in and out. Integration-test `internal/sql/` queries against BigQuery rather than mocking the query string. Don't unit-test `internal/config.py` by mocking `os.environ` at every call site — it's a leaf adapter; trust it, or replace it wholesale in an integration test.
- **Go**: table-driven tests (`[]struct{ name string; in X; want Y }`) are the idiomatic shape for single-purpose-function tests. `net/http/httptest` is the standard adapter-level fake for HTTP ports — reach for it before hand-rolling a mock server.
- **Frontend**: once API logic is split out (see above), component tests exercise the UI through its props, not through fetch internals buried inside the component.

### Function design — single-purpose and clean
One job per function, named for that job. `format_duration_human`, `truncate_to_complete_sentences`, and `safe_format_prompt` in `insights_engine.py` are the standard to hold new functions to: each does exactly what its name says, takes plain inputs, returns a plain output, and has no side effects.

- A function doing two things ("fetch and format," "validate and save") is a signal to split it at the "and" — the two halves usually have different test needs and different reasons to change.
- The deletion test applies at function granularity too, not just module granularity: if inlining a function at its one call site would concentrate logic, it was pulling its weight; if it existed only to shorten a long function, inlining it back is fine.

### Logging
Every service boundary — an API entrypoint, a CLI entrypoint, a background job — gets structured logging from the start, not bolted on during debugging.

- This repo's existing convention, visible in both `cmd/api/main.py` and `internal/logic/insights_engine.py`: one `logger = logging.getLogger("<component-name>")` per module, configured once centrally (`logging.basicConfig` with timestamp, level, logger name, and `file:line`). Never bare `print()`.
- Log at seams, not inside pure functions. `cmd/api/main.py`'s error handlers log every 400/404/500 with context before responding; `internal/logic` logs around the expensive or fallible steps (BigQuery extraction, Gemini generation) — not inside `format_duration_human`. A pure function that logs is no longer pure, and its presence there is a sign logging crept into the wrong layer.
- **Go**: use the standard library `log/slog` for structured, key-value logging instead of formatted strings, so log lines stay queryable.
- Never log a request/response payload wholesale in production. Log identifiers (`client_name`, a request id) and outcomes — not raw PII or full prompt/response bodies.

## Using this vocabulary in review
- Name the module's depth before proposing a change to it — shallow modules get collapsed or absorbed, deep modules get protected.
- When proposing a seam, name both adapters it needs to justify itself, not just the first one.
- When proposing a deepening, describe the win in terms of **locality** and **leverage** ("bugs concentrate in one module," "one interface, N call sites"), not generic terms like "cleaner" or "easier to maintain" — those don't carry information.
- When writing new code rather than reviewing existing code, hold it to the matching stack section above from the start, rather than deferring cleanliness, testing, or logging to a later pass.
