# Planning Stage (Step 1)

This folder stores Step 1 planning artifacts: feature/change plans, research notes, and (for large/ambiguous work) a file-native decision map, all produced by the `productivity/plan` skill before `resources/` work begins. The workspace's core definition (Step 0) lives one level up in `definition.md`.

- **Status**: Pre-`resources/` planning and research.
- **Workflow**: `productivity/plan` checks each ask against `definition.md`, always runs `grill-me`, and loads `goal-driven` only if the user opts in.
- **Contents**:
  - `features/<slug>/plan.md`: one per feature/change, with an ordered **Tasks** checklist (ticked off by `/process`) and a **Resources Needed** list (gathered by `/resources`).
  - `research.md`: optional findings that informed a plan or the definition, with citations.
  - `decisions/<slug>.md`: optional, only for large/ambiguous work; a file-native decision map (`status: open | blocked | resolved`, `blocked_by: [...]`).
