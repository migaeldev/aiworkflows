---
type: resource
name: host-config
title: Host Configuration
description: Records how aiworkspace is installed in this repository — monorepo (production code lives in sibling apps/<workspace>/ folders) or bolt-on (aiworkspace was added into an existing codebase; production destinations are mapped per-workspace via each index.md's Production Target Map). Written by productivity/setup.
tags: [resource, host-mode, config]
timestamp: 2026-10-11T00:00:00+02:00
---

# Host Configuration

host_mode: unset

## Values

- `unset` — the harness has not been initialized. Run `productivity/setup` before any lifecycle work.
- `monorepo` — production code for each workspace lives in `apps/<workspace>/`.
- `bolt-on` — the harness was added into an existing codebase. Everything outside `aiworkspace/` is read-only for AI except via each workspace's Production Target Map.

## Notes

`productivity/setup` writes this value after confirming it with the user. `AGENTS.md` Directive #6 and `productivity/promote` both read it.
