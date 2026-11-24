---
name: learning-plan
description: How to write one learning plan, a self-study page organized in progressive levels, for a Thoughtworks Technology Radar blip (30' to a weekend), with curated videos and articles. It covers the whole procedure, from finding the blip to the finished page, what goes in each section, and the learner's learning preferences. Use when the user asks for a learning plan, study plan, or how to learn a Radar blip or technical topic quickly.
argument-hint: "[topic] [time budget]"
---

# Learning plan

Create a self-study plan for the Thoughtworks Technology Radar blip on: $TOPIC, with a specific $TIME_BUDGET

The $TOPIC can be a literal topic ("Zero trust architecture") or a URL referring to it (https://www.thoughtworks.com/radar/techniques/zero-trust-architecture).

**Follow the `radarwiki` skill first.** [`radarwiki`](../radarwiki/SKILL.md) holds the rules for every page in the wiki: keeping up with the Radar, naming and links, the wiki rules, maintaining existing pages, and research integrity. Read it before you write or change a plan. This skill only adds what's specific to learning plans.

## The template

[`assets/template.md`](assets/template.md) is the structure of every plan: its sections in order. Follow it in every plan.

- Copy the template's body, never its frontmatter: plans have no frontmatter.
- Text in `{curly braces}` describes what goes there, and "Ex." gives an example. Everything else is copied as is.
- A placeholder that starts with "Optional" can be left out. Leave it out unless this skill says the plan needs it.
- When a request asks for something the template or this skill doesn't, the request wins for that plan.

## Steps

1. **Find the blip.** If the learner gave the blip's URL, that's the blip. Otherwise, look for it in the `Thoughtworks Radar` folder. A blip can use a different name for the topic (for example, Grafana Agent is in the Radar as Grafana Alloy), so match the topic, not just the name. But if the Radar has a blip under the name the learner used, that's the blip, even if another blip seems to cover the same topic: blips that the Radar lists separately stay separate. Every topic should have a blip, so if you can't find one, something is wrong: maybe the learner misspelled the topic, or the folder is missing an edition. Don't write the plan. Tell the learner that you found no blip, and list any close matches in the folder.

2. **Pin down the inputs.** Get the topic and time budget from the arguments. If the budget is missing, choose one with the rules on [default length](#default-length). If the learner gave a budget that seems inappropriate (too long for an obsolete topic, or too short for an important one), supersede it with your own estimate. If the learner's background is unclear, assume one instead of asking. State these choices in the plan, as [Prerequisites and time budget](#prerequisites-and-time-budget) says, so the learner can push back.

3. **Cover what the blip highlights.** List everything the blip explicitly mentions or links to: concepts, tools, criticisms, related specs. Each one must end up in the plan: in a level, in "If you have extra time", in the wrap-up, or as a related topic with its own plan. Skip one only for a clear reason, such as time or scope, duplicated information, or obsolescence, and state that reason in one line in the plan, so the learner knows it was a choice and not an oversight.

4. **Find the resources,** following the research integrity rules in `radarwiki`, the rules on [resources](#resources) below, and the trusted and avoided sources in the [learning preferences](#learning-preferences).

5. **Write the plan** in the `pages` folder, following the template section by section, and the [writing rules](#writing-rules) and [sections](#sections) below.

## Writing rules

- **Keep the plan scannable.** It goes from a few lines to a screenful of text for a weekend-long plan.
- **Keep generated text small, and set it apart.** Write your own text only where it helps the plan read well: a theme line, the prerequisites, an exercise brief, a one-line pointer. Keep it short, and never format it like a resource: only human-made content gets a **Read**, **Watch** or **Skim** label and a link with author and date.
- **Every activity is a to-do item**, so the learner can tick it off: resources, exercises, "If you have extra time" items, and the "Review the blip" item. Related topics are plain list items: they're pointers, not tasks, so the learner never has to come back to a finished plan to check them off.
- **Don't hedge.** Every activity should leave the learner knowing what to do next. Options are fine, such as an optional extra resource or an alternative exercise, as long as the plan gives the learner the means to choose: what each option offers that the other doesn't, who or what situation it suits, and how long it takes. If the learner could only make the choice by trying every option first, make it for them. For example, don't mention an alternative resource with a vague caveat ("the blip links to another article, but it's partly paywalled"). Decide where it belongs (in a level, in "If you have extra time", or left out with a reason) and say what it adds.

## Sections

### Metadata

- **Updated** is the date you last changed the plan, so the learner can tell how fresh it is. Older plans may have a **Created** field instead: replace it with **Updated** when you change the plan. The creation date doesn't matter.
- **Status** is always `#undone` in a new plan, and you never change it afterwards. The learner changes it to something else as they study, such as `#wip` or `#done`.

### Prerequisites and time budget

- **Prerequisites:** write them only when the learner's background is unclear, or when the plan builds on other plans. In that case, say what the plan assumes from them, and link them.
- **Time budget:** explain it only if it needs explaining: you chose it because the learner gave none, it departs from the default length, or it overrides the learner's budget. Otherwise, leave it out.

### Current state

The paragraph puts the topic in perspective today, telling the learner what they need to know before starting that the activities won't make clear. Is the topic still relevant? Did anything major happen to it, like a rename, an acquisition, or an open-source product going commercial? Was it superseded by a competing technology? Is it still changing fast? Don't repeat what the levels teach.

Its goals are to:

- Put the topic in perspective.
- Fill in historical gaps in the study material. Maybe all the linked content is from ten years ago. What happened since?
- Remove any lingering doubts that the study material is obsolete or irrelevant, in particular for older topics.

### Levels

The levels are the core of the plan.

- **Levels go progressively deeper.** Each level leaves the learner with usable knowledge, so they can stop after any level. Have at least two levels, usually two to four, unless the plan is a quick historical plan for an obsolete, now barely-relevant topic.
- **At a bare minimum, cover the _what_, _why_ and _how_ of the topic.** This is an indication: if it doesn't fit a topic, go for something else.
  - **Level 1** usually answers the very basic questions about the topic: what is it, what problem does it solve, what does it look like? It starts with the Radar blip, followed by something short and concrete, as an anchor for the more theoretical material that follows. The anchor can be a **Read**, a **Skim** or a **Do**.
  - **Level 2** is usually the "Shu" in "Shu-Ha-Ri": it covers the basics of how the topic works, and shows the motions.
  - **Levels 3 and above** are optional. They tend to be the "Ha" in "Shu-Ha-Ri": hands-on experience, the role of the topic in the wider ecosystem, alternatives, problems and shortcomings. Go beyond Level 3 only when the topic has more good storylines.
- **Give each level one theme.** Everything in a level serves the theme in its title, and the line under the title says what the level is about and what the learner will be able to do after it. If a level needs to cover two concerns, split it into `###` subsections, each with its own theme. Don't mix concerns (for example, security resources in a "Build a server" level): it makes the learning feel chaotic. An item that fits no level goes to "If you have extra time" or the wrap-up.
- **Each level has 1–4 resources**, and at most one **Do** exercise.

### Activities

- **Read, Watch or Skim?** A page that explains concepts or walks through an example is a **Read**. A page that mostly describes a tool, such as an overview or a reference of options, is a **Skim**: the learner skims it, tries the tool for a few minutes, and gets real practice in a later **Do**. Never ask the learner to skim dense conceptual material, such as a list of vulnerabilities or a spec that assumes background knowledge. Make it a **Read** that fits the level and the learner's background, or leave it out (and, if it matters, point to it in the wrap-up).
- **Do** exercises go only where practice fits the level. Each ends with something concrete to produce, compare or decide, so the learner knows when it's done, and builds on earlier exercises.
- For each resource, say why you picked it, and how to use it.

### Resources

- A resource can be anything: a blog post, a conference talk, a page of official documentation. Paid resources are fine only from the trusted sources.
- Prefer well-regarded conference talks and established authors. Quality always wins, so make an exception to these preferences when a resource is clearly better:
  - **Curated third-party explanations over official docs.** A good article by a respected practitioner usually explains a topic better than the reference page. Use official docs when they are the best explanation, or for the hands-on parts (quickstarts, tool pages).
  - **Short over long.** Pick the shortest resource that does the topic justice.

### Time estimates

- **Every to-do item starts with the time the learner will spend on it.** Work it out from the time the content strictly needs (the length of the article or video, or the bare work in an exercise), adjusted for the [pace](#pace). Use round numbers, like ~5 min, ~20 min, ~1 hour or ~1.5 hours.
- **Give the resource's own length too**, when you know it, so the learner can tell it apart from the time the activity takes.
- **Make the estimates add up.** Each level's time is roughly the sum of its activities, and **Time** is the sum of the levels. "If you have extra time" and "Review the blip" don't count. Size the content to fit the time budget.

### If you have extra time

One to three short activities, for the learner who wants to know more about the topic. If useful, explain why an activity is optional. For example, this section might include a longer online course of a few hours that exceeds the time budget.

### Wrap-up

- Say whether the topic is small and covered adequately by this plan, whether you'd recommend a longer plan (and how long), or whether the topic is so vast that you'd split it into smaller topics.
- If you left out something the blip mentions, say what, and why. Otherwise, leave that line out.

### Related Radar topics

Link each related topic to its plan if it has one, or to its blip if it doesn't. Don't mention editions.

## Learning preferences

### Default length

- The learner's goal is to become an up-to-date **generalist**: to understand the current state of technology and how it got here, not to master each topic. All plans together form one larger curriculum. So, when you choose or suggest a time budget, base it on how relevant the topic is to that general understanding, not on how broad the topic is. A niche tool can get 30'–60' even if it has a lot of features. A subtopic usually gets less time than its parent topic. For example, if "Model Context Protocol (MCP)" takes 6 hours, then FastMCP (a framework for MCP) might get two hours, and a single MCP server such as Context7 might get one or less. This is a guideline, not a hard rule: a subtopic can get more time when it's more relevant than its parent. Judge each case, and when you depart from the guideline, say why in the time budget line.
- Relevance means relevance **today**, not when the topic was hot. Before choosing a budget, check which Radar editions in the `Thoughtworks Radar` folder list the topic, and how it has fared since:
  - If the topic appears in one of the recent editions, it's probably current: give it the full time its relevance deserves.
  - If it only appears in older editions, judge how relevant it still is. A topic that has matured into a widely used foundation can still deserve real time. A topic that has since been superseded, abandoned, or made moot (like a tool replaced by newer tools, or a migration that everyone finished years ago) gets a quick plan of 15'–30', no matter how important it once was. One example is [IE6 end-of-life](https://www.thoughtworks.com/radar/platforms/ie6-end-of-life). Such a plan is mostly historical: what the topic was, what role it played, what replaced it, and what lessons or ideas survive from it. It can have a single level, and no hands-on exercise.

### Pace

Design for slow, thoughtful learning. Assume that the learner will re-read, pause/rewind videos, take notes, and pick up on new threads. Estimate every activity at about **three times** the time needed to just read, watch or do the content. For example, two 30' videos take about 3 hours, a 10-minute article takes about 30 minutes, and hands-on exercises take at least three times what you'd expect.

### Trusted sources

- The `Thoughtworks Radar` folder lists all the Radar's topics by edition.
- You can include brief courses from the following sources, even paid ones, as long as they are relevant and high quality. If one is especially relevant but doesn't fit the time budget, you can recommend it in the wrap-up.
  - Coursera
  - DeepLearning.AI
  - Pluralsight

### Avoided sources

None yet.
