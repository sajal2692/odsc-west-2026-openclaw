---
name: task-summary
description: Summarize the user's open tasks from notes/tasks.md, including overdue tasks, tasks due in the next week, and open tasks by priority. Use when the user asks what is on their plate, what is overdue, what is due soon, for a task summary, or for a morning planning check.
---

# Task Summary

Read-only summary of the task list in the workspace. A Python script parses the list and returns structured JSON; you turn that JSON into a short reply.

## Configuration

- **Script**: `skills/task-summary/scripts/task_summary.py`
- **Task list**: `notes/tasks.md`

### Task Format

```markdown
- [ ] Send Q4 budget draft to finance #work [due: 2026-10-24] [priority: high]
- [x] Pay the electricity bill #home [due: 2026-10-20]
```

Due date and priority are optional. Done tasks (`- [x]`) are ignored.

## Workflow

### Step 1: Run the script

From the workspace root:

```bash
python3 "skills/task-summary/scripts/task_summary.py" "notes/tasks.md"
```

Optional arguments:

| Argument | Default | Notes |
|---|---|---|
| `--days` | 7 | How many days ahead count as due soon |
| `--today` | the real date | Treat another date as today, YYYY-MM-DD. Use only when the user asks about a specific date. |

The script prints JSON to stdout:

```json
{
  "generated_at": "2026-10-27",
  "open_count": 9,
  "overdue": [{"task": "...", "due": "2026-10-24", "priority": "high", "tags": ["work"], "section": "This Week"}],
  "due_soon": [...],
  "by_priority": {"high": 3, "medium": 3, "low": 2, "none": 1}
}
```

The script never edits `notes/tasks.md`. If the user asks to change a task, edit the file directly after confirming the change.

### Step 2: Present the summary

Base the reply on the JSON only. Do not invent tasks or dates.

```
{open_count} open tasks.

Overdue:
- {task} (due {due})

Due in the next {days} days:
- {task} (due {due})
```

- List overdue tasks first, high priority before others.
- Skip a heading when its list is empty.
- If nothing is overdue or due soon, say so in one line.

## Scheduling

This skill works as a scheduled run. A morning automation can run it and send the summary to the user's messaging channel.
