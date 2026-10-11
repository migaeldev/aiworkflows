---
type: skill
name: codebase-design
title: Codebase Design Vocabulary
description: Shared vocabulary and principles for talking about module depth, interfaces, and seams — module, interface, depth, seam, adapter, leverage, locality — plus the deletion test and the design-it-twice pattern for exploring alternative interfaces. Also carries default per-stack conventions (Python and Go hexagonal layout, frontend API/UI separation, testing, function design, logging). Use when reviewing architecture, naming a refactor, deciding whether a seam is real, or writing new code.
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
The vocabulary above is language-agnostic; these are default conventions for applying it per stack. **The host project's established layout wins**: if the repo already has a consistent structure, follow it and record it in `aiworkspace/project.md` — use the defaults below only for new services or where no convention exists yet.

### Python — hexagonal (`cmd/` + `internal/`)
- **`cmd/<entrypoint>/main.py`** holds driving adapters only — wiring, not logic. An HTTP API and a batch CLI driving the same core are two real adapters, which is exactly what justifies that seam (see "one adapter = hypothetical seam, two = real") — neither should contain business logic the other would have to duplicate.
- **`internal/logic/`** is the hexagon's interior. A deep module here has a narrow interface (e.g. `run_pipeline(client, period, overwrite)`) hiding extraction, transformation, external calls, and persistence — deleting it would move that complexity elsewhere, not remove it, which is the deletion test's signal to keep it.
- **`internal/config.py`** is the one adapter between the process environment and everything else. Nothing outside it calls `os.environ.get(...)` directly.
- **`internal/sql/`** (or `internal/store/`) is the driven-adapter side for data access: parameterized query templates, not strings built ad hoc in `internal/logic/`.
- Keep pure helpers pure: formatting, truncation, and validation functions take plain data in and return plain data out, with no client or framework imports — that's what makes them cheap to unit-test.

### Go — same hexagonal convention
- **`cmd/<entrypoint>/main.go`** per driving adapter (HTTP server, worker, scheduler, CLI).
- **`internal/`** holds everything not meant to be imported outside the module. Go enforces this at compile time — lean on it instead of re-deriving access discipline by convention.
- Package `internal/` by what a module *does* (`internal/logic`, `internal/store`, `internal/config`), not by technical layer (`internal/models`, `internal/handlers`, a catch-all `internal/services`).
- Define ports as small, consumer-defined interfaces at the point of use ("accept interfaces, return structs"). `type ReportStore interface { Save(ctx context.Context, r Report) error }` is a seam; a twelve-method `Repository` interface is usually a shallow module wearing an interface as a costume.
- The two-adapters rule applies unchanged: if only one concrete implementation will ever exist, keep the concrete type and skip the interface.

### Frontend — split API logic from UI
Calling `fetch()` directly inside a page or component mixes API logic and UI logic in one module — the same shallow-seam problem, in TypeScript. Avoid it in new frontend work:

- Give API calls their own module behind a narrow interface — one file per backend resource (e.g. `src/lib/api/reports.ts` exporting `getReport(params): Promise<Report>`), consumed via a hook (`useReport()`) or an event handler. A raw `fetch(` inside a `.tsx` file is a smell on sight.
- This yields two real adapters almost for free: the real `fetch`-backed implementation, and a fake for component tests.
- Pick one pattern (a thin `ApiClient` class, or plain exported functions per resource) and apply it consistently.
- Shape API responses into domain terms inside the API module, not in JSX. A component's props should already speak the domain vocabulary, not raw wire-format JSON.

### Testing
[`engineering/testing`](../testing/SKILL.md) decides unit vs. integration vs. functional vs. e2e; this skill adds the design angle: **depth determines what's worth testing.** A deep module's narrow interface is cheap to test thoroughly and stays valid across refactors. A shallow module resists good tests — a signal to deepen it, not to write more mocks.

- **Python**: unit-test pure functions in `internal/logic/` directly, no mocking. Integration-test data-access queries against a real test database/emulator rather than asserting on query strings. Don't unit-test the config adapter by mocking `os.environ` everywhere — trust it, or replace it wholesale in an integration test.
- **Go**: table-driven tests (`[]struct{ name string; in X; want Y }`); `net/http/httptest` as the standard fake for HTTP ports.
- **Frontend**: once API logic is split out, component tests exercise the UI through its props, not through fetch internals.

### Function design — single-purpose and clean
One job per function, named for that job: takes plain inputs, returns a plain output, no side effects where avoidable.

- A function doing two things ("fetch and format," "validate and save") is a signal to split it at the "and."
- The deletion test applies at function granularity too: if inlining a function at its one call site would concentrate logic, it was pulling its weight; if it existed only to shorten a long function, inlining it back is fine.

### Logging
Every service boundary — API entrypoint, CLI entrypoint, background job — gets structured logging from the start.

- **Python**: one `logger = logging.getLogger("<component-name>")` per module, configured once centrally (timestamp, level, logger name, `file:line`). Never bare `print()`.
- **Go**: standard library `log/slog` for structured key-value logging.
- Log at seams, not inside pure functions: entrypoints log errors with context before responding; core logic logs around expensive or fallible steps (external calls, queries). A pure function that logs is no longer pure.
- Never log request/response payloads wholesale in production. Log identifiers and outcomes — not PII or full prompt/response bodies.

## Using this vocabulary in review
- Name the module's depth before proposing a change to it — shallow modules get collapsed or absorbed, deep modules get protected.
- When proposing a seam, name both adapters it needs to justify itself, not just the first one.
- When proposing a deepening, describe the win in terms of **locality** and **leverage** ("bugs concentrate in one module," "one interface, N call sites"), not generic terms like "cleaner" or "easier to maintain" — those don't carry information.
- When writing new code rather than reviewing existing code, hold it to the matching stack section above from the start, rather than deferring cleanliness, testing, or logging to a later pass.
