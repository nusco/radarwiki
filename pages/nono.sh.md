- **Blip:** [nono.sh](https://www.thoughtworks.com/radar/tools/nono-sh)
- **Time:** ~40 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[Agent sandboxing]].

---

## Current state (late 2026)

Everyone agrees agents should run in a sandbox, but setting one up is enough friction that many developers don't. nono.sh, from the team behind Sigstore, is an open-source sandbox that uses the operating system's own isolation (Landlock on Linux, Seatbelt on macOS) instead of containers or VMs: one binary, no daemon, and SSH keys and other sensitive files blocked by default. It ships shareable security profiles for popular agents through a registry. The blip is new in November 2026. It's approaching 1.0, so its APIs may still change, and Windows needs WSL2.

## Level 1 — What it is (~10 min)

A lightweight, OS-level sandbox for agents, with ready-made profiles.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/nono-sh) (~1 min) — note why it matters: it lowers the cost of sandboxing.
- [ ] **~5 min** · Skim: [nono](https://github.com/nolabs-ai/nono) (README, ~4 min) — what it protects, and the quick start with a profile from the registry.

## Level 2 — Try it (~30 min)

- [ ] **~30 min** · **Do:** Install nono and run your coding agent with a profile from the registry. Repeat the tests from the [[Agent sandboxing]] exercise: write outside the project, read `~/.ssh`, reach a site that isn't allowed. Compare the results with your agent's built-in sandbox, and decide which you'd keep.

## Wrap-up

This plan covers it. Choosing the right isolation for each risk is covered in [[Agent sandboxing]].

## Review the blip

- [ ] **~5 min** · Re-read [nono.sh](https://www.thoughtworks.com/radar/tools/nono-sh) now that you know the topic.

## Related blips

- **[[Claude Code]]**: one of the autonomous tools nono.sh adds a layer of defense to.
- **[[OpenAI Codex]]**: another.
- **[[Docker]]**: the heavier isolation that nono.sh avoids.
