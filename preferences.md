These are my preferences for every learning plan in this wiki. The `learning-plan` skill reads this file before it writes or updates a plan. When a request asks for something different, the request wins for that plan.

## Default length

- My goal is to become an up-to-date **generalist**: to understand the current state of technology and how it got here, not to master each topic. All plans together form one larger curriculum. So, when you choose or suggest a time budget, base it on how relevant the topic is to that general understanding, not on how broad the topic is. A niche tool can get 30'–60' even if it has a lot of features. A subtopic usually gets less time than its parent topic. For example, if "Model Context Protocol (MCP)" takes 6 hours, then FastMCP (a framework for MCP) might get two hours, and a single MCP server such as Context7 might get one or less. This is a guideline, not a hard rule: a subtopic can get more time when it's more relevant than its parent. Judge each case, and when you depart from the guideline, say why in one line so I can disagree and ask for correction.
- Relevance means relevance **today**, not when the topic was hot. Before choosing a budget, check which Radar editions in the `Thoughtworks Radar` folder list the topic, and how it has fared since:
  - If the topic appears in one of the recent editions, it's probably current: give it the full time its relevance deserves.
  - If it only appears in older editions, judge how relevant it still is. A topic that has matured into a widely used foundation can still deserve real time. A topic that has since been superseded, abandoned, or made moot (like a tool replaced by newer tools, or a migration that everyone finished years ago) gets a quick plan of 15'–30', no matter how important it once was. One example is [IE6 end-of-life](https://www.thoughtworks.com/radar/platforms/ie6-end-of-life). Such a plan is mostly historical: what the topic was, what role it played, what replaced it, and what lessons or ideas survive from it. It can have a single level, and no hands-on exercise.

## Pace

- Design for slow, thoughtful learning. Assume that I'll re-read, pause/rewind videos, take notes, and pick up on new threads. Estimate every level at about **three times** the time needed to just read/watch the content. For example, two 30' videos take about 3 hours, a 10-minute article takes about 30 minutes, and hands-on exercises take at least three times what you'd expect.

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
- **Current state of the topic.** After "If you have extra time", give a quick assessment of the current state of the topic. How did it evolve recently, across its history, and/or since the original resource I gave was published? Is there any timely need-to-know information, like the fact that the topic is now obsolete or irrelevant, or still evolving as we speak? Keep this short: one to three quick paragraphs.
- **Related Radar topics.** At the end of the recommendation for future learning, list all related topics in the Thoughtworks Radar. Make them plain list items, not checkboxes: they're pointers, not tasks, so I never have to come back to a finished plan to check them off. Follow the rule on structural links: link a topic that has a plan to the plan, like `[[Agent Skills]] (Apr 2026)`, and link a topic without a plan to its blip.
- **Close with the blip.** For a topic from a Radar blip, end the file with a horizontal rule and this to-do item, linking the blip: `- [ ] **Close:** [Review the blip](<blip URL>) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.`
