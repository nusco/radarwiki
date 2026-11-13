**Time:** ~1.75 hours
**Radar edition:** November 2025 and April 2026
**Blip:** [Toxic flow analysis for AI](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai)
**Quadrant:** Techniques
**Ring:** Assess
**Created:** 2026-10-21

*Series: after [[Serena]] · next: [[Agent Scan]]. Assumption: you know how prompt injection attacks MCP servers, from Layer 4 of [[Model Context Protocol (MCP)]].*

---

## Layer 1 — The technique (0:00–0:45, ~45 min)

**Goal:** Explain toxic flow analysis: mapping the paths through an agent's tools where untrusted content, private data and an outbound channel meet.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai) — read both versions. In April 2026 it extends from MCP servers to Agent Skills.
- [ ] Read: [Toxic flows in agentic systems](https://invariantlabs.ai/blog/toxic-flow-analysis) (Invariant Labs, Jul 2025, ~4 min) — the post that introduced the term, with the GitHub MCP exploit as its example.
- [x] Read: [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (Simon Willison) — private data plus untrusted content plus a way to send data out. Toxic flow analysis is the search for paths that combine all three.

## Layer 2 — Apply it to your setup (0:45–1:45, ~60 min)

**Goal:** Find the toxic flows in your own agent setup, and know a simple rule for removing them.

- [ ] Read: [Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/) (Meta, Oct 2025) — a practical rule that follows from the lethal trifecta: in a session, an agent should have no more than two of untrusted input, sensitive data, and the ability to change things or communicate outside.
- [ ] **Do:** Draw the flow graph of your Claude Code setup by hand. List each MCP server, skill and built-in tool (web fetch, shell, file access), and mark which part of the trifecta it provides. For example, [[Context7]] brings in untrusted content, file reads can reach private data, and web fetch can send data out. Find one path that connects all three, and decide which leg you'd cut. You'll compare your graph with an automated scan in [[Agent Scan]].

---

## If you have extra time

- [ ] Read the [OpenClaw](https://www.thoughtworks.com/radar/tools/openclaw) entry, the "permission-hungry" agent the newer blip uses as its example.

---

## Current state of the topic

Invariant Labs introduced the term in mid-2025, along with a tool that automates it (now [[Agent Scan]], which has the tool's history). The technique is still in *Assess*, because prompt injection itself is unsolved: no filter reliably stops it. That's why rules that limit capabilities, like the trifecta and the Rule of Two, are the best defense. Since April 2026 the concern covers skills too, after studies such as Snyk's ToxicSkills (see [[Agent Skills]]).

---

## Recommendation for future learning

This plan is enough for a generalist. If you ever deploy agents for other people, study agent security more broadly as its own topic (~3 hours): sandboxing, permissions, and prompt injection defenses.

**Related topics in Thoughtworks Radar:**

- [[Agent Scan]] (Apr 2026), formerly MCP-Scan (Nov 2025)
- [Sandboxed execution for coding agents](https://www.thoughtworks.com/radar/techniques/sandboxed-execution-for-coding-agents) (Apr 2026)
- [OpenClaw](https://www.thoughtworks.com/radar/tools/openclaw) (Apr 2026)
- [[Agent Skills]] (Apr 2026)
- [[Model Context Protocol (MCP)]] (Apr 2025, Nov 2025)

---

- [ ] **Close:** [Review the blip](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
