- **Blip:** [Linear](https://www.thoughtworks.com/radar/tools/linear)
- **Time:** ~40 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Linear is a commercial issue tracker that many startups have used instead of Jira for years: quick to set up like Trello, with real planning features. The reason for this blip, new in November 2026, is how well it works with coding agents. Agents join a workspace like members: you assign them issues, mention them in comments, and see what they did and why. Cursor, OpenAI Codex and Devin can take work from Linear this way, and other agents can reach it through Linear's MCP server.

## Level 1 — What it is (~15 min)

An issue tracker where coding agents are members of the team, and pick up work straight from the backlog.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/linear) (~1 min) — note the division of labor with [[Beads]]: Linear holds the work the team plans, Beads the smaller tasks agents create.
- [ ] **~10 min** · Read: [Agent platform](https://linear.app/docs/agents-in-linear) (Linear docs, ~4 min) — how agents are added, delegated issues and guided, and what they can't do (they aren't billable seats, and have no admin access).

## Level 2 — Try it (~25 min)

- [ ] **~25 min** · **Do:** In a free Linear workspace, create a small issue for a repository of yours, with clear acceptance criteria. Delegate it to an agent you have access to, or connect your coding agent through Linear's MCP server and ask it to pick up the issue. Watch how the agent reports its progress on the issue, and compare that with giving the same task in a chat.

## Wrap-up

This plan covers it. Tracking the agents' own finer-grained tasks is covered in [[Beads]].

## Review the blip

- [ ] **~5 min** · Re-read [Linear](https://www.thoughtworks.com/radar/tools/linear) now that you know the topic.

## Related blips

- **[[Beads]]**: sits a level below Linear, for the tasks agents create as they go.
- **[[OpenAI Codex]]**: one of the agents that can take on Linear issues.
- **[[Cursor]]**: another agent that works from Linear issues.
- **[[Claude Code]]**: can read and update issues through Linear's MCP server.
