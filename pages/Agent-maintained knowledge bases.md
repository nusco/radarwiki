- **Blip:** [Agent-maintained knowledge bases](https://www.thoughtworks.com/radar/techniques/agent-maintained-knowledge-bases)
- **Time:** ~1 hour
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

The pattern took off in April 2026, when Andrej Karpathy published his "LLM Wiki" idea file. It spawned dozens of implementations within months, mostly personal "second brains" in Obsidian. It works now because general-purpose coding agents are good at reading and editing plain-text files, and Git gives you history and review for free. Team-wide knowledge bases are less common, and there are few public reports on how they work out. The main risk is the opposite of the old one: wikis used to go stale because nobody updated them, and now they can grow faster than anyone reads them.

## Level 1 — What it is (~30 min)

A team keeps its knowledge in linked plain-text files, and an agent does the upkeep: it reads new sources, updates the pages, and keeps the links consistent.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/agent-maintained-knowledge-bases) (~2 min) — note the warning: turning a personal wiki into an organization's knowledge base takes more than pointing an agent at a folder.
- [ ] **~25 min** · Read: [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (Andrej Karpathy, Apr 2026, ~7 min) — the idea file the blip links to. Its three layers are the core of the pattern: raw sources the agent never changes, a wiki the agent maintains, and a schema that tells the agent how. Read the gist itself, and skip the comments, which are mostly people promoting their own versions.

## Level 2 — Look at a working one (~30 min)

See the pattern in a real knowledge base, and think through what changes for a team.

- [ ] **~30 min** · **Do:** You're reading one. RadarWiki is an agent-maintained knowledge base: open its repository and map it onto Karpathy's three layers. The `Thoughtworks Radar` folder is the raw sources, `pages` is the wiki, and `skills` is the schema. Then imagine that ten people on a team share it. Write down three things that would go wrong first (for example, two people asking the agent to change the same page in different directions), and one rule you'd add to the schema for each.

Keeping a knowledge base from growing into unread AI-generated documentation is covered in [[AI-driven documentation sprawl]].

## Wrap-up

This plan covers the technique. Tools for it are covered in [[OpenWiki]] (documentation for a single repository) and [[Obsidian]] (the usual editor for the files).

## Review the blip

- [ ] **~5 min** · Re-read [Agent-maintained knowledge bases](https://www.thoughtworks.com/radar/techniques/agent-maintained-knowledge-bases) now that you know the topic.

## Related blips

- **[[AI-driven documentation sprawl]]**: without regular human effort, a knowledge base risks turning into it.
- **[[OpenWiki]]**: a narrower version of the pattern, for the documentation of one code repository.
- **[[Obsidian]]**: the knowledge base is often an Obsidian vault.
