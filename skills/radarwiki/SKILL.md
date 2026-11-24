---
name: radarwiki
description: How the RadarWiki works as a whole, whatever the page: the folder layout, keeping up with the Thoughtworks Technology Radar, naming and linking pages, the wiki rules, maintaining existing pages, and research integrity. Use for any work on the wiki, such as updating the Radar or changing existing pages, and together with the skill for the type of page you're writing, such as learning-plan.
---

# RadarWiki

## Layout

- `skills/` holds all the know-how about the wiki: this skill, and one skill for each type of page, with that page's template inside its folder. The only page type so far is the learning plan, in the `learning-plan` skill. Agents find the skills through `.claude/skills`, a link to this folder.
- `pages/` holds the wiki pages, one Markdown file per page.
- `Thoughtworks Radar/` holds one file per Radar edition, listing its blips, and the script that downloads them.

## Naming and links

- The learner opens pages as notes in Obsidian. Name each file after its topic, like `Model Context Protocol (MCP).md`, and don't add a Markdown level-1 title inside (like `# MCP`): Obsidian shows the file name as the title.
- Link between pages with Obsidian links, like `[[Agent Skills]]`, or `[[Agent Scan|MCP-Scan]]` when a page covers a topic under another name.
- Use standard Markdown links for everything else, such as resources and blips.

## Wiki rules

- Pages must work well together. Before you write a page, look at the existing pages in the `pages` folder. If the new topic is related to one of them, link to it. Assume what the earlier page covers instead of repeating it, avoid reusing its resources, and build the exercises on the earlier page's exercises when that makes sense. Keep one page per topic: two tools that your sources list separately get two pages.
- Treat the pages as a wiki: link material, don't duplicate it. When two topics overlap, put each resource, exercise or explanation in the one page where it fits best, usually the page whose topic is about it. In the other page, add a short explicit pointer that says what it will find there (for example, "Mapping the trifecta across your whole setup is covered in [[Toxic flow analysis for AI]]"). Make an exception only when removing the material would leave a big hole in a topic. In that case, keep a brief version (one resource or a one-line recap) and link to the full treatment.
  - This works in both directions. When you write a new page, check whether existing pages already cover its material. If one does, move that material into the new page, even if the learner has already ticked it off: move it as it is, still ticked, so their progress stays. Replace the moved material with a pointer, and fix any prerequisites that no longer hold.
  - If a related topic has no page yet, an existing page can cover it briefly. When that topic gets its own page, apply the rule above.
- **Structural links go to pages, not sources.** A structural link is one that helps the learner find their way between topics, such as a list of related topics, a series list, or an entry in an index file (for example, a hypothetical `Index.md` listing all topics). When a topic has a page, make that link a link to the page, and don't add a second link to the topic's blip next to it. Link to the blip itself only when the learner needs to read it, such as in the page's metadata or in an activity that asks the learner to read the blip. A topic that has no page yet keeps its blip link. When you write a new page, replace the structural links to its blip in the other pages and in any index file, such as `Index.md`, if one exists, with links to the new page.

## Research integrity

These rules hold for every page, whatever a page skill or its template says:

- **Find every resource with a live web search, never from memory.** Even when you remember a good resource, search for it. Then fetch each page to confirm that it loads and contains what the page says about it.
- **Use only resources that look human-created.** This is a requirement, not a preference: never use content that looks LLM-generated, slop, content farms or SEO filler, even when it looks otherwise good. Some docs, including official ones, read as generated: verbose, overly detailed, meandering. Skip them in favor of a terse, well-structured narrative written by a person.
- Always point to existing human-written or human-curated content instead of writing your own explanations or walkthroughs.

## Keeping up with the Radar

Before you write or revise a page, check that the `Thoughtworks Radar` folder has the latest edition. The folder has one file per edition, numbered by volume, like `034-thoughtworks-radar-2026-april.md`. Run the download script from the folder, because it writes there.

1. **Check the date.** If the newest edition in the folder is less than 25 weeks old, go on with the request.
2. **Check the website.** Otherwise, run `python3 download-script/radar_to_todo.py < /dev/null`. It reads the [Radar archive](https://www.thoughtworks.com/radar/archive) and lists the published volumes, without downloading anything. If none is newer than the folder, go on with the request. While a Radar is late, you'll check on every request, and that's fine.
3. **Ask first.** If there are new editions, tell the learner which ones, and which existing pages they would change: read the blip page of each page, and look for the new editions in its history. Then ask before you download anything or change any page. If the learner says no, go on with the request.
4. **Download the new editions.** Run `printf '<volumes>\n' | python3 download-script/radar_to_todo.py`, with only the new volumes, like `35` or `35-36`. Never select a volume that's already in the folder: its file holds the learner's ticks. The script reads every blip page slowly, so the site doesn't block it. It can take an hour, so let it finish.
5. **Update the README.** Set its sentence on the edition to the newest one, like "Up to date with the Thoughtworks Radar, November 2026 (volume 35)."
6. **Update the pages.** For each page whose blip appears in a new edition, even in the same ring, update everything that depends on the edition: **Radar edition** and **Ring** in the metadata, the current state paragraph and its date, and text that counts or names editions (like "read both versions"). This applies to completed pages too: these changes add no tasks and reset no progress. Leave alone blips that dropped out of the new edition, and don't write pages for new blips unless the learner asks.
7. Go on with the request.

## Maintaining existing pages

- **Update existing pages when needed.** Whenever a change in the system is inconsistent with the existing pages (for example, because the user asked for changes that lead you to update a skill), update the existing pages in the `pages` folder to follow the new version, without waiting for the learner to ask. If an update could be destructive, such as losing progress on a page the learner has started, explain the problem plainly and ask before you make it. Describe the change in natural language, not as a code diff or another proposal that's hard to judge at a glance.

- **Except for changes to a page's style.** The learner edits the page skills and their templates to change the style of the wiki, and there can be hundreds of pages. So a change to a page skill or a template doesn't update the existing pages by itself: update them only when the learner asks. The rules above and below still apply when you do.

- **Keep in-progress pages stable.** When you change a page where some items are already ticked off, preserve the ticked items. Never untick an item without asking the learner. If a change would substantially alter a ticked item, describe the issue to the learner and let them decide.

- **Leave completed pages alone.** A page where every item is ticked off, ignoring optional items (such as "If you have extra time" in a learning plan), is done: don't update it automatically, and don't add new items that would return it to "in progress". This includes the changes that the wiki rules above would make, such as moving material out of the page or updating its structural links. If you think a completed page really needs a change, ask the learner specifically. The one exception is the update for a new Radar edition, in [Keeping up with the Radar](#keeping-up-with-the-radar).
