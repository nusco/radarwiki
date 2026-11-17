# User Preferences

These are my preferences for every learning plan in this wiki. The `learning-plan` skill reads this file before it writes or updates a plan. When a request asks for something different, the request wins for that plan.

## Default length

- My goal is to become an up-to-date **generalist**: to understand the current state of technology and how it got here, not to master each topic. All plans together form one larger curriculum. So, when you choose or suggest a time budget, base it on how relevant the topic is to that general understanding, not on how broad the topic is. A niche tool can get 30'–60' even if it has a lot of features. A subtopic usually gets less time than its parent topic. For example, if "Model Context Protocol (MCP)" takes 6 hours, then FastMCP (a framework for MCP) might get two hours, and a single MCP server such as Context7 might get one or less. This is a guideline, not a hard rule: a subtopic can get more time when it's more relevant than its parent. Judge each case, and when you depart from the guideline, say why in one line so I can disagree and ask for correction.
- Relevance means relevance **today**, not when the topic was hot. Before choosing a budget, check which Radar editions in the `Thoughtworks Radar` folder list the topic, and how it has fared since:
  - If the topic appears in one of the recent editions, it's probably current: give it the full time its relevance deserves.
  - If it only appears in older editions, judge how relevant it still is. A topic that has matured into a widely used foundation can still deserve real time. A topic that has since been superseded, abandoned, or made moot (like a tool replaced by newer tools, or a migration that everyone finished years ago) gets a quick plan of 15'–30', no matter how important it once was. One example is [IE6 end-of-life](https://www.thoughtworks.com/radar/platforms/ie6-end-of-life). Such a plan is mostly historical: what the topic was, what role it played, what replaced it, and what lessons or ideas survive from it. It can have a single level, and no hands-on exercise.

## Pace

- Design for slow, thoughtful learning. Assume that I'll re-read, pause/rewind videos, take notes, and pick up on new threads. Estimate every activity at about **three times** the time needed to just read, watch or do the content. For example, two 30' videos take about 3 hours, a 10-minute article takes about 30 minutes, and hands-on exercises take at least three times what you'd expect.

## Trusted sources

- My topics usually come from the Thoughtworks Technology Radar. The `Thoughtworks Radar` folder lists all its topics by edition.
- You can include brief courses from the following sources, even paid ones, as long as they are relevant and high quality. If one is especially relevant but doesn't fit the time budget, you can recommend it in "Recommendation for future learning".
  * Coursera
  * DeepLearning.AI
  * Pluralsight

## Avoided sources

- None yet.

## Link style

- I open plans as notes in Obsidian. Name each file after its topic, like "Model Context Protocol (MCP).md", and don't add a Markdown level-1 title inside (like `# MCP`): Obsidian shows the file name as the title.
- Link between plans with Obsidian links, like `[[Agent Skills]]`, or `[[Agent Scan|MCP-Scan]]` when a plan covers a topic under another name.
- Use standard Markdown links for everything else, such as resources and blips.

## Rituals

- **Find the blip.** A topic is from a Radar blip if I give its blip URL, or if the Radar has a blip for it. Before you start a plan, look for one in the `Thoughtworks Radar` folder. A blip can use a different name for the topic (for example, MCP-Scan is in the Radar as Agent Scan), so match the topic, not just the name. I expect every topic to have a blip, so if you can't find one, something is wrong: maybe I misspelled the topic, or the folder is missing an edition. Don't write the plan. Tell me that you found no blip, and list any close matches in the folder.
- **Radar metadata.** For a topic from a Radar blip, replace the **Source:** metadata line with four lines, like this:
  ```
  **Time:** ~45 minutes
  **Radar edition:** November 2025
  **Blip:** [Serena](https://www.thoughtworks.com/radar/tools/serena)
  **Quadrant:** Tools
  **Ring:** Assess
  **Created:** 2026-10-21
  ```
  **Quadrant** is Techniques, Tools, Platforms, or Languages & Frameworks: it's the path segment after `/radar/` in the blip URL. **Ring** is Adopt, Trial, Assess, Hold, or Caution. If the blip appears in several editions, list them all (like "November 2025 and April 2026").
- **Start with the blip.** For a topic from a Radar blip, the blip is the first item of Level 1, before the concrete example.
- **Current state of the topic.** Before Level 1, add a section headed `## Current state of the topic (as of <date>)`, so I know what I'm getting into before I start. The date is when you wrote the section, in ISO format. In one short paragraph, tell me what I need to know that the activities won't make clear: Is the topic still relevant today? Did anything major happen to it, like a rename, an acquisition, or an open-source product going commercial? Was it superseded by a competing technology? Is it still changing fast? Don't repeat what the levels teach. When you update the paragraph, update its date too.
- **Related Radar topics.** At the end of the recommendation for future learning, list all related topics in the Thoughtworks Radar. Make them plain list items, not checkboxes: they're pointers, not tasks, so I never have to come back to a finished plan to check them off. Follow the rule on structural links: link a topic that has a plan to the plan, like `[[Agent Skills]] (Apr 2026)`, and link a topic without a plan to its blip.
- **Close with the blip.** For a topic from a Radar blip, end the file with a horizontal rule and this to-do item, linking the blip: `- [ ] **~10 min** · **Close:** [Review the blip](<blip URL>) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.`
