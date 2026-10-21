**Time:** ~2 hours · **Source:** [Thoughtworks Radar – Context engineering (Adopt, April 2026)](https://www.thoughtworks.com/radar/techniques/context-engineering)

*Series: after [[Agent Skills]] · next: [[Context7]]. This plan ties together much of what came before it: tool design, MCP vs. CLI, and skills.*

---

## Layer 1 — What it is (0:00–0:40, ~40 min)

**Goal:** Explain how context engineering differs from prompt engineering, and name its main techniques.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/context-engineering) — read both versions. In November 2025 it was *Assess*, with a list of practices. In April 2026 it's *Adopt*, and the Radar calls it a core architectural concern.
- [ ] Read: [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Anthropic, Sep 2025, ~15 min) — the reference article, cited by both versions of the blip. It covers system prompts, tools, just-in-time retrieval, compaction, notes and sub-agents.

## Layer 2 — How contexts fail (0:40–1:20, ~40 min)

**Goal:** Know why "just put everything in a big context window" doesn't work.

- [ ] Skim: [Context rot](https://www.trychroma.com/research/context-rot) (Chroma, Jul 2025) — the study behind the term. 18 models get less reliable as their input grows, even on simple tasks. Read the introduction and the results. It's long, so skip the appendix.
- [ ] Read: [How to fix your context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html) (Drew Breunig, Jun 2025) — four ways a context fails (poisoning, distraction, confusion, clash) and how to fix each one.

## Layer 3 — Engineer your own context (1:20–2:00, ~40 min)

**Goal:** See what fills your own agent's context, and make it leaner.

- [ ] Read: [Progressive context disclosure](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure) and [Agent instruction bloat](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat) (Radar, Apr 2026) — two short entries that turn the theory into a habit.
- [ ] **Do:** Start Claude Code in this repository and run `/context`. Sort what you see into two groups: always loaded (system prompt, `CLAUDE.md`, memory, skill descriptions, MCP tool names) and loaded on demand (skill bodies, deferred tools, files). Make one change, then measure again. For example, disable an MCP server you don't use here, or move a rarely needed instruction into a skill.

---

## If you have extra time

- [ ] Read: [Context engineering for agents](https://blog.langchain.com/context-engineering-for-agents/) (Lance Martin, LangChain) — another way to group the same techniques: write, select, compress, isolate.
- [ ] Skim: [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) (Claude docs) — the "context setup" technique from the newer blip, and why stable context at the start of the prompt is cheaper.

---

## Current state of the topic

The term became popular in mid-2025, when people started saying that "prompt engineering" no longer described the work of building agents. It moved from *Assess* to *Adopt* within one Radar cycle, which is unusually fast. Many recent tools apply its ideas: [[Agent Skills]] (progressive disclosure), tool search for MCP (see [[MCP by default]]), [[Context7]] (fresh docs on demand), and [[Serena]] (precise code retrieval instead of reading whole files). Larger context windows haven't made it less important. Context rot means that what you put in the context still matters more than how much fits.

---

## Recommendation for future learning

This is one of the most relevant topics in the series, and 2 hours gives a generalist a solid understanding. If you ever build an agent yourself, plan another ~2 hours on memory, compaction and sub-agents. That's better done as part of a hands-on agent-building plan.

**Related topics in Thoughtworks Radar:**

- [ ] [Progressive context disclosure](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure) (Apr 2026)
- [ ] [Agent instruction bloat](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat) (Apr 2026)
- [ ] [Context graph](https://www.thoughtworks.com/radar/techniques/context-graph) (Apr 2026)
- [ ] [Curated shared instructions for software teams](https://www.thoughtworks.com/radar/techniques/curated-shared-instructions-for-software-teams) (Nov 2025, Apr 2026)
- [ ] [AGENTS.md](https://www.thoughtworks.com/radar/techniques/agents-md) (Nov 2025)
- [ ] [Agent Skills](https://www.thoughtworks.com/radar/techniques/agent-skills) (Apr 2026)
- [ ] [Code intelligence as agentic tooling](https://www.thoughtworks.com/radar/techniques/code-intelligence-as-agentic-tooling) (Apr 2026)
- [ ] [Context7](https://www.thoughtworks.com/radar/tools/context7) (Nov 2025)
