---
type: resource
name: host-config
title: Host Configuration
description: Records how aiworkspace is installed in this repository — monorepo (production code lives in sibling apps/<workspace>/ folders) or bolt-on (aiworkspace was added into an existing codebase with no apps/ folder; production is the repo root, mapped per-workspace via each index.md's Production Target Map).
tags: [resource, host-mode, config]
timestamp: 2026-10-04T00:00:00+02:00
---

# Host Configuration

host_mode: monorepo

## Notes
This repository is the origin of the aiworkspace pattern itself — production code for each domain lives in its own `apps/<workspace>/` folder, as described throughout `AGENTS.md`, `CLAUDE.md`, and `aiworkspace/README.md`. `AGENTS.md` Directive #6 branches on this value; absent this file, agents default to `monorepo` behavior.

This file is read by `productivity/setup` (when bolting `aiworkspace` onto a different repo) and by `productivity/promote` (to decide whether to copy to `apps/<workspace>/` or to a workspace's Production Target Map).
