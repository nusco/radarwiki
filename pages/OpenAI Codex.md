- **Blip:** [OpenAI Codex](https://www.thoughtworks.com/radar/tools/openai-codex)
- **Time:** ~1 hour 20 minutes
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Tools
- **Ring:** Adopt
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you use another coding agent, such as Claude Code, and focuses on what's different about Codex.

---

## Current state (late 2026)

"Codex" is a name OpenAI has reused several times: a 2021 code model, then in 2025 a cloud agent and an open-source command-line agent, and now a family of surfaces (CLI, IDE extension, desktop app and cloud tasks) built on the same agent loop. That loop is Apache-2.0 licensed and was rewritten in Rust in 2025. In 2026 its documentation moved into OpenAI's "ChatGPT Learn" site, so older links to `developers.openai.com/codex` now redirect there. The blip moved from *Trial* to *Adopt* in November 2026: Codex now stands with Claude Code and [[OpenCode]] as one of the coding agents teams use every day.

## Level 1 — What it is (~15 min)

OpenAI's coding agent, in the terminal, the IDE, a desktop app and the cloud, with enterprise controls and an open-source core.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/openai-codex) (~2 min) — read both versions. April 2026 warns about outdated library patterns, and November 2026 explains the move to *Adopt*: enterprise features, an open-source loop, and easy import from other agents.
- [ ] **~10 min** · Skim: [openai/codex](https://github.com/openai/codex) (OpenAI, README) — the open-source repository. Note the different surfaces it points to (CLI, IDE, desktop app, Codex Web), and how to install the CLI.

## Level 2 — Use it (~1 hour 5 minutes)

Set Codex up from your existing agent's configuration, and see how its sandbox and approvals work.

- [ ] **~10 min** · Read: [Permissions](https://learn.chatgpt.com/docs/permission-modes) (ChatGPT Learn, ~2 min) — the permission modes, from "Ask for approval" to "Full access". Note that each mode combines a sandbox (like `workspace-write`) with an approval policy, and that "Approve for me" sends approvals to an automatic reviewer instead of you.
- [ ] **~10 min** · Skim: [Import from another agent](https://learn.chatgpt.com/docs/import) (ChatGPT Learn, ~3 min) — the "challenger's gambit" the blip mentions: Codex CLI can import instructions, settings, skills and plugins from Claude Code or Cursor.
- [ ] **~45 min** · **Do:** Install the Codex CLI and import your Claude Code setup. Give Codex a task you recently gave Claude Code in the same repository, in "Ask for approval" mode. Compare the two: how each plans, what each asks permission for, and the result. Write down one thing Codex does better and one thing it does worse for you.

## If you have extra time

- [ ] **~30 min** · **Do:** Point Codex at an open-weight model, which the blip calls one of its strengths, through a hosted provider or a local runner (see [[Local coding models]]). Repeat the Level 2 task and compare.

## Wrap-up

This plan covers it for someone who already uses a coding agent. Building your own agents on Codex's open-source loop is covered in [[Coding harness for general-purpose agents]].

## Review the blip

- [ ] **~5 min** · Re-read [OpenAI Codex](https://www.thoughtworks.com/radar/tools/openai-codex) now that you know the topic.

## Related blips

- **[[Coding harness for general-purpose agents]]**: Codex's Apache-2.0 agent loop can be reused this way.
- **[[OpenCode]]**: another CLI-first coding agent that teams use daily.
- **[[Open-weight models]]**: Codex's compatibility makes it a solid choice for running them.
- **[[Claude Code]]**: the other CLI-first agent the blip puts Codex next to.
