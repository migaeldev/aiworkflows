---
type: skill
name: setup
title: Setup (Repository Onboarding)
description: One-time bootstrap after the aiworkspace harness files are copied into a repository — detect the stack, record host_mode and project conventions, map the codebase (with permission), onboard the brand (or use template defaults), create the project persona (soul.md), then scaffold the first workspace via new-workspace. Use when aiworkspace/host.md reads host_mode unset, or the user asks to set up/onboard aiworkspace here.
tags: [skill, productivity, setup, onboarding, host-mode]
timestamp: 2026-10-11T00:00:00+02:00
---

# Setup (Repository Onboarding)

## Trigger
Use once per repository, after the harness files (`aiworkspace/`, `AGENTS.md`, `CLAUDE.md`) are on disk and `aiworkspace/host.md` reads `host_mode: unset`. It isn't re-run routinely. Each later concern has its own skill: re-map with `/map`, rebrand with `/brand`, change the persona with `/persona`.

Tell the user up front what the steps are and that each optional one can be skipped.

## Process

1. **Detect host context** (top level only, no deep reading yet), looking for:
   - manifests and lockfiles: `package.json` + `pnpm-lock.yaml`/`yarn.lock`/`package-lock.json`/`bun.lockb`, `pyproject.toml`/`requirements.txt`/`uv.lock`/`poetry.lock`, `go.mod`, `Cargo.toml`, `pom.xml`/`build.gradle`, …
   - CI config: `.github/workflows/`, `.gitlab-ci.yml`, …
   - an existing `apps/` folder or monorepo tooling: `pnpm-workspace.yaml`, `turbo.json`, `nx.json`
   - existing agent files: `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, …
2. **Propose a `host_mode`**, don't assume it:
   - `monorepo` — the repo is new/empty, or already organized as `apps/<name>/`.
   - `bolt-on` — an existing codebase with its own structure.
   - Confirm with the user either way (`AGENTS.md` Directive #1), then record it in `aiworkspace/host.md` in place of `unset`.
3. **Fill in `aiworkspace/project.md` — Project, Stack & Tooling, and Directives.** Propose values from step 1: name, purpose, languages, package manager, install/build/lint/test commands. Confirm them with the user and write them in. Ask about project-wide rules (e.g. "pnpm only", "no new dependencies without approval") and list them under Project-Specific Directives. Carry over relevant rules from any pre-existing agent files.
4. **Codebase map (asks permission)** — run [`engineering/codebase-map`](../../engineering/codebase-map/SKILL.md). It asks permission before reading anything, writes `aiworkspace/codebase-map.md`, settles the **Comment policy** (asking the user when the code has no consistent comment scheme), and fills any Stack & Tooling rows still unset. If the user declines, it records `declined` and setup continues.
5. **Brand** — run [`design/brand-onboarding`](../../design/brand-onboarding/SKILL.md). It asks whether to onboard the brand now. If yes, it detects existing tokens, runs a grill-me interview on brand and UI technology, and writes the `aiworkspace/brand/` folder: `brand.md`, plus any logos, fonts, tokens, docs, and reference artifacts. If no, it records `template-defaults`. If "not now", it leaves `pending`, and the question comes back at the first UI task. If the project has no UI at all, record `template-defaults` and move on.
6. **Project persona** — run [`productivity/persona`](../persona/SKILL.md) at **project** scope to create `aiworkspace/soul.md`. It's built from the codebase map, `project.md`, and `brand/brand.md`, with grill-me filling the gaps. If the user skips it, set **Persona** in `project.md` to `declined`.
7. **Merge agent instructions** — if the repo already had its own `CLAUDE.md`/`AGENTS.md` before the harness was copied in, make sure it points at the harness `AGENTS.md` rather than being overwritten, and that the two don't contradict each other. Surface any conflicts to the user, and only edit those files with their approval.
8. **Workspaces interview** — invoke [`productivity/grill-me`](../grill-me/SKILL.md) to learn whether one or several domain workspaces are expected now. **In `bolt-on` mode**, also learn where different kinds of production code should land. The codebase map's Change Recipes and Module Map make good proposals. This seeds the first workspace's Production Target Map.
9. **Scaffold the first workspace by delegating to [`productivity/new-workspace`](../new-workspace/SKILL.md)**. Don't duplicate its logic here.
10. **Present & gate** — show everything written (`host.md`, `project.md`, `codebase-map.md`, `brand/`, `soul.md`, the new workspace) and anything skipped. Wait for explicit confirmation before any Step 0/1 work begins.

## Notes
- Getting the harness files into the repo is a separate step: a manual copy for now (see the planned installer in the root `README.md` roadmap).
- This skill and the skills it delegates to write only inside `aiworkspace/`, plus the agent-instruction merge in step 7 with the user's approval. Never write to `apps/` or other production code from here.
