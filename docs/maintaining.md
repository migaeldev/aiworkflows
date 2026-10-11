# Maintaining the harness

The "Slash Commands & Aliases" table in [`aiworkspace/README.md`](../aiworkspace/README.md) is the single source of truth for commands. The Claude Code adapters in `.claude/skills/` are generated from it, so never edit them by hand:

```bash
python tools/gen_claude_adapters.py          # regenerate after editing the table or a skill description
python -m unittest discover tools/tests      # tests for the tools themselves
```

Adapter behavior:
- Primary commands carry the canonical skill's description, so Claude can also pick them up from plain-language requests.
- Aliases, `/finalize`, and `/promote` set `disable-model-invocation: true`. Only a human typing the command runs them (Directive #7).
- `/plan` intentionally replaces Claude Code's built-in plan-mode command in the terminal. Plan mode is still available with Shift+Tab.
