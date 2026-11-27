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
2. **The pages are the deliverable.** Pages are plain markdown with headings, links and `- [ ]` checkboxes, which I read in Obsidian.
3. **Every plan starts from a Radar blip.** The system is built for the Radar, and generalizing it can wait until there's a real need. The source of truth is the Radar website (its [search pages](https://www.thoughtworks.com/radar/search) and blip pages), not the PDFs. (The two sources can be inconsistent.)
4. **Mostly skills.** The system is skill files, plus a script that downloads the Radar.
5. **Never lose progress.** Edits are surgical: changing one item never resets your checked boxes.

### Note

Contact MV about the inconsistencies I'm finding between the Radar PDFs and the search system. I compared the first seven Radars (2010–2012) with the search system, without checking rings, and I also checked MCP in the April 2025 PDF. So there may be more. I found:

- MCP: in the April 2025 PDF (Platforms, Assess, blip 40), but missing from its blip history.
- RDF triple stores: in the April 2010 PDF (blip 23), but missing from its blip history.
- RDFa: shown for April 2010, though the PDF doesn't list it as a blip.
- RDF & SPARQL: in the January 2010 PDF, but shown as RDFa on the site.

Are they interested in fixing these, or should we live with them?

### My Backlog

**Manage Long Page Names**

As a Learner
I want page file names to stay within the path limits of common OSes
So that the wiki works wherever I open it.

- [ ] Windows limits paths to 260 characters by default. The longest blip name so far has 65 characters, so this isn't a problem yet. Decide whether and how to shorten names that would push a path past the limit.

**Find Related Blips When the Radar Lists None**

As a Learner
I want a learning plan to list related blips even when its blip's page lists none
So that older plans are connected to the rest of the wiki too.

- [ ] Older blip pages have no "Related blips" section. None of the six smoke-test blips in "Manage Illegal Filename Characters in Blips" had one, from F# (2010) to TCR (November 2025). The `learning-plan` skill currently leaves the section out in that case.
- [ ] To be decided: how the Wikimaster finds related blips on its own (for example, blips that the blip's text links to or mentions, blips in the same edition on the same topic, or later blips that replaced it), and whether the page says that the list comes from the Wikimaster rather than from Thoughtworks.
- [ ] Note: find out when the Radar started listing related blips, to tell how many blips this affects.

**Visualize as Obsidian graph**
As a Learner
I want to visualize the Radar Wiki as a graph in Obsidian
So that I can plan and track my progress.
- [ ] The repo contains an Obsidian graph configuration that shows all the `.md` pages in the `pages` folder.
- [ ] Pages that are tagged as #done show up green. Pages tagged as #wip show up orange. Pages with any other tag (including #undone) are grey.
- [ ] The README explains how to manage the graph and shows an image example.
- [ ] The graph links show up as undirected.
- [ ] The graph hides unresolved links (links to pages that don't exist yet).
- [ ] The graph parameters result in a graph that is relatively readable even with a lot of nodes.
- [ ] TO DECIDE: How do we avoid cluttering diffs? ( current best option: an `obsidian-integration` folder with instructions, a brief one-line mention in the `README`)
- [ ] TO DECIDE: Any other comments from the agent worth discussing?

**Generate Page from Template**

_Note: Some criteria here are obsolete after the implementation of "Organize the Know-how as Skills". We need to review it and complete it. (In particular, we must review the template and rules and update the existing pages.)_

As a learner, I want the Wiki pages to be generated from a template, so that I can easily change their style and get consistent results.
- [ ] The wiki should have a place to put templates. This place should contain a template for a page that describes the general structure and the content of each section.
- [ ] The natural language instructions to generate plans in the SKILL.md should move to the template so that they're easy to read and change for a human user, and harder to miss for an agent maintainer.
- [ ] The split: the template says what a page looks like and contains (metadata, sections, levels, labels, time estimates, preferences). The skill keeps the process: finding the blip, keeping up with the Radar, maintaining plans, wiki rules, and research integrity (live search, fetch every page, human-made content only).
- [ ] After manual review by Paolo, the existing plans should be re-validated against the template and, if necessary, changed.
- [ ] Templates live in a `templates/` folder in the vault. Only the agent uses them: no Obsidian templating (no Templates or Templater plugin, no Obsidian-generated skeletons).
- [ ] The instructions in the template are visible (for example, callouts), not hidden comments, so I can read them and edit them to personalize the wiki's style.
- [ ] All the learning preferences (default length, pace, trusted and avoided sources, link style) move to the template, too. We'll learn over time which pieces sit better in the skill.
- [ ] The template also covers the `*Assumption: …*` and `*Time budget: …*` lines (where they go and how they look), and a **Status** metadata field with one of `#undone`, `#wip` or `#done`. The agent writes `#undone` in new plans and never changes the field afterwards: only I do, on my study branch.
- [ ] When re-validating, completed plans follow the existing rule: ask me before any change, structural or content. In-progress plans keep their ticks.
- [ ] Changing the template doesn't automatically update the existing pages. I ask for that when I want it.
- [ ] Obsidian's core Templates plugin is disabled.
- [ ] The README's "Structure" section mentions the template.

**Update Plan for Returning Blip**

When the wiki maintainer updates the wiki to a new edition of the Radar, if there are returning blips, it might pay to try and refresh the learning plans for those blips. (The rationale is that if a blip is returning, then it's likely important, and there might be fresher, more relevant and higher quality material out there for it). A good test bed is _Toxic Flow Analysis_ in the Nov 2026 Radar.

**Refresh Underexplained Blip**

Some blips in the Radar can be new enough that the maintainer cannot find good material out there. In the Nov 2026 Radar, that happened for Semantic review of AI-edited prose, AI-accelerated shadow IT, AI-driven documentation sprawl, Agent pipeline responsibility and the hands-on half of Anchoring coding agents to a reference application. Design a mechanism to return to these "underexplained" blips later, when the Internet might provide material to flesh out the blip's learning plan.

**Retry Failed Pages**

It happened with felonybench and PluginEval. Add instructions for retrying.
Related: MITRE ATLAS generates pages on the fly, and the agent doesn't run JavaScript, so it comes out nearly empty. Find a solution. Probably: "This session has a Playwright browser available, from the Vaadin plugin. It's a real headless browser: it runs JavaScript, can wait for a page to finish loading, and can take a snapshot of the page. I didn't use it, and I should have tried it before passing these back to you."

**Curate Updated Blips**
As a learner, I want updated Blips to be consistent in the Wiki, so that I avoid duplicated pages and missing information.
- [ ] If a blip appears in different editions of the Radar, recap its history when you write its learning plan, telling me in which Radars it appeared and in which rings, according to the Radar website. For example, it's interesting to me that a blip moved from "Trial" to "Adopt".
- [ ] Hold and Caution are the same ring, renamed in April 2026. In a blip's history, keep the name each edition used, but don't present a change from Hold to Caution as a move.
- [ ] If the blip of an existing learning plan is renamed, use the latest name for the learning plan and in other Wiki pages that refer to it, but also add a note about the renaming. (Examples of this kind of change: `aws-bedrock-agentcore` became `amazon-bedrock-agentcore`, and `local-coding-assistants` became `local-coding-models`.)
- [ ] One special case of renaming: if the blip of an existing learning plan is renamed in capitalization only, just rename it in the learning plan (both in the file name and the content) and other Wiki pages that refer to it, but don't worry about adding a note. This is probably a typo that was later fixed.
- [ ] If the blip of an existing learning plan is moved to another quadrant, just tell me in the appropriate metadata section in the learning plan. (Example of this kind of change: `litellm` moved from `languages-and-frameworks` to `platforms`.)
- [ ] A new learning plan uses the blip's current name and quadrant from the Radar website, with no note about changes that happened before the plan existed.
- [ ] The edition files in the `Thoughtworks Radar` folder are not regenerated or corrected to match the website.
- [ ] Edition lists already in existing learning plans stay as they are, even if the website disagrees with them (for example, the plans that list MCP as "Apr 2025, Nov 2025"). New or updated text follows the website.
- [ ] Blips that the Radar lists as separate stay separate, even if they seem to be the same topic (see "Manage aliased blips").

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
  - An old alias can also appear in a blip's "Related blips". For example, the MCP blip lists MCP-Scan, which its page currently links as `[[Agent Scan|MCP-Scan]]`.

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

**Visualize progress in graph**
As a learner I want to visualize the learning plans in the Obsidian grap with different color to see which ones I completed.

**Verify links**
As a learner, I want every link checked before it lands on the page, so that I never hit an invented or dead link.
- [ ] The agent fetches each URL and confirms it loads and matches its description.
- [ ] A mechanical link-check script runs as a required final step, independent of the model.
- [ ] Any link that can't be verified is removed or clearly marked as unverified.

**Find Exact Timing in Audio/Video Sources**

Wikimaster: "I didn't verify the exact start and end times of the podcast excerpts in Grilling and Production-aware coding agents."
Then, when asked to elaborate:
Wikimaster: "I can't listen to audio. What I can do is check timings from text:
- Chapter lists. I had the Pragmatic Engineer timestamps but didn't use the one after "The wayfinder skill" to find where the excerpt ends. That's a plain miss on my part.
- Episode length. Audio players and YouTube pages show it once the page renders, which Playwright can do.
- Transcripts. Many podcasts publish one, and YouTube has captions. With a transcript I can confirm where a topic starts and stops, not just guess from chapter titles.
  
  The one case I can't check is an episode with no chapters and no transcript. There I could only give the total length."

## Epic: Wiki linking
_TODO: generated. select and roll into the general backlog_

First, check out how LLM Wiki does it:
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
https://llm-wiki.net/

Note: potential bug. When you click on a link named `AGENTS.md` for a page that doesn't exist, Obsidian creates a page named `AGENTS` in a file named `AGENTS.md`. It should be a file named `AGENTS.md.md`.

**WL-1 · MVP: Link the first mention**
As a learner, I want the first mention of each related topic to be a link, even if that topic has no page yet, so that the wiki grows as I explore.

**WL-2 · MVP: Clicking a missing page gets a plan**
As a learner, I want to click a link to a topic that has no plan and get one, so that I can follow my curiosity.
- [ ] In Obsidian, clicking the link creates a stub (`status: pending`).
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

## Epic: Progress and maintenance
_TODO: generated. select and roll into the general backlog_

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
