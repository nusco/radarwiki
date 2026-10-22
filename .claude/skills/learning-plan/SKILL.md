---
name: learning-plan
description: Create a layered self-study plan for a short technical topic (from 30 minutes to a weekend), with curated videos and articles. Use when the user asks for a learning plan, study plan, or how to learn a technical topic quickly.
argument-hint: "[topic] [time budget]"
---

# Learning plan

Create a self-study plan for: $TOPIC, with a specific $TIME_BUDGET

## Standing rules

- The $TOPIC can be a literal topic ("Zero trust architecture") or a URL referring to it (https://www.thoughtworks.com/radar/techniques/zero-trust-architecture)
- Write the plan to a Markdown file in the `Topics` folder.
- In the file, use Markdown syntax for links. Also, list resources as GitHub Markdown todo items.
- Structure the file logically, beginning with the topic and the time required.
- The file will be opened as a note in Obsidian, so its file name should be something like "Model Context Protocol (MCP).md", and you shouldn't add a Markdown level-1 title inside (like #MCP); Obsidian will add the title automatically.
- The learner is a slow, thorough learner: they pause, rewind, take notes, and follow up on what they read. Estimate every layer at about **twice** the time a typical learner would need. For example, two 30' videos take about 2 hours, a 10-minute article takes about 20 minutes, and hands-on exercises take at least twice what you'd expect. As a calibration point, the learner needed at least 4 hours for a plan that had been estimated at 2 hours. Size the content so that it fits the time budget at this pace, and still give the nominal length of each video or article next to its link.
- The learner's goal is to become an up-to-date **generalist**: to understand the current state of technology and how it got here, not to master each topic. All plans together form one larger curriculum. So, when you choose or suggest a time budget, base it on how relevant the topic is to that general understanding, not on how broad the topic is. A niche tool can get 30'–60' even if it has a lot of features. A subtopic usually gets less time than its parent topic. For example, if "Model Context Protocol (MCP)" takes 4 hours, then FastMCP (a framework for MCP) might get an hour or two, and a single MCP server such as Context7 might get 30'–60'. This is a guideline, not a hard rule: a subtopic can get more time when it's more relevant than its parent. Judge each case, and when you depart from the guideline, say why in one line so the learner can disagree.
- Relevance means relevance **today**, not when the topic was hot. Before choosing a budget, check which Radar editions in the `Thoughtworks Radar` folder list the topic, and how it has fared since:
  - If the topic appears in one of the recent editions, it's probably current: give it the full time its relevance deserves.
  - If it only appears in older editions, judge how relevant it still is. A topic that has matured into a widely used foundation can still deserve real time. A topic that has since been superseded, abandoned, or made moot (like a tool replaced by newer tools, or a migration that everyone finished years ago) gets a quick plan of 15'–30', no matter how important it once was. [IE6 end-of-life](https://www.thoughtworks.com/radar/platforms/ie6-end-of-life) is an example. Such a plan is mostly historical: what the topic was, what role it played, what replaced it, and what lessons or ideas survive from it. It can have a single layer, and no hands-on exercise.
  - If the learner gave a time budget that seems too long for an obsolete topic, keep the plan short anyway and say so in one line, so the learner can push back.
- Plans must work well together. Before you write a plan, look at the existing plans in the `Topics` folder. If the new topic is related to one of them, link to it with an Obsidian link (like `[[Model Context Protocol (MCP)]]`). Assume what the earlier plan covers instead of repeating it, avoid reusing its resources, and build the exercises on the earlier plan's exercises when that makes sense. Keep one plan per topic: two tools that the Radar lists separately get two plans.

## Steps

1. **Pin down the inputs.** Get the topic and time budget from the arguments. If the budget is missing, choose one with the relevance rules above (both general and current relevance) and state it in one line, so the learner can change it. If the learner's background is unclear, state your assumption in one line instead of asking.
2. **Split the time into 2–4 layers**, from fundamentals (that might be just one short description or a 5 minutes video) to applied use. Each layer must leave the learner with something usable, so they can stop after any layer. If time is tight, then have a minimum of two layers. The exception is a quick historical plan for an obsolete topic, which can have a single layer.
3. **For each layer, give:**
   - a heading with the time slot and estimated hours
   - a one-line **Goal**
   - 1–4 **Read** / **Watch** resources, each with a link and a short reason it was picked
   - in levels 3-4, one hands-on **Do** exercise, with later exercises building on earlier ones
4. **Curate resources carefully:**
   - Prefer official docs, well-regarded conference talks, and established authors.
   - You can include brief courses from the following sources–even paid ones, as long they are relevant and high quality:
      * Coursera
      * Deeplearning.ai
      * Pluralsight
   - Use only resources you are confident exist. Verify any you are unsure of with a web search.
   - Give video lengths when you know them.
5. **Have a short "If you have extra time" note**.
6. **Give a quick assessment of the current state of the topic**: How did it evolve recently, across its history, and/or since the original resource given by the learner was published? Is there any timely need-to-know information, like the fact that the topic is now obsolete or irrelevant, or still evolving as we speak? Keep this short: one to three quick paragraphs.
7. **At the end, give your recommendation for future learning:**
   - Is the topic small and covered adequately by this plan?
   - Would you recommend having a longer self-study plan for this topic? How long? (Follow the relevance rule above.)
   - Is the topic so vast that you'd recommend splitting it into multiple smaller topics?
   - List all related topics in Thoughtworks Radar. (You'll find all the topics listed by Radar edition in the `Thoughtworks Radar` folder.)
   - If there is any Coursera/Deeplearning.ai/Pluralsight course that is especially relevant but doesn't fit the time budget, you can recommend it here.

Keep the whole plan scannable. It should go from a few lines to a screenful of text for a weekend-long plan.
