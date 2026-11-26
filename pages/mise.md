- **Blip:** [mise](https://www.thoughtworks.com/radar/tools/mise)
- **Time:** ~55 minutes
- **Radar edition:** October 2024, April 2026 and November 2026
- **Quadrant:** Tools
- **Ring:** Adopt
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Developers have long used one version manager per language (nvm for Node, pyenv for Python, rbenv for Ruby), or asdf to manage them all through plugins. mise ("mise-en-place") started as a faster, Rust-based asdf, and grew into a single tool for three jobs: tool versions, environment variables (replacing direnv) and project tasks, all in one `mise.toml`. The Radar first covered it in October 2024 (*Assess*), and moved it to *Adopt* in April 2026, where it stays. It also checks the signatures of the tools it installs, which most version managers don't.

## Level 1 — What it is (~5 min)

One tool and one config file for a project's tool versions, environment variables and tasks.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/mise) (~1 min per version) — read all three versions, oldest first, to see it grow from "a faster asdf" to "a default frontend for the development environment".

## Level 2 — Use it (~50 min)

Set up a project with mise, from tools to tasks.

- [ ] **~15 min** · Read: [Getting started](https://mise.jdx.dev/getting-started.html) (mise docs, ~5 min) — the quick start: install, run a tool, then set up a project with tools, environment variables and a task. Pay attention to "Trust project configuration": mise won't run a project's config until you trust it.
- [ ] **~35 min** · **Do:** Pick a project that depends on a specific language version, and describe it in a `mise.toml`: the tool versions, one environment variable, and a task (like `test` or `lint`). Check that a fresh shell picks the right versions, and that `mise run test` works. If you already use nvm, pyenv or asdf, note what you could uninstall.

## If you have extra time

- [ ] **~25 min** · Read: [Migrating from asdf and direnv to mise](https://dev.to/masutaka/migrating-from-asdf-and-direnv-to-mise-3nhi) (Takashi Masuda, Mar 2026, ~8 min) — a real migration on macOS, with the small problems it ran into and how the author solved them. Read it before moving your own machine over. If you use asdf, the official [Migrating from asdf](https://mise.jdx.dev/dev-tools/comparison-to-asdf.html) guide maps the commands.

## Wrap-up

This plan covers it. The supply-chain checks the blip mentions are covered in [[Cosign]].

## Review the blip

- [ ] **~5 min** · Re-read [mise](https://www.thoughtworks.com/radar/tools/mise) now that you know the topic.

## Related blips

- **[[Cosign]]**: mise uses it to verify the tools it installs.
- **[[Rust]]**: mise is written in Rust, which makes it faster than shell-based version managers.
