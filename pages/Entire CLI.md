- **Blip:** [Entire CLI](https://www.thoughtworks.com/radar/tools/entire-cli)
- **Time:** ~40 minutes
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Git records what changed, but not the agent session that produced the change. Entire CLI hooks into Git and stores each agent session (prompts, transcript, tool calls, files touched) in the repository, next to the commits, but outside the branch history. It's the command-line tool of Entire, a company building a Git hosting service, but capture works in any Git repository without an account. The blip stays in *Assess* in November 2026, with a new lesson from a Thoughtworks team: sharing sessions helps people learn how teammates prompt, but some developers don't want everything they ask an agent to be permanently readable by everyone with access to the repository.

## Level 1 — What it is (~15 min)

Store your agent sessions with your commits, so your team can see how each change was made.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/entire-cli) (~2 min) — read both versions. April 2026 is about audit trails and checkpoints, and November 2026 about sharing sessions, and its cost in privacy.
- [ ] **~10 min** · Skim: [Entire CLI](https://github.com/entireio/cli) (Entire, README) — read "Quick Start" and "Security & Privacy". Note the warning: sessions are pushed with the repository, so a public repository makes them public.

## Level 2 — Try it (~25 min)

- [ ] **~25 min** · **Do:** In a private test repository, run `entire enable`, make a change with your coding agent, and commit. Look at what was stored with the commit. Then read the session as if you were a teammate: what would you learn from it, and is there anything you'd rather not share? Decide whether your team would use it.

## Wrap-up

This plan covers it. A private alternative is covered in [[AgentsView]], and line-level attribution of AI code in [[Git AI]].

## Review the blip

- [ ] **~5 min** · Re-read [Entire CLI](https://www.thoughtworks.com/radar/tools/entire-cli) now that you know the topic.

## Related blips

- **[[OpenAI Codex]]**: one of the coding agents Entire CLI captures.
- **[[Pi]]**: another supported agent.
- **[[OpenCode]]**: another supported agent.
- **[[AgentsView]]**: a local alternative for developers who don't want to share their sessions.
- **[[Cursor]]**: another supported agent.
- **[[Claude Code]]**: another supported agent.
