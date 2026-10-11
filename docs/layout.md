# Layout

```text
.
├── AGENTS.md                     # Agent-agnostic operating rules (source of truth)
├── CLAUDE.md                     # Claude Code pointer to AGENTS.md
├── .claude/skills/               # Generated Claude Code slash-command adapters (/plan, /spec, …)
├── docs/                         # This documentation
├── tools/                        # Harness maintenance scripts (not copied into host repos)
└── aiworkspace/
    ├── README.md                 # Architecture, lifecycle & slash-command spec
    ├── index.md                  # Registry of workspaces & skills (filled as you go)
    ├── host.md                   # host_mode — written by setup
    ├── project.md                # Project conventions — written by setup
    ├── codebase-map.md           # Where/how to change code — setup, with permission
    ├── brand/                    # Brand values, logos, fonts, tokens, docs & references — /brand (optional)
    ├── soul.md                   # Project persona — /persona
    ├── scripts/                  # Shipped helper scripts (agent_pointers.py)
    ├── skills/                   # design / engineering / productivity / security
    └── workspaces/
        └── template-workspace/   # Boilerplate copied by /define
```
