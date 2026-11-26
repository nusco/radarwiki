- **Blip:** [Omnigent](https://www.thoughtworks.com/radar/platforms/omnigent)
- **Time:** ~35 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Every coding agent has its own way to handle policies, sandboxing, credentials and sessions. Omnigent, which Databricks open-sourced in June 2026, is a "meta-harness" that sits above several coding agents (Claude Code, Codex, Pi, and agents defined in YAML) and provides those things once: spending caps and approvals, an OS sandbox that injects credentials without showing them to the agent, resumable sessions, and an inbox of parallel sessions. It can talk to agents through [[Agent Client Protocol (ACP)|ACP]]. Run as a shared server, it adds single sign-on and admin policies. The blip is new in November 2026, with two caveats: the project is alpha, and nobody knows yet what the right abstraction over coding agents is.

## Level 1 — What it is (~15 min)

One layer of policies, sandboxing and sessions over whichever coding agents developers choose.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/omnigent) (~2 min) — note who it suits: organizations that want the same controls whatever agent developers use.
- [ ] **~10 min** · Skim: [Omnigent](https://omnigent.ai/) (project site) — the features and the architecture diagram.

## Level 2 — Try it (~20 min)

- [ ] **~20 min** · **Do:** Install Omnigent, and run two sessions with two different coding agents under one policy, such as a spending cap or an approval before running shell commands. Check that the policy applies to both. Then decide which of its features your agent already has on its own.

## Wrap-up

This plan covers it, for an alpha project. Running parallel agents in the terminal is covered in [[Herdr]], and sandboxing in [[Agent sandboxing]].

## Review the blip

- [ ] **~5 min** · Re-read [Omnigent](https://www.thoughtworks.com/radar/platforms/omnigent) now that you know the topic.

## Related blips

- **[[Agent Client Protocol (ACP)]]**: Omnigent can drive agents through it, instead of wrapping each CLI.
- **[[OpenAI Codex]]**: one of the agents it sits above.
- **[[Pi]]**: another.
- **[[Herdr]]**: offers a similar inbox of parallel sessions on a laptop.
- **[[Claude Code]]**: another agent it sits above.
- **[[E2B]]**: one of the cloud sandboxes its sessions can run in.
