- **Blip:** [Deep Agents](https://www.thoughtworks.com/radar/languages-and-frameworks/deep-agents)
- **Time:** ~50 minutes
- **Radar edition:** November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know what an agent harness is, from [[Coding harness for general-purpose agents]].

---

## Current state (late 2026)

In July 2025, LangChain's founder Harrison Chase noticed that the most capable agents, like Claude Code, shared a simple recipe: a loop that calls tools, plus a long system prompt, a planning tool, subagents and a file system. He called them "deep agents", and released Deep Agents, an open-source harness that packages that recipe for your own agents, in Python and TypeScript. It has evolved since: planning is now opt-in, and LangChain offers a managed version. The blip is new in November 2026. It fits teams already using LangChain or LangGraph that need a capable, long-running agent inside a larger workflow.

## Level 1 — What it is (~15 min)

A ready-made harness for long-running agents, in the style of coding agents, for use in your own applications.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/deep-agents) (~1 min).
- [ ] **~10 min** · Read: [Deep Agents](https://www.langchain.com/blog/deep-agents) (Harrison Chase, LangChain, Jul 2025, ~3 min) — the post that named the pattern, and its four ingredients. Some details have changed since: planning is no longer built in by default.

## Level 2 — Build one (~35 min)

- [ ] **~35 min** · **Do:** Follow the quickstart in the [Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview) (LangChain docs) to create an agent with one tool. Give it a task that needs several steps, such as researching a topic and writing a short report to a file. Look at what it delegated to subagents and what it wrote to its file system. Compare with the coding harness approach from [[Coding harness for general-purpose agents]].

## Wrap-up

This plan covers it. The frameworks it builds on have their own plans: [[LangChain]] and [[LangGraph]].

## Review the blip

- [ ] **~5 min** · Re-read [Deep Agents](https://www.thoughtworks.com/radar/languages-and-frameworks/deep-agents) now that you know the topic.

## Related blips

- **[[Langfuse]]**: observability for Deep Agents, through the LangChain ecosystem.
- **[[LangGraph]]**: Deep Agents integrates with it for larger agent workflows.
- **[[LangChain]]**: the framework family Deep Agents belongs to.
- **[[Agent Skills]]**: one of the harness features Deep Agents supports.
