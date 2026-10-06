# Building Self-Hosted Personal AI Agents with OpenClaw

Companion repository for my ODSC AI West 2026 session. The talk covers how agent harnesses work, how to design the workspace that defines your agent, and how to turn repeated requests into skills and scheduled runs.

## What's here

| Path | What it holds |
|---|---|
| `workspaces/personal-assistant/` | The assistant from the demos: instruction files, memory, notes with projects, trackers, dailies and weekly reviews, and the `rental-search` skill |
| `workspaces/scratch/` | A near-empty workspace for the scratch agent, with starter files for you to fill in |
| `multi-agent/` | How to add the scratch agent next to your assistant, each with its own Telegram bot |
| `automations/` | The daily rental-search run from the talk |
| `skills/task-summary/` | A small skill with a script, for the take-home exercises |
| `exercises.md` | The take-home exercises |
| `examples/other-harnesses/` | One workspace shared with Claude Code or Codex |
| `setup_check.py` | Checks that Python and the task-summary script work on your machine |

## Demos by slide

| Slide | Demo | Files |
|---|---|---|
| Loading the Workspace into Context | A message to the assistant, then `/context list` | [`workspaces/personal-assistant/`](workspaces/personal-assistant/) |
| A Workspace Walkthrough | Live edits to the scratch agent, then a tour of the assistant's workspace | [`workspaces/scratch/`](workspaces/scratch/), [`multi-agent/`](multi-agent/) |
| The Rental Search Skill | A rental request in Telegram, the script's results and new rows in the shortlist | [`skills/rental-search/`](workspaces/personal-assistant/skills/rental-search/), [`notes/trackers/rentals.md`](workspaces/personal-assistant/notes/trackers/rentals.md) |
| Scheduled Runs | The daily rental search, with new listings in Telegram | [`automations/rental-search-daily.md`](automations/rental-search-daily.md) |

## Requirements

- OpenClaw, which is free and open source. The commands here follow OpenClaw 2026.9.5.
- A machine that stays on, if you want the agent to reach you while your laptop is closed. A small VPS, a mini PC or a spare laptop all work. Your own laptop is fine for trying it out.
- A model: an existing Claude Code or Codex login, or an API key from a model provider. Model usage costs money.
- A Telegram account, and two bot tokens from Telegram's @BotFather: one for the assistant, one for the scratch agent.
- Python 3.9 or newer, for the skill scripts.

## Setup

1. **Install OpenClaw** and go through onboarding. On macOS or Linux:

   ```bash
   npx openclaw@latest
   ```

   The [getting started guide](https://docs.openclaw.ai/start/getting-started) covers other install options. For a VPS with Docker, follow the [deployment guide from my O'Reilly course](https://github.com/sajal2692/openclaw-oreilly-live-course/blob/main/deployment/linux-vps-guide.md), and run the `openclaw` commands below inside the gateway container.

2. **Check Python and the sample skill:**

   ```bash
   git clone https://github.com/sajal2692/odsc-west-2026-openclaw.git
   cd odsc-west-2026-openclaw
   python3 setup_check.py
   ```

3. **Connect Telegram.** Add your assistant's bot, send it a message, then approve the pairing request:

   ```bash
   openclaw channels add --channel telegram --token <BOT_TOKEN>
   openclaw pairing list telegram
   openclaw pairing approve telegram <CODE>
   ```

4. **Copy the assistant's workspace in.** OpenClaw keeps the first agent's workspace in `~/.openclaw/workspace`. If you already have one, back it up first.

   ```bash
   cp -R ~/.openclaw/workspace ~/.openclaw/workspace.backup
   cp -R workspaces/personal-assistant/. ~/.openclaw/workspace/
   ```

5. **Put your own details in.** In `USER.md`, change the name, timezone and goals to yours. In `AGENTS.md`, set the timezone in the Local environment list and replace every `<YOUR_CHAT_ID>` with your numeric Telegram chat ID. To find it, send your bot a message while `openclaw logs --follow` is running.

6. **Add the scratch agent** by following [multi-agent/README.md](multi-agent/README.md).

Then work through [exercises.md](exercises.md).

## More

- [Building Integrated AI Agents with OpenClaw](https://github.com/sajal2692/openclaw-oreilly-live-course), my O'Reilly live course, goes deeper on deployment, security and multi-agent setups.
- [OpenClaw](https://github.com/openclaw/openclaw) and its [documentation](https://docs.openclaw.ai).
