- **Blip:** [Agent sandboxing](https://www.thoughtworks.com/radar/techniques/agent-sandboxing)
- **Time:** ~2 hours 50 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Adopt
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

The blip is new in November 2026, but it continues [Sandboxed execution for coding agents](https://www.thoughtworks.com/radar/techniques/sandboxed-execution-for-coding-agents) (*Trial*, April 2026), and widens it from coding agents to all agents, straight into *Adopt*. Sandboxing went mainstream in a year. In late 2025 the major coding agents shipped built-in OS-level sandboxes, and in 2026 container, microVM and remote sandboxes became products of their own. The reason is that prompt injection is still unsolved, so the safest assumption is that an agent may be turned against you. A sandbox limits the damage it can do. The open problem is network access: blocking files is easy, but deciding which hosts an agent can reach is still a judgment call.

## Level 1 — Why agents need a sandbox (~35 min)

Understand the trade-off a sandbox resolves: agents are most useful when they run without asking permission, and most dangerous then too.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/agent-sandboxing) (~2 min) — then its predecessor, [Sandboxed execution for coding agents](https://www.thoughtworks.com/radar/techniques/sandboxed-execution-for-coding-agents) (~2 min), which lists concrete tools. Notice how the new blip shifts the focus from tools to least privilege.
- [ ] **~20 min** · Read: [Living dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/) (Simon Willison, Oct 2025, ~5 min) — an annotated talk on why "YOLO mode" is so productive, why prompt injection makes it risky, and why sandboxing is "the only solution that's credible". The background on the lethal trifecta is covered in [[Toxic flow analysis for AI]].
- [ ] **~5 min** · Skim: [Felony Bench](https://www.felonybench.com/) (Felpix) — the blip's "recent security headlines": a tongue-in-cheek tally of real incidents in 2026 where AI agents broke into third-party systems, each with a source. Skim the list to see what an unsandboxed agent can actually do.

## Level 2 — How a built-in sandbox works (~1.25 hours)

See the two boundaries every agent sandbox needs, filesystem and network, and test them on your own agent.

- [ ] **~20 min** · Read: [Beyond permission prompts: making Claude Code more secure and autonomous](https://www.anthropic.com/engineering/claude-code-sandboxing) (David Dworken and Oliver Weller-Davies, Anthropic, Oct 2025, ~6 min) — a short engineering post on why both boundaries are needed, and how an OS-level sandbox lets the agent run with fewer prompts. Pay attention to how credentials stay outside the sandbox.
- [ ] **~15 min** · Skim: [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing) (Claude Code docs) — read "What the sandbox restricts" and "Sandbox modes", and skip the configuration details. Note what runs *outside* the sandbox: you'll test it next.
- [ ] **~40 min** · **Do:** Turn on the sandbox in Claude Code with `/sandbox`, in a throwaway project. Ask the agent to write a file outside the project folder, to read `~/.ssh`, and to `curl` a site that isn't allowed. Write down what's blocked, what asks for permission, and what still gets through. End with one sentence: what would a prompt-injected agent still be able to do here?

## Level 3 — Choosing the right boundary (~1 hour)

Go beyond the built-in sandbox, and choose an isolation level from the risk, as the blip recommends.

- [ ] **~35 min** · Read: [External sandboxes for coding agents](https://blog.primeradiant.com/external-sandboxes-for-coding-agents/) (Simon Willison, Prime Radiant, Nov 2026, 12 min) — a recent take on moving the sandbox outside the agent, with three prototypes (a VM, a container, a microVM) and a proxy that controls network access and swaps in credentials. Read it for the design, not the setup commands: the prototypes are unaudited.
- [ ] **~25 min** · **Do:** Pick three agent uses: one you run today, one unattended (like an overnight build), and one that reads untrusted content (like triaging public GitHub issues). For each, do a quick [[Threat modeling]] pass: what's the worst a hijacked agent could do? Then choose a boundary (built-in sandbox, container, microVM or remote sandbox) and a network policy, and write one line on why.

## If you have extra time

- [ ] **~20 min** · Read: [Development containers](https://code.claude.com/docs/en/devcontainer) (Claude Code docs, ~8 min for the first sections and "Restrict network egress") — the container option from the April 2026 blip, if you want to try one after the Level 3 exercise. Read the warning on what a container doesn't stop.

## Wrap-up

This plan covers the technique for a generalist. Most of the remaining depth is in specific tools, such as container and microVM runtimes, and in agent security as a whole.

## Review the blip

- [ ] **~5 min** · Re-read [Agent sandboxing](https://www.thoughtworks.com/radar/techniques/agent-sandboxing) now that you know the topic.

## Related blips

- **[[Threat modeling]]**: the blip asks you to choose the isolation level from a threat model.
- **[[Sandboxed execution for coding agents]]**: the April 2026 blip that this one builds on and generalizes.
