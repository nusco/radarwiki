- **Blip:** [Herdr](https://www.thoughtworks.com/radar/tools/herdr)
- **Time:** ~35 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know a terminal multiplexer like tmux.

---

## Current state (late 2026)

Developers who run several coding agents at once need to know which one is waiting for them, and to pick up interrupted work. Herdr, an open-source terminal multiplexer written in Rust, is built for that: it works like tmux, with panes and detaching, but it also shows whether each agent is working, blocked, done or idle, and agents can drive it from the command line. The blip is new in November 2026. GUI alternatives exist, such as T3 Code, Orca and Paseo. Agents don't survive a restart of Herdr's server, so persistence has limits.

## Level 1 — What it is (~10 min)

A terminal multiplexer that knows which of your agents needs attention.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/herdr) (~1 min).
- [ ] **~5 min** · Skim: [herdr](https://github.com/herdrdev/herdr) (README, ~3 min) — the features and install, and the note on what survives a restart.

## Level 2 — Try it (~25 min)

- [ ] **~25 min** · **Do:** Install Herdr and run two coding agents in separate panes, on two small tasks. Detach, do something else, and reattach. Check how quickly you can tell which agent needs you. Decide whether it beats your current way of running parallel agents.

## Wrap-up

This plan covers it. When parallel agents help, and when they don't, is covered in [[Subagents for better context management]] and [[Coding agent swarms]].

## Review the blip

- [ ] **~5 min** · Re-read [Herdr](https://www.thoughtworks.com/radar/tools/herdr) now that you know the topic.

## Related blips

- **[[Orca]]**: one of the GUI-based alternatives the blip names.
