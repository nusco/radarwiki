---
title: RadarWiki — Product Backlog
date: 2026-11-13
status: draft
---

### Read before building

- **gupsammy's `learn-anything` skill**: how it researches and vets sources, and its 80/20 plan shape. The original repo is unreachable. Find it [here](https://github.com/majiayu000/claude-skill-registry-data/blob/a21980a5b576646393ed574f158d7dd92fae4c3f/personal-development/learn-anything-gupsammy-claude-setup-2/SKILL.md).
- **Karpathy's "LLM Wiki" pattern**: the same Obsidian + agent architecture. Its "lint" step is close to `refresh`.
- **Metacademy**: prerequisite graph and time estimates (for LP-7).
- **setchy/thoughtworks-tech-radar-volumes**: blip history data (for PE-2 and PE-3).
- **Wonderland (Obsidian plugin, archived)**: the closest existing click-a-missing-link experience.

# RadarWiki — Product Backlog

## Vision

RadarWiki is a personal wiki of learning plans for Thoughtworks Technology Radar blips, stored as plain markdown on disk.
Unlike AI-generated courses, the plans in RadarWiki point to material created by people: well-regarded courses, popular blog posts, sources you trust.

### Principles

1. **The agent writes the plan; people made the content.** Every linked resource is found through a real search and checked before it goes on the page. The agent never cites from memory.
2. **The files are the product; the editor only displays them.** Pages are plain markdown with headings, links and `- [ ]` checkboxes, which I read in Obsidian.
3. **Every plan starts from a Radar blip.** The system is built for the Radar, and generalizing it can wait until there's a real need.
4. **Mostly skills.** The system is skill files, plus a script that downloads the Radar.
5. **Never lose progress.** Edits are surgical: changing one item never resets your checked boxes.


### My Backlog

**Curate Updated Blips**
As a learner, I want updated Blips to be consistent in the Wiki, so that I avoid duplicated pages and missing information.
- [ ] If a blip appears in different editions of the Radar, recap its history when you write its learning plan, telling me in which Radars it appeared and in which rings. For example, it's interesting to me that a blip moved from "Trial" to "Adopt".
- [ ] Hold and Caution are the same ring, renamed in April 2026. In a blip's history, keep the name each edition used, but don't present a change from Hold to Caution as a move.
- [ ] If a blip was renamed, use the latest name for the learning plan and in other Wiki pages that refer to it, but also add a note about the renaming. (This happened at least twice: when `aws-bedrock-agentcore` was renamed to `amazon-bedrock-agentcore`, and when `local-coding-assistants` was renamed `local-coding-models`. This rule applies to these two cases from the past, and any future case as well.)
- [ ] One special case of renaming: if a blip was renamed in capitalization only, just rename it in the learning plan (both in the file name and the content) and other Wiki pages that refer to it, but don't worry about adding a note. This is probably a typo that was later fixed.
- [ ] If a blip was moved to another quadrant, just tell me in the appropriate metadata section in the learning plan. (This happened at least once, when `litellm` moved from `languages-and-frameworks` to `platforms`. Again, this rule applies to these two cases from the past, and any future case as well.)
- [ ] Blips that the Radar lists as separate stay separate, even if they seem to be the same topic (see "Manage aliased blips").

**Keep up to date with the TW Radar**
As a learner, I want the Wiki to track the latest editions, so that I don't miss updated information.
- [ ] Whenever the system is asked to update anything (for example, to revise a learning plan), it also checks that the `Thoughtworks Radar` folder contains all editions of the Radar, including the latest ones. The radar is on `https://www.thoughtworks.com/radar/`.
- [ ] If any editions of the radar are missing, the system creates files for them. See `thoughtworks-radar-2010-april` for an example of the naming convention and structure of these files.
- [ ] The system does not create learning plans for these new blips, unless specifically asked to. The Wiki pages are still created on an as-needed basis.
- [ ] If the new Radar edition updates a previous blip that already had a matching learning plan, then the system does update that learning plan. One such example is the "Toxic flow analysis" blip, that moved  from Assess to Trial in the latest Radar (November 2026). So its metadata, its "Current state" paragraph, and the edition dates in the plans that link to it need updating.

**Manage aliased blips**
As a learner, I want to tell the maintainer that two blips are aliases of each other, so that I can resolve the redundancy (_somehow_).
- [ ] We should decide how discovery (when possible), notification and the fix happen. The canonical case is https://www.thoughtworks.com/radar/tools/mcp-scan that became https://www.thoughtworks.com/radar/tools/agent-scan, so two separate blips (both still living) but one actual topic. Arguably, the old name's plan should point to the new name's plan, or some other wiki-ish solution.
- [ ] We should decide what happens to the older blip's learning plan: it could not exist, exist and point to the newer blip's plan, or be an alias linked to it. The canonical case is https://www.thoughtworks.com/radar/tools/mcp-scan, which became https://www.thoughtworks.com/radar/tools/agent-scan: two separate blips, both still live, but one actual topic.
- [ ] Notes for refinement:
  - The Radar doesn't always reveal an alias. Nothing on the MCP-Scan or Agent Scan pages connects them. That link came from researching the tool.
  - Some blips do mention a former name, which could help discovery, but each case needs judgment. Candidates:

    | Earlier blip | Later blip | Text in the later blip | Same topic? |
    |---|---|---|---|
    | Azure Cognitive Search | Azure AI Search | "formerly known as Cognitive Search" | Yes |
    | Snowplow Analytics & Piwik | Matomo | "formerly Piwik" | Partly: the old blip covered two tools |
    | Presto | Trino | "previously known as PrestoSQL" | Unclear: needs judgment, because Presto and PrestoSQL aren't quite the same thing |

  - Until this is done, a request for a plan on the older blip creates a separate plan.
  - The `[[Agent Scan|MCP-Scan]]` link example in `SKILL.md` may need revisiting.

**Manage homonymous blips**

As a learner, I want to distinguish different blips that have the same name, to avoid confusing different topics.
- [ ] Examples:
          https://www.thoughtworks.com/radar/search?q=gremlin
          https://www.thoughtworks.com/radar/search?q=zap
- [ ] To be decided. We should probably disambiguate the blip name in the file name and any list of multiple blips, adding the quadrant name:
        - "Gremlin (Tools)"
        - "Gremlin (Languages & Frameworks)"
    or, shorter:
        - "Gremlin (tool)"
        - "Gremlin (language)"
- [ ] Also deal with the case where blips differ only by capitalization. "ZAP" and "Zap" count as homonyms. On a Mac, ZAP.md and Zap.md would normally be the same file. They also mustn't be mistaken for the capitalization rename in "Curate Updated Blips", which is about one blip whose name changed.
- [ ] An ambiguous request should prompt a question. If you ask for "a plan on Gremlin", the maintainer should ask which one. The skill now says that a blip under the name you used is the blip, which doesn't settle it when there are two.
- [ ] When to disambiguate. I'd add the quadrant from the first plan, even if the other blip has no plan yet, so the file never needs renaming later.
- [ ] Quadrants can change. If a blip moves, as litellm did, its file name goes stale. A short description, like "Gremlin (chaos engineering)", would avoid that, so it's worth keeping as an alternative.
- [ ] So, notes for refinement:
  - ZAP (OWASP security proxy) and Zap (Go logging library) differ only by capitalization, so they collide as file names on case-insensitive file systems. They aren't a capitalization rename: those are one blip, and these are two.
  - If a request is ambiguous, like "a plan on Gremlin", the maintainer asks which blip I mean.
  - Decide whether to disambiguate from the first plan, even if the other blip has no plan yet.
  - A blip can change quadrant, which would make a quadrant-based name stale. A short description of the topic is an alternative.
  - "(language)" doesn't work as a short label for every blip: Zap is a Go logging library, so "Zap (language)" would be wrong. "(framework)" or "(library)" would fit it better. If the short form has to be chosen per blip, it's close to the short description alternative.
  - `tools/gremlin` is a SaaS tool for chaos experiments. `languages-and-frameworks/gremlin` has no description on its page, and is probably the graph query language.

---

From here on: machine-generated backlog to fish from later.

## Epic 1: Learning plans

**LP-3 · MVP: Verified links**
As a learner, I want every link checked before it lands on the page, so that I never hit an invented or dead link.
- [ ] The agent fetches each URL and confirms it loads and matches its description.
- [ ] A mechanical link-check script runs as a required final step, independent of the model.
- [ ] Any link that can't be verified is removed or clearly marked as unverified.

**LP-4 · MVP: Choose the length**
As a learner, I want to choose how long a plan takes (from 30 minutes to a weekend), so that it fits my time.
- [ ] If neither my request nor my learning preferences settle the length, the agent asks with a few choices (e.g. 1 hour / half a day / weekend).
- [ ] The length is recorded in the page's frontmatter.

**LP-7 · Later: Prerequisites**
As a learner, I want a plan to name its prerequisite topics as links, so that I can fill gaps first. (This borrows Metacademy's prerequisite-graph idea.)

---

## Epic 2: Wiki linking

First, check out how LLM Wiki does it:
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
https://llm-wiki.net/

**WL-1 · MVP: Link the first mention**
As a learner, I want the first mention of each related topic to be a link, even if that topic has no page yet, so that the wiki grows as I explore.

**WL-2 · MVP: Clicking a missing page gets a plan**
As a learner, I want to click a link to a topic that has no plan and get one, so that I can follow my curiosity.
- [ ] In Obsidian, clicking the link creates a stub (`status: pending`) using a Templater template.
- [ ] I ask the agent (e.g. in a sidebar) to fill it in. It asks for length and pace only if my learning preferences don't decide them.
- [ ] The finished plan replaces the stub at the same path, so existing links keep working.

**WL-3 · MVP: Fill all pending pages**
As a learner, I want to say "fill all pending plans," so that I can click around freely and generate everything later.
- [ ] The agent finds empty or pending stubs and links to pages that don't exist yet.
- [ ] It lists them and asks before generating more than a few.

**WL-4 · MVP: No duplicate topics**
As a learner, I want one page per topic, so that `[[Claude Code]]` and `[[claude-code]]` don't become two different pages.
- [ ] Each page has a canonical title, with aliases listed in its frontmatter.
- [ ] Before writing a link, the agent checks existing titles and aliases.

**WL-5 · Later: One-click generation**
As a learner, I want clicking a missing page to start generation directly, with a quick length/pace menu, so that I don't need to switch to the agent.
- [ ] Possible approach: a Templater script shows the menu, then runs the agent headless. The page fills in after a delay.

---

## Epic 3: Progress and maintenance

**PM-2 · MVP: Tweak one item**
As a learner, I want to ask the agent to change a single item, for example an exercise I can't complete, so that I'm not stuck.
- [ ] The agent can make the item easier, change it, or replace it with an alternative.
- [ ] Only that item changes. Every checked box elsewhere stays as it was.

**PM-3 · MVP: Edits never rewrite whole pages**
As a learner, I want the agent never to regenerate a whole page when I ask for a change, so that my progress is never lost.
- [ ] The rule appears in every workflow that edits pages, not only in agent-wide instructions.

**PM-4 · Next: Refresh a plan**
As a learner, I want to refresh existing plans, for example when a link breaks, so that old plans stay usable.
- [ ] Re-checks every link and replaces dead ones with equivalent human-made sources.
- [ ] Updates the "current state" paragraph and the `last-verified` date in the frontmatter.
- [ ] Keeps all progress.

**PM-5 · Next: Find dead links across the wiki**
As a learner, I want a link checker that scans the whole wiki without using the model, so that I know which plans need a refresh.

**PM-6 · Later: Dashboard**
As a learner, I want an overview of plans in progress, completion percentages, pending stubs and stale pages, so that I can decide what to study next.
- [ ] Kept in a separate, Obsidian-only file (Bases or Dataview), so plan pages stay portable.

**PM-7 · Later: Scheduled refresh**
As a learner, I want stale plans re-checked automatically (e.g. monthly), so that maintenance happens without my asking.

---

## Prior art, risks and open questions

### Risks

| Risk | Mitigation |
|---|---|
| Invented or dead links (the top risk) | LP-2, LP-3. Instruct explicitly: "only use resources you actually found." |
| Weak models skip verification or rewrite whole pages | Required link-check script (LP-3), PM-3 in every workflow |
| Duplicate topic pages | WL-4 |
| Lost progress | PM-2, PM-3 |
| Link rot over time | PM-4, PM-5, PM-7 |

### Open questions

- Flat folder or subfolders?
- What happens to finished plans: archive them, or leave them in place with `status: done`?
- How to detect a Radar blip: from the dataset, or by web search?
- ~~Final name.~~ Decided: "RadarWiki".
