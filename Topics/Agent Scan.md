**Time:** ~45 minutes
**Radar edition:** April 2026
**Blip:** [Agent Scan](https://www.thoughtworks.com/radar/tools/agent-scan), formerly [MCP-Scan (November 2025)](https://www.thoughtworks.com/radar/tools/mcp-scan)
**Quadrant:** Tools
**Ring:** Assess
**Created:** 2026-10-21

*Assumption: you know the lethal trifecta and toxic flows, from [[Toxic flow analysis for AI]].*

---

## Layer 1 — What it finds (0:00–0:15, ~15 min)

**Goal:** Know what Agent Scan checks today (MCP servers *and* skills), and the blip's caveats.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/agent-scan) — short. It's useful for an inventory, but it sends metadata to Snyk, and you should check its false positives yourself before making it a mandatory gate.
- [ ] **Do:** Run `uvx snyk-agent-scan@latest inspect`. It lists the MCP servers, tools and skills it finds in your setup, without analyzing them or sending anything for analysis. This is the inventory the blip talks about.

## Layer 2 — Scan, and compare with a manual check (0:15–0:45, ~30 min)

**Goal:** See what an automated scan catches that a manual check doesn't.

- [ ] Skim: [The Agent Scan README](https://github.com/snyk/agent-scan) — read the section on what data it sends to Snyk, and the list of issues it reports.
- [ ] **Do:** Pick three entries from the `inspect` inventory, including at least one MCP server and one skill if you have them. For each, mark which leg of the lethal trifecta it provides, if any: untrusted content, private data, or a way to send data out. Did the inventory list anything you'd forgotten you had? Then go through the issues the README says the scanner reports, and decide which ones a manual check like yours would catch and which ones only a scanner could catch.
  - Optional: run a full scan (`uvx snyk-agent-scan@latest`). It needs a Snyk account and a `SNYK_TOKEN`, and the free tier can fail on the first try with "Daily usage limit reached for the public version of Agent-Scan". If you get that error, skip the full scan. Comparing your manual check with the README is enough for this exercise.

---

## If you have extra time

- [ ] Read: [Introducing MCP-Scan](https://invariantlabs.ai/blog/introducing-mcp-scan) (Luca Beurer-Kellner and Marc Fischer, Invariant Labs, Apr 2025, ~4 min) — the original launch post. It shows which attacks the tool was built to catch (tool poisoning, rug pulls, tool shadowing), and that sending data off for analysis was part of the design from the start.

---

## Current state of the topic

MCP-Scan started at Invariant Labs. It became Agent Scan after Snyk acquired the company, and it now covers skills and agent configurations, not just MCP servers. It's one of the few tools for inventorying an agent's supply chain, but it's still in *Assess*: the analysis runs in Snyk's cloud, and its signal quality isn't proven yet.

---

## Recommendation for future learning

This plan covers it.

---

## Related topics

- [MCP-Scan](https://www.thoughtworks.com/radar/tools/mcp-scan) (Nov 2025)
- [[Toxic flow analysis for AI]] (Nov 2025, Apr 2026)
- [[Agent Skills]] (Apr 2026)

---

- [ ] **Close:** [Review the blip](https://www.thoughtworks.com/radar/tools/agent-scan) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
