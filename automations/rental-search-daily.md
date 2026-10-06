# Daily Rental Search

The scheduled run from the talk. Every morning, the personal assistant runs the `rental-search` skill in a fresh session, adds new listings to `notes/trackers/rentals.md`, and sends the results to Telegram.

Run these where the `openclaw` command can reach your gateway. If OpenClaw runs in Docker, open a shell in the gateway container first:

```bash
docker compose exec openclaw-gateway bash
```

Replace `<YOUR_CHAT_ID>` with your numeric Telegram chat ID. To find it, send your bot a message while `openclaw logs --follow` is running.

## Test it now

A one-time run in one minute:

```bash
openclaw automations create --name "Rental search test" \
  --at 1m --session isolated \
  --message "Use the rental-search skill to check for new listings. Add new ones to notes/trackers/rentals.md and add a line to today's daily note." \
  --announce --channel telegram --account default --to <YOUR_CHAT_ID> \
  --keep-after-run
```

## Schedule it every morning

Every day at 8am Vancouver time:

```bash
openclaw automations create --name "Daily rental search" \
  --cron "0 8 * * *" --tz America/Vancouver \
  --session isolated \
  --message "Use the rental-search skill to check for new listings. Add new ones to notes/trackers/rentals.md and add a line to today's daily note." \
  --announce --channel telegram --account default --to <YOUR_CHAT_ID>
```

- `--session isolated` starts each run in a fresh session, with the workspace files and no chat history.
- `--announce --channel telegram` sends the result to your chat.
- The skill runs a Python script, so the agent needs permission to run `python3`. Scheduled runs can't ask you for approval in Telegram.

## List, inspect and remove

```bash
openclaw automations list --all
openclaw automations get <JOB_ID>
openclaw automations rm <JOB_ID>
```

`openclaw cron` is an older name for the same command and still works.
