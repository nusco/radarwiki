---
name: learning-plan
description: Create a layered self-study plan for a short technical topic (30' to a weekend), with curated videos and articles. Use when the user asks for a learning plan, study plan, or how to learn a technical topic quickly.
argument-hint: "[topic] [time budget]"
---

# Learning plan

Create a self-study plan for: $TOPIC, with a specific $TIME_BUDGET

## Standing rules

- The $TOPIC can be a literal topic ("Zero trust architecture") or a URL referring to it (https://www.thoughtworks.com/radar/techniques/zero-trust-architecture)
- Write the plan to a Markdown file in the `Topics` folder.
- In the file, use Markdown syntax for links. Also, list resources as GitHub Markdown todo items.
- Structure the file logically, beginning with the topic and the time required.
- Open the file with metadata, one field per line. Example for a topic from a Thoughtworks Radar blip:
  ```
  **Time:** ~45 minutes
  **Radar edition:** November 2025
  **Blip:** [Serena](https://www.thoughtworks.com/radar/tools/serena)
  **Quadrant:** Tools
  **Ring:** Assess
  **Created:** 2026-10-21
  ```
  **Quadrant** is Techniques, Tools, Platforms, or Languages & Frameworks: it's the path segment after `/radar/` in the blip URL. **Ring** is Adopt, Trial, Assess, Hold, or Caution. If the blip appears in several editions, list them all (like "November 2025 and April 2026"). For a topic that doesn't come from the Radar, replace the four Radar lines with a single **Source:** line that links where the topic came from.
  **Created** is today's date in ISO format. Keep this date when you revise the plan later. Use it to tell how old the plan's time-sensitive parts are, such as "Current state of the topic", before you update them.
- The file will be opened as a note in Obsidian, so its file name should be something like "Model Context Protocol (MCP).md", and you shouldn't add a Markdown level-1 title inside (like #MCP); Obsidian will add the title automatically.
- Design for slow, thoughtful learning. Assume that the learner will re-read, pause/rewind videos, take notes, and pick up on new threads. Estimate every layer at about **three times** the time needed to just read/watch the content. For example, two 30' videos take about 3 hours, a 10-minute article takes about 30 minutes, and hands-on exercises take at least three times what you'd expect. Size the content so that it fits the time budget at this pace, and still give the nominal length of each video or article next to its link.
- The learner's goal is to become an up-to-date **generalist**: to understand the current state of technology and how it got here, not to master each topic. All plans together form one larger curriculum. So, when you choose or suggest a time budget, base it on how relevant the topic is to that general understanding, not on how broad the topic is. A niche tool can get 30'–60' even if it has a lot of features. A subtopic usually gets less time than its parent topic. For example, if "Model Context Protocol (MCP)" takes 6 hours, then FastMCP (a framework for MCP) might get two hours, and a single MCP server such as Context7 might get one or less. This is a guideline, not a hard rule: a subtopic can get more time when it's more relevant than its parent. Judge each case, and when you depart from the guideline, say why in one line so the learner can disagree and ask for correction.
- Relevance means relevance **today**, not when the topic was hot. Before choosing a budget, check which Radar editions in the `Thoughtworks Radar` folder list the topic, and how it has fared since:
  - If the topic appears in one of the recent editions, it's probably current: give it the full time its relevance deserves.
  - If it only appears in older editions, judge how relevant it still is. A topic that has matured into a widely used foundation can still deserve real time. A topic that has since been superseded, abandoned, or made moot (like a tool replaced by newer tools, or a migration that everyone finished years ago) gets a quick plan of 15'–30', no matter how important it once was. One example is [IE6 end-of-life](https://www.thoughtworks.com/radar/platforms/ie6-end-of-life). Such a plan is mostly historical: what the topic was, what role it played, what replaced it, and what lessons or ideas survive from it. It can have a single layer, and no hands-on exercise.
- If the learner gave a time budget that seems inappropriate (too long for an obsolete topic, or too short for an important one) supersede it with your own estimate, but explicitly say so in one line so the learner can push back or ask you to change the estimate.
- Plans must work well together. Before you write a plan, look at the existing plans in the `Topics` folder. If the new topic is related to one of them, link to it with an Obsidian link (like `[[Model Context Protocol (MCP)]]`). Assume what the earlier plan covers instead of repeating it, avoid reusing its resources, and build the exercises on the earlier plan's exercises when that makes sense. Keep one plan per topic: two tools that the Radar lists separately get two plans.
- Treat the plans as a wiki: link material, don't duplicate it. When two blips overlap, put each resource, exercise or explanation in the one plan where it fits best, usually the plan whose blip is about it. In the other plan, add a short explicit pointer that says what it will find there (for example, "Mapping the trifecta across your whole setup is covered in [[Toxic flow analysis for AI]]"). Make an exception only when removing the material would leave a big hole in a topic. In that case, keep a brief version (one resource or a one-line recap) and link to the full treatment.
  - This works in both directions. When you write a new plan, check whether existing plans already cover its material. If one does, move that material into the new plan, even if the learner has already ticked it off: move it as it is, still ticked, so their progress stays. Replace the moved material with a pointer, and fix any "Assumption:" line that no longer holds.
  - If a related blip has no plan yet, an existing plan can cover it briefly. When that blip gets its own plan, apply the rule above.
- **Structural links go to plans, not blips.** A structural link is one that helps the learner find their way between topics, such as the related topics in "Recommendation for future learning", a series list, or an entry in `Study List.md`. When the blip has a plan, make that link an Obsidian link to the plan (like `[[Agent Skills]]`, or `[[Agent Scan|MCP-Scan]]` when the plan covers a blip under another name), and don't add a second link to the blip next to it. Link to the blip itself only when the learner needs to read it: the **Blip:** metadata line, the blip as the first item of Layer 1, the **Close** item, and other blips that are reading resources inside a layer. A topic that has no plan yet keeps its blip link. When you write a new plan, replace the structural links to its blip in `Study List.md` and in the other plans with links to the new plan.

## Maintaining existing plans

- **Skill changes reach existing plans.** Whenever you change this skill, update the plans already in the `Topics` folder to follow the new version, without waiting for the learner to ask. If an update could be destructive, such as losing progress on a plan the learner has started, explain the problem plainly and ask before you make it. Describe the change in natural language, not as a code diff or another proposal that's hard to judge at a glance.
- **Completed and in-progress plans should be stable.** When you change a plan where some items are already ticked off, preserve the ticked items. If a change would substantially alter a ticked item, describe the issue to the learner and let them decide. A plan where every item is ticked off is done: don't update it automatically, and don't add new items that would turn it back into "in progress". If you think a completed plan really needs a change, ask the learner specifically.

## Steps

1. **Pin down the inputs.** Get the topic and time budget from the arguments. If the budget is missing, choose one with the relevance rules above (both general and current relevance) and state it in one line, so the learner can change it. If the learner's background is unclear, state your assumption in one line instead of asking.
2. **Cover what the blip highlights.** If the topic comes from a Radar blip, list everything the blip explicitly mentions or links to: concepts, tools, criticisms, related specs. Each one must end up in the plan: in a layer, in "If you have extra time", in the recommendation for future learning, or as a related topic with its own plan. Skip one only for a clear reason, such as time or scope, duplicated information, or obsolescence, and state that reason in one line in the plan, so the learner knows it was a choice and not an oversight.
3. **Split the time into 2–4 layers**, from fundamentals (that might be just one short description or a 5 minutes video) to applied use. Each layer must leave the learner with something usable, so they can stop after any layer. If time is tight, then have a minimum of two layers. The exception is a quick historical plan for an obsolete topic, which can have a single layer.
   - **Give each layer one theme.** Everything in a layer should serve the theme in its title. If a layer needs to cover two concerns, split it into subsections, each with its own consistent theme and title. Don't mix concerns in a layer (for example, security resources in a "Build a server" layer, or a changelog in a "Design" layer): it makes the learning feel chaotic. If an item doesn't fit any layer's theme, move it to "If you have extra time" or the recommendation for future learning.
   - **Start Layer 1 with the blip, then a concrete example.** If the topic comes from a Radar blip, the blip is the first item. The second item should be short and concrete, such as a worked example, a demo, a quick look at a real artifact, or a tiny hands-on step. It can be a **Read**, a **Skim** or a **Do**. Its job is to give the learner a concrete anchor for the broader, more theoretical material that follows, so save the announcements, overviews and design rationale for after it.
4. **For each layer, give:**
   - a heading with the time slot and estimated hours
   - a one-line **Goal**
   - 1–4 **Read** / **Watch** resources, each with a link and a short reason it was picked
   - in levels 3-4, one hands-on **Do** exercise, with later exercises building on earlier ones
5. **Curate resources carefully:**
   - Prefer well-regarded conference talks and established authors. Follow these general preferences, but quality always wins, so make an exception when a resource is clearly better:
      * **Curated third-party explanations over official docs.** A good article by a respected practitioner usually explains a topic better than the reference page. Use official docs when they are the best explanation, or for the hands-on parts (quickstarts, tool pages).
      * **Human-written over LLM-generated.** Some docs, including official ones, read as generated: verbose, overly detailed, meandering. Prefer a terse, well-structured narrative written by a person.
      * **Short over long.** Pick the shortest resource that does the topic justice. Use a long one only when the topic really needs the length.
   - You can include brief courses from the following sources–even paid ones, as long they are relevant and high quality:
      * Coursera
      * Deeplearning.ai
      * Pluralsight
   - Use only resources you are confident exist. Verify any you are unsure of with a web search.
   - Always point to existing human-written or human-curated content instead of writing your own explanations or walkthroughs.
   - Check what a page actually contains before you add it, and say exactly how the learner should use it. A page that explains concepts or walks through an example is a **Read**. A page that mostly describes a tool, such as an overview or a reference of options, is a **Skim**. Tell the learner to skim it and try the tool for a few minutes, and let a later **Do** exercise give them real practice with it. For example: "Skim: MCP Inspector — skim the page, then launch the Inspector and click around. You'll use it properly in the exercise below."
   - Use **Skim** only for tool pages like these. Never ask the learner to skim dense conceptual material, such as a list of vulnerabilities or a spec that assumes background knowledge: skimming it leaves them with nothing they understand. Either make it a **Read** that fits the layer and the learner's background, or leave it out (and, if it matters, point to it in the recommendation for future learning).
   - Give video lengths when you know them.
6. **Have a short "If you have extra time" note**.
7. **Give a quick assessment of the current state of the topic**: How did it evolve recently, across its history, and/or since the original resource given by the learner was published? Is there any timely need-to-know information, like the fact that the topic is now obsolete or irrelevant, or still evolving as we speak? Keep this short: one to three quick paragraphs.
8. **At the end, give your recommendation for future learning:**
   - Is the topic small and covered adequately by this plan?
   - Would you recommend having a longer self-study plan for this topic? How long? (Follow the relevance rule above.)
   - Is the topic so vast that you'd recommend splitting it into multiple smaller topics?
   - List all related topics in Thoughtworks Radar. (You'll find all the topics listed by Radar edition in the `Thoughtworks Radar` folder.) Make them plain list items, not checkboxes: they're pointers, not tasks, so the learner never has to come back to a finished plan to check them off. Follow the rule on structural links: link a topic that has a plan to the plan, like `[[Agent Skills]] (Apr 2026)`, and link a topic without a plan to its blip.
   - If there is any Coursera/Deeplearning.ai/Pluralsight course that is especially relevant but doesn't fit the time budget, you can recommend it here.
9. **Close with the blip.** If the topic comes from a Radar blip, end the file with a horizontal rule and this to-do item, linking the blip: `- [ ] **Close:** [Review the blip](<blip URL>) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.`

Keep the whole plan scannable. It should go from a few lines to a screenful of text for a weekend-long plan.
