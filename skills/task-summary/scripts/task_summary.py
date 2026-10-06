"""Summarize open tasks from a Markdown task list.

Reads notes/tasks.md (or the path you pass) and prints a JSON summary:
open task count, overdue tasks, tasks due soon, and open tasks by priority.
The script only reads the file. It never changes it.

Usage:
    python3 skills/task-summary/scripts/task_summary.py
    python3 skills/task-summary/scripts/task_summary.py notes/tasks.md --today 2026-10-27
"""

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

parser = argparse.ArgumentParser(description="Summarize open tasks as JSON.")
parser.add_argument("tasks_file", nargs="?", default="notes/tasks.md",
                    help="Path to the task list (default: notes/tasks.md)")
parser.add_argument("--today", help="Date to treat as today, YYYY-MM-DD (default: the real date)")
parser.add_argument("--days", type=int, default=7,
                    help="How many days ahead count as due soon (default: 7)")
args = parser.parse_args()

today = date.fromisoformat(args.today) if args.today else date.today()
soon_cutoff = today + timedelta(days=args.days)

path = Path(args.tasks_file)
if not path.exists():
    print(f"Task file not found: {path}", file=sys.stderr)
    sys.exit(1)

# A task line looks like:
#   - [ ] Send Q4 budget draft #work [due: 2026-10-24] [priority: high]
task_line = re.compile(r"^\s*- \[( |x|X)\] (.+)$")
due_field = re.compile(r"\[due:\s*(\d{4}-\d{2}-\d{2})\]")
priority_field = re.compile(r"\[priority:\s*(high|medium|low)\]", re.IGNORECASE)
tag_field = re.compile(r"(?<!\S)#([\w-]+)")

open_tasks = []
section = ""
for line in path.read_text(encoding="utf-8").splitlines():
    if line.startswith("## "):
        section = line[3:].strip()
        continue

    match = task_line.match(line)
    if not match or match.group(1).lower() == "x":
        continue

    body = match.group(2)
    due = due_field.search(body)
    priority = priority_field.search(body)
    tags = tag_field.findall(body)

    # Strip the fields and tags to leave the plain task text.
    text = due_field.sub("", body)
    text = priority_field.sub("", text)
    text = tag_field.sub("", text)
    text = " ".join(text.split())

    open_tasks.append({
        "task": text,
        "due": due.group(1) if due else None,
        "priority": priority.group(1).lower() if priority else None,
        "tags": tags,
        "section": section,
    })

# Overdue: due before today. Due soon: due today or within the next --days days.
dated = sorted((t for t in open_tasks if t["due"]), key=lambda t: (t["due"], t["task"]))
overdue = [t for t in dated if date.fromisoformat(t["due"]) < today]
due_soon = [t for t in dated if today <= date.fromisoformat(t["due"]) <= soon_cutoff]

by_priority = {"high": 0, "medium": 0, "low": 0, "none": 0}
for t in open_tasks:
    by_priority[t["priority"] or "none"] += 1

summary = {
    "generated_at": today.isoformat(),
    "open_count": len(open_tasks),
    "overdue": overdue,
    "due_soon": due_soon,
    "by_priority": by_priority,
}
print(json.dumps(summary, indent=2))
