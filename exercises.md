# Take-Home Exercises

Shape the scratch agent from the talk into an agent of your own. Each step changes one file, then checks the change in a reply. Work through them in order.

You need a running OpenClaw gateway with the scratch agent added. See [Setup](README.md#setup) and [multi-agent/README.md](multi-agent/README.md). The scratch agent's files are in `~/.openclaw/workspace-scratch`.

After each change, send `/new` to the scratch bot so the next reply starts from the updated files.

## 1. Give it a voice

Fill in `IDENTITY.md`, then add one voice rule to `SOUL.md` with an example of a right reply and a wrong one.

**Check:** ask it something ordinary, such as "What should I focus on today?", and look for the rule in the reply.

## 2. Tell it about you

Fill in `USER.md` with your name, timezone, work and how you like replies. Keep it to stable facts.

**Check:** ask "What do you know about me?" The answer should match the file and nothing more.

## 3. Add a project file and a tracker

- Create `notes/projects/<your-project>.md` with a status line, a goal, decisions with dates, and next actions. `workspaces/personal-assistant/notes/projects/apartment-search.md` is an example.
- Create a tracker in `notes/trackers/`, such as a reading list or job applications, as a table with a Status column.
- Add both to the map in `notes/README.md`.
- Add a write-back rule for each to `AGENTS.md`, for example: "Trackers: edit rows in place, never delete a row."

**Check:** ask the agent to add a row to the tracker, then to record a decision on the project. Open both files and compare them with your rules.

## 4. Add a weekly review template

Create `notes/weekly/_template.md` with the sections you want each week. `workspaces/personal-assistant/notes/weekly/_template.md` is a longer example.

**Check:** ask for this week's review. It should follow your template and draw on your project and tracker.

## 5. Add a skill

Copy the `task-summary` skill and its sample tasks into the scratch workspace:

```bash
mkdir -p ~/.openclaw/workspace-scratch/skills
cp -R skills/task-summary ~/.openclaw/workspace-scratch/skills/
cp skills/task-summary/sample-tasks.md ~/.openclaw/workspace-scratch/notes/tasks.md
```

Read `SKILL.md` to see how the description tells the agent when to use it, and what the script does. Swap in your own tasks when you're ready.

**Check:** ask "What's overdue?" The reply should list tasks from `notes/tasks.md` and nothing invented.

## 6. Schedule it

Turn the skill into a morning automation for the scratch agent. Follow `automations/rental-search-daily.md`, with three changes: add `--agent scratch`, use `--account scratch` for delivery, and change the message to "Use the task-summary skill to summarize my open tasks."

**Check:** create the one-minute test job first, and wait for the summary in Telegram. Then create the daily one, and remove the test job.

## Going further

- Copy the personal-assistant workspace's `rental-search` skill and point it at your own city.
- Use the same workspace with Claude Code or Codex. See [examples/other-harnesses](examples/other-harnesses/).
