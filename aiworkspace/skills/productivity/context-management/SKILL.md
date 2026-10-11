---
type: skill
name: context-management
title: Context Management
description: Manage AI agent context and session memory effectively. Use during long sessions, multi-step tasks, or when responses start degrading. Covers context resets, checklists, and subagents.
tags: [skill, productivity, context, memory, workflow]
timestamp: 2026-09-09T14:02:14+02:00
---

# Context Management Skill

## Trigger
Use during long sessions, multi-step tasks, or when the agent's responses start degrading in quality or consistency.

## The Insight
Best practice: "Regularly reset context between tasks to prevent irrelevant conversation and file contents from degrading performance."

## Why Context Matters
- LLMs have limited effective context windows
- Old, irrelevant content crowds out useful information
- Accumulated context from failed approaches confuses new attempts
- Fresh context = better, more accurate responses

## Techniques

### 1. Reset Context Between Tasks
After completing a task, before starting an unrelated new one, clear or reset the agent session memory.

This resets the conversation while retaining:
- Core `AGENTS.md` directives and instructions
- Project domain configuration
- Tool permissions

**When to reset context:**
- Switching to an unrelated task
- After a complex debugging session
- When responses feel "confused" or repetitive
- Before starting important production implementations

### 2. Checklists for Large Tasks
For migrations, bulk fixes, or multi-file changes:

```markdown
## Migration Checklist

### Completed
- [x] Update User model
- [x] Update User service
- [x] Update User controller

### In Progress
- [ ] Update User tests ← CURRENT

### Remaining
- [ ] Update API documentation
- [ ] Update client SDK
- [ ] Run full test suite
```

Have the agent maintain this checklist:
- Update after each step
- Verify completion before proceeding
- Track what's done vs remaining

### 3. Course Correction Tools

**Interrupt generation early:**
- Interrupt generation as soon as you notice the agent going down a wrong path.

**Request undo / rollback:**
```markdown
Undo the last change to user-service.ts
```

### 4. Subagents for Investigation
Early in complex tasks, use subagents to investigate details:

```markdown
Use a subagent to research how error handling is done in this codebase.
Report back the patterns found.
```

Benefits:
- Preserves main conversation context
- Subagent performs deep investigation in an isolated context
- Main context receives clean, summarized findings

### 5. Explicit Context Boundaries
Tell the agent explicitly what's relevant and what isn't:

```markdown
Forget about the authentication changes we discussed earlier.
Focus only on the new payment integration.
The relevant files are:
- src/payments/
- src/api/checkout.ts
```

## Signs You Need to Manage Context

| Symptom | Solution |
| :--- | :--- |
| Agent references old, abandoned approaches | Reset context / clear session memory |
| Responses getting slower or repetitive | Reset context or reduce file reads |
| Agent confused about current state | Summarize current state explicitly |
| Repeating the same mistakes | Clear and re-explain requirements |
| Losing track of multi-step task | Use a checklist |

## Checklist Template for Large Tasks

```markdown
## Task: [Migration/Refactor/Bulk Fix Name]

### Overview
[Brief description of the full task]

### Progress Tracking

#### Phase 1: [Name]
- [ ] Step 1.1
- [ ] Step 1.2
- [ ] Step 1.3

#### Phase 2: [Name]
- [ ] Step 2.1
- [ ] Step 2.2

#### Phase 3: [Name]
- [ ] Step 3.1
- [ ] Step 3.2

### Current Focus
[Which item is being worked on NOW]

### Blocked Items
[Items waiting on something]

### Verification
- [ ] All tests pass
- [ ] Manual verification complete
- [ ] Ready for review
```

## Anti-Patterns

**Don't:**
- Keep adding to context indefinitely
- Assume the agent remembers everything from 50 messages ago
- Debug the same issue repeatedly without clearing
- Mix multiple unrelated tasks in one session

**Do:**
- Clear or reset memory between distinct tasks
- Summarize context when resuming
- Use checklists for tracking
- Interrupt early when going off track
