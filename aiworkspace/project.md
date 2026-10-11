---
type: resource
name: project-config
title: Project Conventions
description: This repository's stack, tooling, context files, and project-specific directives. Written by productivity/setup and kept current as conventions change. AGENTS.md Directives #3–#5 read it.
tags: [resource, config, conventions]
timestamp: 2026-10-11T00:00:00+02:00
---

# Project Conventions

_Filled in by `productivity/setup`. Until then, values read `unset`/`pending`. For any unset value, agents infer it from the repo, confirm it with the user, and record it here (AGENTS.md Directive #5)._

## Project

- **Name**: unset
- **Purpose**: unset

## Stack & Tooling

| Concern | Value |
| :--- | :--- |
| Languages / frameworks | unset |
| Package manager(s) | unset |
| Install command | unset |
| Build command | unset |
| Lint / format command | unset |
| Test command(s) | unset |
| Test runner(s) | unset |

## Context Files

| File | Status | Written by |
| :--- | :--- | :--- |
| **Codebase map** | pending | `engineering/codebase-map` (`pending` / `declined` / `codebase-map.md`) |
| **Brand** | pending | `design/brand-onboarding` (`pending` / `template-defaults` / `custom` → `brand/`) |
| **Persona** | pending | `productivity/persona` (`pending` / `declined` / `soul.md`) |

## Code Comments

- **Comment policy**: unset _(`follow-existing: <scheme>` / `add: <scheme>` / `minimal` / `none`)_

## Git Workflow

- **Commit policy**: unset _(`auto` — `productivity/process` commits each completed task automatically, no confirmation needed / `ask` — it proposes the commit and waits for a yes before running it / `manual` — it never runs `git commit`, only notes the change is ready with a suggested message)_. Asked once, the first time it matters, by `productivity/setup` or `productivity/process`; change it any time by editing this value.

## Project-Specific Directives

_Rules that apply to every workspace in this repo, with the same force as `AGENTS.md`. Example: "Use pnpm, never npm or yarn." Leave empty if none._

- _none yet_
