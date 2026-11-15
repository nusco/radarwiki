---
title: Learning Wiki — Product Backlog
date: 2026-11-13
status: draft
---

# Learning Wiki — Product Backlog

## Vision

Learning Wiki is a personal wiki of learning plans for the methodical self-learner, stored as plain markdown on your own disk. You can use it to learn any topic you care about.
Unlike AI-generated courses, the plans in Learning Wiki point to material created by people: well-regarded courses, popular blog posts, sources you trust.

### Principles

1. **The agent writes the plan; people made the content.** Every linked resource is found through a real search and checked before it goes on the page. The agent never cites from memory.
2. **The files are the product; the editor only displays them.** Pages are plain markdown with frontmatter, headings, links and `- [ ]` checkboxes. Obsidian is the first editor supported, not a requirement.
3. **Skills only.** The whole system is one installable skill folder. An `init` workflow creates everything else.
4. **Works with any agent.** Claude Code is the reference agent, but nothing in the system depends on Claude-only features.
5. **Never lose progress.** Edits are surgical: changing one item never resets your checked boxes.
6. **The system is mostly skill files.** This makes for easy setup: install the skills into an empty folder, then say "set up a learning wiki here."


### My Backlog

**Current state of the topic**
NOTE: Change this to be more general, like an intro paragraph of generated text with the history of the topic (in the beginning of the plan, not the end), or something more generally useful. Otherwise, consider whether to make it a personal preference for TW Radar blips and move it to preferences.md.
As a learner, I want one generated paragraph that recaps the current state of the topic, to gain historical perspective.
- [ ] Comes after the last level of the learning plan.
- [ ] Shows the date it was written.
- [ ] Tells whatever the learned needs to know that isn't already clear from the activities: is this topic still relevant today? Did anything major happened to it, like an OS product going commercial, or a renaming? Was it superseded by another competing technology?

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
- [ ] If neither my request nor my user preferences settle the length, the agent asks with a few choices (e.g. 1 hour / half a day / weekend).
- [ ] The length is recorded in the page's frontmatter.

**LP-5 · MVP: Choose the pace**
As a learner, I want to set my pace, from "speeds through content" to "goes down every rabbit hole," so that the amount of material suits me.
- [ ] Pace changes how many items there are, how deep they go, and whether optional extras appear.
- [ ] Optional extras are visibly marked as optional.

**LP-6 · Next: Small generated content, clearly separated**
As a learner, I want short generated pieces (exercise briefs, one-line framing notes) where they help, so that the plan reads well, without being mistaken for real sources.
- [ ] Generated text is short and visually set apart from linked resources.
- [ ] Exercises state the goal and what "done" looks like. (Their time estimate is covered by "Timed activities".)

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
- [ ] I ask the agent (e.g. in a sidebar) to fill it in. It asks for length and pace only if my user preferences don't decide them.
- [ ] The finished plan replaces the stub at the same path, so existing links keep working.

**WL-3 · MVP: Fill all pending pages**
As a learner, I want to say "fill all pending plans," so that I can click around freely and generate everything later. This also works in editors that can't create stubs.
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

## Epic 3: Personalization

**User Preferences Generation**
As a learner, I want to generate my user preferences through an interview
- [ ] `init` creates it through a short interview, and I can edit it by hand.

**PE-2 · MVP: Start from the Technology Radar blip**
As a learner, I want the first Level 1 activity to be the topic's Thoughtworks Technology Radar blip, when one exists, so that every plan starts my way.
- [ ] The agent detects whether the topic has a blip and links to it.
- [ ] If there's no blip, the plan says so in one line.

**PE-4 · Next: Rituals in general**
As a learner, I want to define my own rituals ("always start with X," "always end with a build exercise"), so that the blip habit is one example of a general feature rather than hard-coded.

---

## Epic 4: Progress and maintenance

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

## Epic 5: Setup and packaging

**SP-1 · MVP: One umbrella skill**
As a sharer, I want the whole system packaged as one skill folder, so that it installs and updates as a unit.
- [ ] `learning-wiki/SKILL.md` routes requests to workflow files: `init`, `plan`, `tweak`, `refresh`, `fill-pending`.
- [ ] Shared material lives inside the same folder: `reference/` (page format, link rules, source quality), `scripts/` (link checker), `assets/` (templates), `harnesses/` (one file per agent).
-  Structure: One skill folder, installed with `npx skills add`. Everything else is created by `init`, and there's nothing Claude-specific in it except one file in `harnesses/`.

    ```
    learning-wiki/
    ├── SKILL.md            # entry point: routes to init / plan / tweak / refresh
    ├── init.md, plan.md, tweak.md, refresh.md
    ├── reference/          # page format, link rules, source quality
    ├── harnesses/          # claude-code.md, pi.md, …
    ├── scripts/            # check-links.py
    └── assets/             # page template, profile skeleton, .obsidian/, settings files
    ```

**SP-2 · MVP: One-command install**
As a sharer, I want people to install it with `npx skills add <repo>`, so that it works for whatever agent they use.
Notes:
    - Don't let the model write config from scratch. Put the files `init` needs inside the skill folder (the Agent Skills format has an `assets/` directory for this): the page template, a profile skeleton, the `.obsidian/` config, and a per-harness permissions file. `init` then copies the files and fills in only the profile from its interview. Copying is deterministic, which matters a lot for weaker models. An Ollama model inventing a `settings.json` from memory is a bug waiting to happen.
    - Harness-specific knowledge still has to live somewhere. "Generate whatever reduces friction" assumes the agent knows its own harness's config format. Claude knows Claude Code's, but a local model in Pi may not know Pi's. Keep a small reference file per known harness (`harnesses/claude-code.md`, `harnesses/pi.md`) holding the config snippet and where it goes, and have `init` read only the one that applies. For harnesses you don't know, the fallback is: "tell the user which permissions to grant, and don't guess." Adding support for a new harness then means adding one file.

**Scope the skill descriptions.**
If someone installs the skills globally instead of per folder, a vague `plan` skill could trigger while they're writing code. Word every description to apply only "inside a learning wiki (a folder containing `_profile.md`).

**SP-3 · MVP: `init` in an empty folder**
As a learner, I want to run `init` in an empty folder and end up with a working wiki, so that setup takes minutes.
- [ ] A short interview creates the user preferences, a README and the page template.
- [ ] Files are copied from `assets/`, not generated from scratch, so the result is the same every time, even with weaker models.
- Notes:
    - Make self-granted permissions visible. An agent writing its own permission rules is exactly what a careful user, and a careful harness, should see. Claude Code will ask before editing its settings file, and the change may only take effect after a restart. Have `init` show what it's about to allow (for example, "fetch any web page, run the link checker") and ask for confirmation. It's a one-time prompt, and it's the right one.
    - Some Obsidian steps can't be done from inside the folder. `init` can write `.obsidian/` config, and with bash it could even download plugin files from GitHub releases. But the user still has to open the folder as a vault and turn on community plugins, and Obsidian may need a reload to pick up the changes. So `init` should end with a short checklist for the user, and anything it downloads into the vault should be shown, since that's third-party code.
    - Make `init` safe to rerun. It should never overwrite the profile or existing pages, so that "run init again" also works as repair and upgrade.


**SP-4 · MVP: Safe to rerun**
As a learner, I want to rerun `init` to repair or upgrade my wiki, so that I can update the system safely.
- [ ] It never overwrites my user preferences or my pages.

**SP-5 · MVP: Setup for convenience settings**
As a learner, I want `init` to configure my agent's permissions (for example, allowing web page fetches), so that checking links doesn't flood me with permission prompts.
- [ ] Uses the matching `harnesses/<agent>.md`.
- [ ] Shows what it will allow and asks before writing anything.
- [ ] For an agent it doesn't know, it tells me which permissions to grant instead of guessing.
- [ ] Never writes configuration that changes behavior (rules, hooks), only settings that remove friction.

**SP-6 · MVP: Obsidian setup**
As a learner, I want `init` to prepare the folder for Obsidian, so that clicking a missing page and checking boxes work immediately.
- [ ] Writes the `.obsidian/` config and the Templater stub template.
- [ ] Shows me any plugin code it downloads before installing it.
- [ ] Ends with a checklist of manual steps: open the folder as a vault, enable community plugins, reload.

**SP-7 · Next: Scoped skill descriptions**
As a learner, I want the skill to activate only inside a learning wiki (a folder containing `preferences.md`), so that a global install doesn't trigger it while I'm coding.

**SP-8 · Later: Optional Claude Code plugin**
As a sharer, I want an optional Claude Code plugin around the skill, for hooks and automatic dependency installs, without making the core depend on it.

*Development note:* while building, keep the skill in `WIKI_FOLDER/.agents/skills/` and symlink `.claude/skills` to it, so Pi and Codex pick it up too. If Windows matters, keep `.claude/skills` as the real folder instead.

---

## Epic 6: Portability

**PO-1 · MVP: Portable pages**
As an other-agent or other-editor user, I want pages written in portable markdown, so that they read correctly anywhere.
- [ ] Only frontmatter, headings, links, lists and checkboxes.
- [ ] No Dataview queries, Bases files or `![[embeds]]` inside plan pages.

**PO-2 · MVP: Agent-neutral skill text**
As an other-agent user, I want the skill to describe actions rather than one agent's tool names, so that it works in my agent.
- [ ] "Fetch each URL and confirm it loads," not "use WebFetch."
- [ ] Skill frontmatter contains only `name` and `description`.

**PO-3 · Next: Pi + Ollama**
As a Pi user, I want Learning Wiki to work with my Ollama model, so that I can use local or open models.
- [ ] `harnesses/pi.md` documents web tools (e.g. `ollama launch pi`, which installs Ollama's Pi web search package) and the context-window setting (64K or more).
- [ ] Tested end to end with an Ollama cloud model.
- [ ] The README sets expectations for small local models.

**PO-4 · Next: Link style setting**
As a user of a plain editor, I want to choose standard markdown links instead of wikilinks, so that links work in my editor.
- [ ] The style is set in the user preferences. The agent writes whichever is chosen. Files use a flat layout where filename equals title.

**PO-5 · Next: Agents without web access**
As an other-agent user, I want an agent that can't browse to say so rather than make things up, so that I can trust what's on the page.
- [ ] Without web access, plans either aren't generated or have every link marked unverified. Never invented links.

**PO-6 · Later: Other editors**
As a VS Code user, I want a Foam setup option, so that I get similar click-to-create behavior. Plain editors rely on `fill-pending` (WL-3).

**PO-7 · Later: Agent-wide rules file**
As a sharer, I want an optional `AGENTS.md` for rules that should apply even when no skill is active, plus a one-line `CLAUDE.md` containing `@AGENTS.md` so that Claude Code reads it too.

---

## Prior art, risks and open questions

### Read before building

- **gupsammy's `learn-anything` skill**: how it researches and vets sources, and its 80/20 plan shape. The original repo is unreachable; there's a copy in `majiayu000/claude-skill-registry` and the full text on Skills.lc.
- **glebis's `learning-vault` skill**: setting up an Obsidian vault from inside a skill, including a bundled plugin, plus self-assessment.
- **Karpathy's "LLM Wiki" pattern**: the same Obsidian + agent architecture. Its "lint" step is close to `refresh`.
- **Metacademy**: prerequisite graph and time estimates (for LP-7).
- **ChenChenyaqi's `learn-anything`**: one adapter per agent (compare `harnesses/`).
- **setchy/thoughtworks-tech-radar-volumes**: blip history data (for PE-2 and PE-3).
- **Wonderland (Obsidian plugin, archived)**: the closest existing click-a-missing-link experience.

### Risks

| Risk | Mitigation |
|---|---|
| Invented or dead links (the top risk) | LP-2, LP-3, PO-5. Instruct explicitly: "only use resources you actually found." |
| Weak models skip verification or rewrite whole pages | Required link-check script (LP-3), PM-3 in every workflow, files copied from templates (SP-3) |
| Context too small for fetched pages | Document a context window of 64K or more in `harnesses/` (PO-3) |
| Duplicate topic pages | WL-4 |
| Lost progress | PM-2, PM-3 |
| Link rot over time | PM-4, PM-5, PM-7 |

### Open questions

- Flat folder or subfolders? A flat layout is recommended for portability (PO-4).
- What happens to finished plans: archive them, or leave them in place with `status: done`?
- How to detect a Radar blip: from the dataset, or by web search?
- Defaults when the user preferences don't specify length or pace.
- How far to take rituals beyond the Radar blip (PE-4).
- Final name. Candidates: Redlink, Docent, Pointers. "Learning Wiki" for now.
