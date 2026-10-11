# Planning Stage (Step 0)

This folder stores Step 0 planning artifacts: the workspace's Project Plan, individual Feature/Change Plans, research notes, and (for large/ambiguous work) a file-native decision map — all produced by the `productivity/plan` skill before `resources/` work begins.

- **Status**: Pre-`resources/` planning and research.
- **Workflow**: `productivity/plan` always runs `grill-me`; `goal-driven` is loaded only if the user opts in. Every plan gets an optional, recommended `## Goal` section first.
- **Contents**:
  - `project-plan.md` — whole-workspace scope, written once at inception (see `productivity/new-workspace`'s Step 3).
  - `features/<slug>/spec.md` — one per feature/change, written every time this stage runs for a new ask.
  - `research.md` — optional findings that informed a plan, with citations.
  - `decisions/<slug>.md` — optional, only for large/ambiguous work; file-native decision map (`status: open | blocked | resolved`, `blocked_by: [...]`).
