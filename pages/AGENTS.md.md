- **Blip:** [AGENTS.md](https://www.thoughtworks.com/radar/techniques/agents-md)
- **Time:** ~2 hours
- **Radar edition:** November 2025
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-24
- **Status:** #undone

This plan assumes that you've done Level 1 of [[Context engineering]], so you know why what's always in the context matters.

---

## Current state (late 2026)

AGENTS.md started at OpenAI in 2025. In December 2025, OpenAI donated it to the Agentic AI Foundation, under the Linux Foundation, together with MCP. Most coding agents read it now. Claude Code was the last big holdout: since v2.1.277 (September 2026), it reads AGENTS.md when a project has no `CLAUDE.md`. Research published in 2026 found that these files often don't help much, and that generated ones can hurt, so the interest has moved from "have one" to "keep it short and handwritten". The November 2026 Radar no longer lists AGENTS.md, but its [Agent instruction bloat](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat) blip (*Caution*) continues the story.

## Level 1 — What it is (~25 min)

Explain what an AGENTS.md is, what usually goes in it, and why one shared file name matters.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/agents-md) (~1 min) — a README for agents. What makes it valuable is the shared convention, not any particular format.
- [ ] **~10 min** · Read: [Cloudflare's AGENTS.md](https://github.com/cloudflare/agents/blob/main/AGENTS.md) (Cloudflare, 208 lines, ~4 min for these sections) — a real file from a real project. Read "Commands", "Nested AGENTS.md files" and "Boundaries" (Always / Ask first / Never), and notice how little of the file is prose.
- [ ] **~10 min** · Read: [agents.md](https://agents.md/) (AAIF, ~3 min) — the official site. It's short: why the format exists, which agents support it, and how nested files work (the closest file to the edited code wins).

## Level 2 — Write a good one (~60 min)

Write a short, handwritten AGENTS.md, and check that your agent loads it.

- [ ] **~15 min** · Read: [Writing a good AGENTS.md](https://www.philschmid.de/writing-good-agents) (Philipp Schmid, Feb 2026, ~4 min) — a terse guide based on research and practice. Include only what the agent can't infer, leave out codebase overviews and style rules, and don't generate the file with `/init`.
- [ ] **~15 min** · Read: [AGENTS.md in Claude Code](https://code.claude.com/docs/en/memory#agents-md) (Claude Code docs, ~5 min for these sections) — read "When Claude Code reads AGENTS.md" and "Share one file with other coding tools". It explains how AGENTS.md and `CLAUDE.md` coexist: Claude Code falls back to AGENTS.md only when there's no `CLAUDE.md`, or you can import AGENTS.md with `@AGENTS.md`.
- [ ] **~30 min** · **Do:** This repository has no `CLAUDE.md`, so write a root `AGENTS.md` for it by hand. Keep it under ~30 lines, and include only what an agent couldn't work out by itself. For example: plans go in `pages/` and come from the skills in `skills/`, the files in `Thoughtworks Radar/` come from the download script and shouldn't be edited by hand, and files get deleted with `trash`. Then start Claude Code here and run `/memory` to check that it loaded your file. You're done when an agent that has never seen the repository would make no mistakes it could easily avoid.

## Level 3 — Does it actually help? (~30 min)

Know what the evidence says about context files, and use it to prune your own.

- [ ] **~15 min** · Read: [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988) (Gloaguen et al., ETH Zurich, Feb 2026, rev. Sep 2026, ~5 min for these sections) — the study that the later Radar blips cite. Read the abstract, the Introduction and the Conclusion of the [full text](https://arxiv.org/html/2602.11988). On real tasks, context files didn't make agents noticeably better, and they made runs about 20% more expensive. Repository overviews didn't help, and handwritten files did better than generated ones.
- [ ] **~15 min** · **Do:** Go through the AGENTS.md you wrote in Level 2 line by line. Cut anything that's an overview, or that the README or a linter already covers. Decide which lines stay, and why.

Keeping instruction files lean as they grow over time is covered by the Agent instruction bloat item in Level 3 of [[Context engineering]].

## If you have extra time

- [ ] **~35 min** · Read: [Writing an effective AGENTS.md](https://aaif.io/blog/writing-an-effective-agents-md) (Steve Kearns, AAIF, Aug 2026, ~12 min) — the longest and most balanced guide. It has many examples from real repositories (Rails, VS Code, Kubo), a table that turns vague instructions into usable ones, and advice on when nested files are worth it. Read it if you maintain a larger repository than this one.
- [ ] **~30 min** · Read: [Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) (Kyle, HumanLayer, Nov 2025, <10 min) — the same advice applied to `CLAUDE.md`, with more on *why* agents ignore long instruction files. Schmid's guide in Level 2 builds on it.

## Wrap-up

This plan covers it. AGENTS.md is a small convention, and the bigger ideas behind it (what deserves a place in the context, and how to keep it lean) belong to [[Context engineering]]. The best way to go further is to keep your own file small.

**Left out:** GitHub's widely shared [How to write a great agents.md](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/) (Matt Nigh, Nov 2025) is about Copilot's custom agent files (`.github/agents/*.md`), not the repository-level AGENTS.md, and its numbers don't come with a method.

## Review the blip

- [ ] **~10 min** · Re-read [AGENTS.md](https://www.thoughtworks.com/radar/techniques/agents-md) now that you know the topic.

## Related blips

- **[[Context engineering]]**: AGENTS.md is one of its simplest techniques, a fixed starting file of instructions for the agent.
