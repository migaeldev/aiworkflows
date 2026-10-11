---
type: skill
name: codebase-map
title: Codebase Map
description: With the user's explicit permission, read the host codebase (read-only) and write aiworkspace/codebase-map.md — languages, frameworks, folder structure, recognized design patterns, conventions, comment scheme, testing, entry points, and change recipes saying where and how to make each kind of change. Every claim cites a file path. Use during productivity/setup, when the map is missing or stale, or when the user asks to map or re-map the codebase.
tags: [skill, engineering, onboarding, context, architecture, conventions]
timestamp: 2026-10-11T00:00:00+02:00
---

# Codebase Map

## Purpose
`aiworkspace/codebase-map.md` is the agent's working memory of the host system: **where** a change belongs and **how** to write it so it matches what's already there. Agents consult it before planning or writing code (`AGENTS.md` Directive #5), and `productivity/persona` builds the project's coding persona from it.

It is **descriptive** — what the code *does* today. `project.md` is **normative** — what the project has *decided*. If the two conflict, `project.md` wins; flag the conflict to the user.

## Trigger
- `productivity/setup` (its codebase-map step).
- `codebase-map.md` is missing while **Codebase map** in `project.md` is `pending`.
- The map looks stale — its `mapped_at_commit` is far behind `HEAD`, or the code contradicts it.
- `/map` (alias `/remap`), or the user asks to map, re-map, or update the map.

## Step 1 — Ask for authorization (always)
Never read the codebase for mapping without explicit permission, even inside `setup`. An explicit `/map` (or "map the codebase") request counts as permission. Confirm the scope and exclusions in one line, then proceed. If an earlier map exists, `/map` updates it in place (see Keeping it current). In every other case, ask:

> "May I read through the codebase (read-only) to build `aiworkspace/codebase-map.md`? I'll record languages, frameworks, folder structure, design patterns, conventions, and where different kinds of changes belong. I won't open `.env`/secret files or dependency/build folders, and I won't modify anything outside `aiworkspace/`."

| Answer | Action |
| :--- | :--- |
| **Yes** | Map the whole repo, minus the exclusions below. |
| **Yes, but only certain paths** | Map those paths. Record the scope in the map's frontmatter. |
| **No** | Set **Codebase map** in `project.md` to `declined`. Stop. Don't ask again unless the user brings it up. |

**Always excluded**: `.git/`, dependency folders (`node_modules/`, `.venv/`, `vendor/`, …), build output (`dist/`, `build/`, `.next/`, `target/`, …), `aiworkspace/` itself, and any secret-bearing file (`.env*` except `.env.example`/`.env.template`, key/cert files, credentials JSON). Never copy a secret value into the map.

If the repo is empty or has no source code yet (typical for a fresh `monorepo`), say so. Write a minimal map that just records "greenfield", and stop.

## Step 2 — Survey
Work from the outside in, citing paths as you go:
1. **Manifests, lockfiles, CI, Docker/deploy config** → languages, versions, frameworks, package managers, real build/test/lint commands.
2. **Top-level tree (2–3 levels)** → folder structure and what each folder is for.
3. **Entry points** → servers, CLIs, jobs, workers, UI apps, and their startup files.
4. **Representative files from each major area** (aim for 2–3 per area, not everything) → patterns and conventions.
5. **Tests** → frameworks, locations, naming, fixtures/factories, how external services are faked.

For a large repo, sample. Record which areas you covered and which you didn't, so the map never implies more coverage than it has.

## Step 3 — Recognize patterns and conventions
Name only what the code shows, each with evidence (`path:line` or a file list). For each one, say whether it's consistent or only partial:
- **Architecture & design patterns**: layered/MVC, hexagonal/ports-and-adapters, clean architecture, feature-sliced, monorepo packages; repository, service, factory, strategy, observer, dependency injection, CQRS/event sourcing, middleware pipelines, hooks/context (frontend), etc.
- **Naming**: files, directories, classes, functions, variables, constants, tests.
- **Code style**: formatter/linter config, import ordering, module boundaries, error handling, logging, configuration/env access.
- **Comment & documentation scheme**: docstring style (Google/NumPy/reST, JSDoc/TSDoc, GoDoc, …), file headers, inline-comment density, TODO conventions, README-per-module.

## Step 4 — Comment policy
- **A consistent scheme exists**: record it in the map, and set **Comment policy** in `project.md` to `follow-existing: <scheme>`.
- **No (or no consistent) scheme**: ask the user, and record the answer as **Comment policy** in `project.md`:
  - `add: <scheme>` — add comments in a proposed scheme (suggest the language's standard, e.g. Google-style docstrings, TSDoc) to code the agent writes or touches;
  - `minimal` — only where logic is non-obvious;
  - `none` — don't add comments.

## Step 5 — Write `aiworkspace/codebase-map.md`
Use the template below. Mark every claim as an observation with evidence, or as `unknown`. Never guess (Directive #2). Put anything you couldn't settle under Open Questions and ask the user about it.

Then set **Codebase map** in `project.md` to `codebase-map.md`. Fill any `project.md` Stack & Tooling rows that are still `unset` with what you found, once the user confirms them.

## Step 6 — Present & gate
Summarize the map: stack, structure, top patterns, the change recipes, and the open questions. Wait for the user to confirm or correct it. Corrections go straight into the map.

## Keeping it current
- When work in `processing/` introduces a new pattern, area, or entry point, propose an update to the relevant section at `finalize` time.
- When re-mapping, update the existing file in place and bump `mapped_at_commit`/`timestamp`. Keep the user's earlier corrections.

---

## `codebase-map.md` template

```markdown
---
type: resource
name: codebase-map
title: Codebase Map
description: Descriptive map of the host codebase — stack, structure, patterns, conventions, and change recipes. Written by engineering/codebase-map.
status: finalized
scope: whole repo | <paths>
mapped_at_commit: <git sha or "no git">
tags: [resource, context, architecture]
timestamp: <ISO-8601>
---

# Codebase Map

## Overview
What the system does, who uses it, main moving parts — 3–5 sentences.

## Languages, Frameworks & Tooling
| Area | Technology (version) | Evidence |
| :--- | :--- | :--- |

## Folder Structure
(annotated tree, 2–3 levels — purpose of each folder)

## Entry Points
| Entry point | Kind (API/CLI/job/UI/…) | File | How it's started |
| :--- | :--- | :--- | :--- |

## Module Map
| Module / area | Responsibility | Key files | Depends on |
| :--- | :--- | :--- | :--- |

## Architecture & Design Patterns
- **<Pattern>** — where and how it's used (`evidence`), consistent / partial.

## Conventions
- **Naming**: …
- **Formatting & linting**: …
- **Error handling**: …
- **Logging**: …
- **Configuration & env**: …
- **Imports / module boundaries**: …

## Comment & Documentation Scheme
Observed scheme with example (`path:line`), or "none observed — policy: see project.md".

## Testing
Frameworks, locations, naming, fixtures, how externals are faked, how to run.

## Data & Integrations
Databases, queues, external APIs/SDKs, auth providers, and where each client lives.

## Build, CI & Deploy
…

## Change Recipes
How to make each common kind of change *in this codebase*. Each recipe says which files to touch and which existing example to copy:
- **Add an API endpoint**: …
- **Add a UI page/component**: …
- **Add a data model / migration**: …
- **Add a background job / CLI command**: …
- **Add a test**: …

## Hotspots & Caveats
Generated code, vendored code, fragile areas, known tech debt, files that must not be hand-edited.

## Coverage & Open Questions
- Covered: …
- Not covered: …
- Open questions: …
```

## Notes
- Read-only toward the host codebase. Writes only `aiworkspace/codebase-map.md` and the **Codebase map**, **Comment policy**, and (with confirmation) Stack & Tooling lines in `project.md`.
