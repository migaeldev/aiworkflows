# The lifecycle

```text
[0: define] ──> [1: plan] ──> [2: resources/] ──> [3: processing/] ──> [4: finalized/] ──> [5: promote] ──> [production]
 workspace core   feature/tasks   input context      active iteration     audited & gated     human-only
```

| Step | Command | What happens |
| :--- | :--- | :--- |
| — | `/map` | Create or refresh the codebase map (`codebase-map.md`) |
| — | `/brand` | Onboard or change the brand (`brand/`), or choose template defaults |
| — | `/persona` | Create or change the project or a workspace persona (`soul.md`) |
| 0 | `/define` | Create a workspace and define its core (`definition.md`). Alias `/spec` |
| 1 | `/plan` | Plan a feature/change as an ordered task list (defines the workspace first if needed) |
| 2 | `/resources` | Collect the context, schemas, and data the plan calls for |
| 3 | `/process` | Work through the plan's tasks inside `processing/`, one round at a time; `/process auto` runs all remaining tasks in one approved pass |
| 4 | `/finalize` | Security audit, API spec (if applicable), docs, tests, dual-axis code review |
| 5 | `/promote` | Human-authorized copy to production |

Full specification: [`aiworkspace/README.md`](../aiworkspace/README.md).
