# Adding the Scratch Agent

The scratch agent runs next to your personal assistant on the same gateway, with its own workspace and its own Telegram bot. Its starter files in `workspaces/scratch/` are mostly blank, so you can see each change you make show up in its replies.

Run these where the `openclaw` command can reach your gateway. If OpenClaw runs in Docker, open a shell in the gateway container first:

```bash
docker compose exec openclaw-gateway bash
```

1. **Create a second Telegram bot** with @BotFather (`/newbot`), and connect it as a second account:

   ```bash
   openclaw channels add --channel telegram --account scratch --token <SCRATCH_BOT_TOKEN>
   ```

2. **Copy the workspace in, then create the agent and bind it to its bot:**

   ```bash
   mkdir -p ~/.openclaw/workspace-scratch
   cp -R odsc-west-2026-openclaw/workspaces/scratch/. ~/.openclaw/workspace-scratch/
   openclaw agents add scratch --workspace ~/.openclaw/workspace-scratch --bind telegram:scratch --non-interactive
   openclaw config set agents.entries.scratch.heartbeat.every 0m
   ```

   If your first agent already has a Telegram bot, bind it too, so both bots keep working:

   ```bash
   openclaw agents bind --agent main --bind telegram:default
   ```

3. **Keep the agents' conversations apart:**

   ```bash
   openclaw config set tools.sessions.visibility agent
   openclaw config set tools.agentToAgent.enabled false
   ```

4. **Pair with the scratch agent.** Send its bot a message, then approve the pairing request:

   ```bash
   openclaw pairing approve --channel telegram --account scratch <CODE>
   ```

5. **Check the routing:**

   ```bash
   openclaw agents list --bindings
   ```

`openclaw.example.json5` shows what these commands add to your config.
