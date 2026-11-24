- **Blip:** [Context engineering](https://www.thoughtworks.com/radar/techniques/context-engineering)
- **Time:** ~3 hours
- **Radar edition:** November 2025 and April 2026
- **Quadrant:** Techniques
- **Ring:** Adopt
- **Updated:** 2026-11-24
- **Status:** #undone

---

## Current state (late 2026)

The term became popular in mid-2025, when people started saying that "prompt engineering" no longer described the work of building agents. It moved from *Assess* to *Adopt* within one Radar cycle, which is unusually fast. Many recent tools apply its ideas: [[Agent Skills]] (progressive disclosure), tool search for MCP (see [[MCP by default]]), [[Context7]] (fresh docs on demand), and [[Serena]] (precise code retrieval instead of reading whole files). Larger context windows haven't made it less important. Context rot means that what you put in the context still matters more than how much fits. The November 2026 Radar doesn't list the technique itself, but it moves one of its practices, [Progressive context disclosure](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure), to *Adopt*.

## Level 1 — What it is (~60 min)

Explain how context engineering differs from prompt engineering, and name its main techniques.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/context-engineering) (~3 min) — read both versions. In November 2025 it was *Assess*, with a list of practices. In April 2026 it's *Adopt*, and the Radar calls it a core architectural concern.
- [ ] **~10 min** · **Do:** Start Claude Code in this repository and run `/context`. Look at what fills the context before you've asked anything: the system prompt, `CLAUDE.md`, memory, skill descriptions, MCP tools. That's the context you'll learn to engineer.
- [ ] **~40 min** · Read: [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Prithvi Rajasekaran and others, Anthropic, Sep 2025, ~15 min) — the reference article, cited by both versions of the blip. It covers system prompts, tools, just-in-time retrieval, compaction, notes and sub-agents.

## Level 2 — How contexts fail (~60 min)

Know why "just put everything in a big context window" doesn't work.

- [ ] **~30 min** · Read: [Context rot](https://www.trychroma.com/research/context-rot) (Kelly Hong, Anton Troynikov and Jeff Huber, Chroma, Jul 2025) — the study behind the term. 18 models get less reliable as their input grows, even on simple tasks. Read the introduction and the conclusion (~10 min), and look at the charts in between. Skip the details of each experiment.
- [ ] **~30 min** · Read: [How to fix your context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html) (Drew Breunig, Jun 2025, ~10 min) — four ways a context fails (poisoning, distraction, confusion, clash) and how to fix each one.

## Level 3 — Engineer your own context (~60 min)

See what fills your own agent's context, and make it leaner.

- [ ] **~15 min** · Read: [Progressive context disclosure](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure) and [Agent instruction bloat](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat) (Radar, Apr 2026 and Nov 2026, ~2 min each) — two short entries that turn the theory into a habit.
- [ ] **~45 min** · **Do:** Run `/context` again, and sort what you see into two groups: always loaded (system prompt, `CLAUDE.md`, memory, skill descriptions, MCP tool names) and loaded on demand (skill bodies, deferred tools, files). Make one change, then measure again. For example, disable an MCP server you don't use here, or move a rarely needed instruction into a skill.

## If you have extra time

- [ ] **~25 min** · Read: [Context rot: the emerging challenge that could hold back LLM progress](https://www.understandingai.org/p/context-rot-the-emerging-challenge) (Timothy B. Lee, Nov 2025, ~10 min free part) — linked by the blip. It isn't a summary of the Chroma study, which it mentions only in passing. It puts context rot in a wider story: the earlier needle-in-a-haystack tests, why attention gets more expensive as the input grows, and why this matters for agents that work for hours or days. Read it if you want the "why" behind Level 2. The paywall cuts in just before Lee explains why he thinks context rot happens. Stop there, because the rest isn't needed.
- [ ] **~15 min** · Read: [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) (Claude docs, ~5 min for these sections) — the "context setup" technique from the newer blip. Read only the opening and "How prompt caching works", to see why stable context at the start of the prompt is cheaper.
- [ ] **~15 min** · Read: [Subagents](https://code.claude.com/docs/en/sub-agents) (Claude Code docs, ~5 min for the opening) — cited by the older blip. Read only the opening, up to the built-in subagents: sub-agents keep a side task's context out of the main conversation.

## Wrap-up

This is one of the most relevant topics for a generalist, and 3 hours gives a generalist a solid understanding. If you ever build an agent yourself, plan another ~3 hours on memory, compaction and sub-agents. That's better done as part of a hands-on agent-building plan. Start it with [Context engineering for agents](https://www.langchain.com/blog/context-engineering-for-agents) (LangChain, Jul 2025, 14 min), cited by the older blip, which groups the same techniques from a builder's point of view: write, select, compress, isolate.

**Left out from the blip:** the two research papers cited by the newer version ([dynamic tool selection](https://arxiv.org/abs/2509.20386v1) and [active context compression](https://arxiv.org/abs/2601.07190)) are research-level, and the Anthropic article covers the same ideas for a generalist. The older version's prompt-engineering basics ([tips](https://www.promptingguide.ai/introduction/tips), [few-shot](https://www.promptingguide.ai/techniques/fewshot)) are assumed knowledge. Its [just-in-time tooling](https://jentic.com/blog/just-in-time-tooling) post is mostly a product pitch, and [[MCP by default]] covers the same idea as MCP tool search. The newer version's [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) is in [[Naive API-to-MCP conversion]], where it fits best.

## Review the blip

- [ ] **~10 min** · Re-read [Context engineering](https://www.thoughtworks.com/radar/techniques/context-engineering) now that you know the topic.

## Related Radar topics

- [Progressive context disclosure](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure)
- [Agent instruction bloat](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat)
- [Context graph](https://www.thoughtworks.com/radar/techniques/context-graph)
- [Curated shared instructions for software teams](https://www.thoughtworks.com/radar/techniques/curated-shared-instructions-for-software-teams)
- [[AGENTS.md.md|AGENTS.md]]
- [[Agent Skills]]
- [Code intelligence as agentic tooling](https://www.thoughtworks.com/radar/techniques/code-intelligence-as-agentic-tooling)
- [[Context7]]
