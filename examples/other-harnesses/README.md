# One Workspace for Several Harnesses

If you use OpenClaw as an assistant and Claude Code or Codex for code, keep one set of rules for all of them.

- `AGENTS.md` holds the shared rules. OpenClaw, Codex and Hermes read it directly.
- `CLAUDE.md` is a thin file for Claude Code. It imports `AGENTS.md` with `@AGENTS.md` and adds only the Claude-specific lines.
- Keep `SOUL.md` and `IDENTITY.md` out of the coding harness's folder, so the assistant's persona stays with the assistant.
- Let one harness write memory, and point the others at the same notes and write-back rules.
