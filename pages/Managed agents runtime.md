- **Blip:** [Managed agents runtime](https://www.thoughtworks.com/radar/techniques/managed-agents-runtime)
- **Time:** ~1 hour
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you know why agents need a sandbox, from [[Agent sandboxing]].

---

## Current state (late 2026)

In 2025 the main coding agents gained "cloud" or "background" modes: you assign a task, the agent works in a remote sandbox, and you get back a pull request. In April 2026 Anthropic launched [[Claude Managed Agents]], a hosted runtime for any kind of agent, and other vendors offer similar services. Meanwhile some companies built their own runtimes, Ramp's Inspect being the best documented. The blip is new in November 2026, and its main point is that "managed" doesn't have to mean someone else's cloud: what matters is that the runtime is treated as production infrastructure.

## Level 1 — What it is (~10 min)

Move agents off developers' laptops onto a platform that runs them: sandboxed compute, triggers, credentials, session state and observability.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/managed-agents-runtime) (~3 min) — list what the runtime provides and what the team still defines (model, prompt, tools, skills). Note the two examples: a daily security triage agent, and agents that fix code smells across many repositories.

## Level 2 — How a runtime works (~50 min)

See the parts of a real runtime, and try a hosted one.

- [ ] **~35 min** · Read: [Why we built our background agent](https://builders.ramp.com/post/why-we-built-our-background-agent) (Ramp, 2026, ~12 min) — the most detailed public account of a self-built runtime. It covers sandboxes that start fast, session state, how the agent authenticates to GitHub, and the clients people use to start it (Slack, web, a browser extension). Read it for the design choices, and skip the product details.
- [ ] **~15 min** · **Do:** Start a task in a hosted runtime you have access to, such as Claude Code on the web or the GitHub Copilot coding agent: ask for a small fix in one of your repositories, and let it open a pull request. Then compare it with Ramp's design: which parts of the runtime did you see (sandbox, trigger, credentials, session state, logs), and which stayed hidden?

## Wrap-up

This plan covers the technique. The products have their own plans: [[Claude Managed Agents]], [[OpenAI Codex]] and [[Cursor]]. Running a runtime's agents unattended is covered in [[Unattended overnight agentic builds]].

## Review the blip

- [ ] **~5 min** · Re-read [Managed agents runtime](https://www.thoughtworks.com/radar/techniques/managed-agents-runtime) now that you know the topic.

## Related blips

- **[[Agent sandboxing]]**: the blip asks for sandboxing on every managed runtime.
- **[[Claude Managed Agents]]**: a general-purpose hosted runtime, the blip's main example.
- **[[OpenAI Codex]]**: its cloud tasks run in remote sandboxes managed by OpenAI.
- **[[Cursor]]**: its cloud agents run in remote sandboxes too.
