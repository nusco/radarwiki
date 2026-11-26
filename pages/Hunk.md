- **Blip:** [Hunk](https://www.thoughtworks.com/radar/tools/hunk)
- **Time:** ~35 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Reviewing an agent's changes in a pull request or a plain `git diff` is slow, and the diff doesn't say why the agent did what it did. Hunk, an open-source terminal diff viewer started in March 2026, shows a whole changeset as a multi-file review, refreshes while the agent works, and lets the agent leave notes next to the lines it changed. It works with Git, Jujutsu and Sapling. The blip is new in November 2026, and Hunk is still before version 1.0. The Radar's open question: do the notes make reviews faster, or just add more to read?

## Level 1 — What it is (~10 min)

A terminal diff viewer for reviewing agent changes, with the agent's own notes beside the code.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/hunk) (~1 min) — note the warning that skipping line-by-line review leads to complacency with AI-generated code.
- [ ] **~5 min** · Skim: [hunk](https://hunk.dev/) (product page, ~2 min) — the features, especially agent notes and watch mode.

## Level 2 — Try it (~25 min)

- [ ] **~25 min** · **Do:** Install Hunk and load its agent skill. Ask your coding agent for a change across a few files, with notes in Hunk explaining each hunk. Review it in Hunk, then review a similar change with plain `git diff`. Did the notes speed you up, or slow you down?

## Wrap-up

This plan covers it. Deciding which changes deserve a careful human review is covered in [[Risk-tiered human oversight]].

## Review the blip

- [ ] **~5 min** · Re-read [Hunk](https://www.thoughtworks.com/radar/tools/hunk) now that you know the topic.

## Related blips

- **[[Complacency with AI-generated code]]**: the risk of skipping human review, which Hunk tries to make easier.
- **[[Jujutsu]]**: one of the version control systems Hunk supports.
- **[[Difftastic]]**: a syntax-aware diff tool, without Hunk's agent notes.
