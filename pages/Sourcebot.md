- **Blip:** [Sourcebot](https://www.thoughtworks.com/radar/tools/sourcebot)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Large companies have thousands of repositories, and both developers and coding agents need to search across all of them, not just the one they have checked out. Sourcegraph long filled that role, and Sourcebot is a newer, self-hosted alternative: it indexes repositories from GitHub, GitLab, Bitbucket and others, and gives fast, symbol-aware search and navigation. Its MCP server lets agents search the whole organization's code. The blip is new in November 2026. The core is free for small teams, and its AI chat ("Ask Sourcebot"), useful for people who don't code, is a paid feature.

## Level 1 — What it is (~10 min)

A self-hosted code search across all of an organization's repositories, for people and, through MCP, for agents.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/sourcebot) (~1 min) — note the two uses: large-scale refactoring and understanding legacy systems.

## Level 2 — Try it (~35 min)

- [ ] **~35 min** · **Do:** Run Sourcebot locally with [Docker Compose](https://docs.sourcebot.dev/docs/deployment/docker-compose.md) (Sourcebot docs, ~3 min), and index a few public repositories you know, or your own. Search for a function across all of them, and try jumping to its references. Then connect your coding agent to Sourcebot's [MCP server](https://docs.sourcebot.dev/docs/mcp/overview.md), and ask it a question that spans two repositories.

## Wrap-up

This plan covers it. Agents that understand legacy code are covered in [[Using GenAI to understand legacy codebases]].

## Review the blip

- [ ] **~5 min** · Re-read [Sourcebot](https://www.thoughtworks.com/radar/tools/sourcebot) now that you know the topic.

## Related blips

- **[[Software engineering agents]]**: they need the same cross-repository context as developers.
- **[[Using GenAI to understand legacy codebases]]**: Sourcebot helps agents navigate legacy systems.
- **[[Sourcegraph]]**: the older code search platform in the same space.
