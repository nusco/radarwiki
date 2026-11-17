**Time:** ~45 minutes
**Radar edition:** April 2026
**Blip:** [Agent Scan](https://www.thoughtworks.com/radar/tools/agent-scan), formerly [MCP-Scan (November 2025)](https://www.thoughtworks.com/radar/tools/mcp-scan)
**Quadrant:** Tools
**Ring:** Assess
**Created:** 2026-10-21

*Assumption: you know the lethal trifecta and toxic flows, from [[Toxic flow analysis for AI]].*

---

## Current state of the topic (as of 2026-11-15)

MCP-Scan started at Invariant Labs. It became Agent Scan after Snyk acquired the company, and it now covers skills and agent configurations, not just MCP servers. It's one of the few tools for inventorying an agent's supply chain, but it's still in *Assess*: the analysis runs in Snyk's cloud, and its signal quality isn't proven yet.

---

## Level 1 — What it finds, and why (0:00–0:15, ~15 min)

**Goal:** Know what Agent Scan checks today (MCP servers *and* skills), why an inventory of your agent's supply chain is worth having, and the blip's caveats.

- [ ] **~3 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/agent-scan) (~1 min) — it's useful for an inventory, but it sends metadata to Snyk, and you should check its false positives yourself before making it a mandatory gate.
- [ ] **~12 min** · **Do:** Run `uvx snyk-agent-scan@latest inspect`. It lists the MCP servers, tools and skills it finds in your setup, without analyzing them or sending anything for analysis. This is the inventory the blip talks about.

## Level 2 — How it compares with a manual check (0:15–0:45, ~30 min)

**Goal:** See what an automated scan catches that a manual check doesn't.

- [ ] **~10 min** · Skim: [The Agent Scan README](https://github.com/snyk/agent-scan) (~14 min in full) — read only the section on what data it sends to Snyk, and the list of issues it reports.
- [ ] **~20 min** · **Do:** Pick three entries from the `inspect` inventory, including at least one MCP server and one skill if you have them. For each, mark which leg of the lethal trifecta it provides, if any: untrusted content, private data, or a way to send data out. Did the inventory list anything you'd forgotten you had? Then go through the issues the README says the scanner reports, and decide which ones a manual check like yours would catch and which ones only a scanner could catch.

---

## If you have extra time

- [ ] **~12 min** · Read: [Introducing MCP-Scan](https://invariantlabs.ai/blog/introducing-mcp-scan) (Luca Beurer-Kellner and Marc Fischer, Invariant Labs, Apr 2025, ~4 min) — the original launch post. It shows which attacks the tool was built to catch (tool poisoning, rug pulls, tool shadowing), and that sending data off for analysis was part of the design from the start.
- [ ] **~30 min** · **Do:** Run a full scan (`uvx snyk-agent-scan@latest`) and compare its findings with your manual check from Level 2. It needs a Snyk account and a `SNYK_TOKEN`, and the free tier can fail on the first try with "Daily usage limit reached for the public version of Agent-Scan". If you get that error, try again later or skip it.

---

## Recommendation for future learning

This plan covers it.

**Left out from the blip:** the older MCP-Scan blip links to Invariant Labs' [post on tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks). [[Model Context Protocol (MCP)]] already covers tool poisoning, and the launch post above shows how the scanner catches it.

Related Radar topics:

- [MCP-Scan](https://www.thoughtworks.com/radar/tools/mcp-scan) (Nov 2025)
- [[Toxic flow analysis for AI]] (Nov 2025, Apr 2026)
- [[Agent Skills]] (Apr 2026)

---

- [ ] **~10 min** · **Close:** [Review the blip](https://www.thoughtworks.com/radar/tools/agent-scan) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
