---
type: skill
name: promote
title: Promote (Step 5)
description: Human-authorized deployment of audited finalized/ content to production — apps/<workspace>/ in monorepo mode, or the workspace's Production Target Map in bolt-on mode. Use only when the human explicitly requests promotion.
tags: [skill, productivity, lifecycle, step-5, host-mode]
timestamp: 2026-10-11T00:00:00+02:00
---

# Promote (Step 5)

## Trigger
Use only when explicitly requested by the human. Never self-trigger — `AGENTS.md` Directive #7 requires explicit human instruction for this transition, and Directive #6 makes production AI-read-only outside of this step.

## Preconditions
1. Read `host_mode` from `aiworkspace/host.md`. If it is `unset` or missing, stop and run `productivity/setup` first.
2. Confirm `finalized/` has passed Step 4 — `finalized/review.md` exists and `log.md` records the gate results. If not, stop and say what's missing.

## Process — `monorepo`
1. **Copy** audited content from `finalized/` into `apps/<workspace>/`, verbatim.
2. **Populate** `apps/<workspace>/README.md` as a standalone production guide: full developer setup, environment variable tables, and — if the app has one — the `.env.template` embedded inline as a copyable code block.
3. **Update the root `README.md`** — add or update the application entry.

## Process — `bolt-on`
1. **Read the Production Target Map** in the workspace's `index.md`.
2. **Resolve every file** in `finalized/` (excluding harness artifacts such as `review.md`, audit logs, and test reports) to a destination in the map.
3. **If any file has no map entry, stop** — list the unmapped files and ask the human where each goes. Never guess a destination. Add the answers to the map before continuing.
4. **Show the plan** — a `finalized/ path → destination` table, noting which destinations already exist and will be overwritten — and get confirmation.
5. **Copy** each file to its mapped destination, verbatim. Write nowhere else outside `aiworkspace/`.

## Then, both modes
1. **Update `aiworkspace/index.md`** — set this workspace's Production Location (`apps/<workspace>/`, or "host repo — see Target Map").
2. **Log it** — append to the workspace's `log.md`: date, files promoted, destinations.
3. **Clean up** — clear temporary files in this workspace's `resources/` and `processing/`, after confirming with the human which (if any) to keep.

## Notes
- This is the only skill permitted to write to production (`apps/[workspace]` in monorepo mode; Target Map destinations in bolt-on mode).
