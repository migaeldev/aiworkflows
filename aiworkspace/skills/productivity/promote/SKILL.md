---
type: skill
name: promote
title: Promote (Step 4)
description: Human-authorized deployment of audited finalized/ content to production. Use only when the human explicitly requests promotion.
tags: [skill, productivity, lifecycle, step-4]
timestamp: 2026-10-04T00:00:00+02:00
---

# Promote (Step 4)

## Trigger
Use only when explicitly requested by the human. Never self-trigger — `AGENTS.md` Directive #7 requires explicit human instruction for this transition, and Directive #6 makes `apps/[workspace]` AI-read-only outside of this step.

## Process (current: monorepo mode only)
1. **Copy** audited content from `finalized/` into `apps/<workspace>/`, verbatim.
2. **Populate** `apps/<workspace>/README.md` as a standalone production guide: full developer setup, environment variable tables, and the `.env.template` embedded inline as a copyable code block.
3. **Update the root `README.md`** — add or update the application entry in the directory tree and navigation table.
4. **Update `aiworkspace/index.md`** to point at `apps/<workspace>/` as the canonical production location.
5. **Clean up** — clear temporary files in `resources/` and `processing/` for this workspace.

## Pending (not yet available)
Host-mode-aware promotion — resolving to either `apps/<workspace>/` (monorepo) or a per-file Production Target Map (bolt-on repos with no `apps/` folder) — is planned in `workflow-improvements-planning-claude.md` §7 (Change 5) but not yet built. Until that lands, this skill only supports the monorepo pattern above; if a workspace has no `apps/<workspace>/` target, stop and ask rather than guessing a destination.

## Notes
- This is the only skill permitted to write to `apps/[workspace]`.
