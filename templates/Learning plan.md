- **Blip:** {Ex.: "[Serena](https://www.thoughtworks.com/radar/tools/serena)"}
- **Time:** {Ex.: "~45 minutes"}
- **Radar edition:** {Ex.: "November 2025 and April 2026"}
- **Quadrant:** {"Techniques", "Tools", "Platforms", or "Languages & Frameworks"}
- **Ring:** {"Adopt", "Trial", "Assess", or "Caution" (formerly "Hold")}
- **Updated:** {The update date of the page. Ex.: "2026-10-21"}
- **Status:** {Always "#undone"; the user can change this to something else as they study, such as "#wip" or "#done"}

*Assumption: {The learner's background, only when it's unclear. If the plan builds on other plans, what it assumes from them, with links. Ex.: "You know what an MCP server is and how to add one to Claude Code, from `[[Model Context Protocol (MCP)]]`."}*

*Time budget: {Why this time budget, only if it needs explaining: you chose it because the learner gave none, it departs from the default length, or it overrides the learner's budget. Otherwise, leave this line out. Ex.: "a single tool would usually get an hour or less, but Pi has become a foundation that other agents are built on, and it's best learned by extending it, which takes time."}*

---

## Current state of the topic ({The date you wrote this section. Ex.: "late 2026"})

{One short paragraph on what the learner needs to know before starting, that the activities won't make clear: Is the topic still relevant today? Did anything major happen to it, like a rename, an acquisition, or an open-source product going commercial? Was it superseded by a competing technology? Is it still changing fast? Don't repeat what the levels teach.}

---

## Level 1 — {The level's theme. Ex.: "What it is"} ({The time slot. Ex.: "0:00–0:15"}, {The level's time. Ex.: "~15 min"})

**Goal:** {What the learner will be able to do after this level, in one line. Ex.: "Explain how Context7 reduces hallucinated code."}

- [ ] **{Time}** · Read: [The Radar blip]({The blip URL}) ({The blip's length. Ex.: "~1 min"}).
- [ ] **{Time}** · {Something short and concrete, as an anchor for the more theoretical material that follows: a worked example, a demo, a quick look at a real artifact, or a tiny hands-on step. It can be a Read, a Skim or a Do.}

## Level 2 — {The level's theme. Ex.: "How it works"} ({The time slot. Ex.: "0:15–0:45"}, {The level's time. Ex.: "~30 min"})

**Goal:** {What the learner will be able to do after this level, in one line.}

- [ ] **{Time}** · Read: [{Title}]({URL}) ({Author, date and length. Ex.: "Enes Akar, Upstash, Mar 2025, 6 min"}) — {Why you picked it, and how to use it.}
- [ ] **{Time}** · Watch: [{Title}]({URL}) ({Author, date and length}) — {Why you picked it, and how to use it.}
- [ ] **{Time}** · Skim: [{Title}]({URL}) ({Author, date and length}) — {Only for a tool page, such as an overview or a reference of options. Ex.: "skim the page, then launch the Inspector and click around. You'll use it properly in the exercise below."}
- [ ] **{Time}** · **Do:** {A hands-on exercise that ends with something concrete to produce, compare or decide, so the learner knows when it's done. It builds on earlier exercises. Only where practice fits the level.}

## Level {N} — {The level's theme} ({The time slot}, {The level's time})

{More levels like Level 2, usually 2–4 levels in total.}

---

## If you have extra time

- [ ] **{Time}** · {One to three short activities, for the learner who wants to know more about the topic. Ex.: an additional video or blog post.}

---

## Recommendation for future learning

{Is the topic small and covered adequately by this plan? Would you recommend a longer plan, and how long? Is the topic so vast that you'd split it into smaller topics? Ex.: "This plan covers it."}

**Left out from the blip:** {Only if you left out something the blip mentions: what, and why. Otherwise, leave this line out.}

Related Radar topics:

- {A related Radar topic: a link to its plan if it has one, like `[[Agent Skills]]`, or to its blip if it doesn't. No editions.}

---

- [ ] **~10 min** · **Close:** [Review the blip]({The blip URL}) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.

# About this template

This is the model for every learning plan in the `pages` folder. Edit it to change the style of the wiki. Changing it doesn't update the existing plans: ask the agent when you want them updated.

Everything above this heading is the plan. Text in `{curly braces}` describes what goes there, and "Ex." gives an example. Everything else is copied as is. Everything from this heading down is not part of the plan.

When a request asks for something this template doesn't, the request wins for that plan.

## Writing rules

- **Keep the plan scannable.** It goes from a few lines to a screenful of text for a weekend-long plan.
- **Keep generated text small, and set it apart.** Write your own text only where it helps the plan read well: a goal, an assumption, an exercise brief, a one-line pointer. Keep it short, and never format it like a resource: only human-made content gets a **Read**, **Watch** or **Skim** label and a link with author and date.
- **Every activity is a to-do item**, so the learner can tick it off: resources, exercises, "If you have extra time" items, and the closing item. Related topics are plain list items: they're pointers, not tasks, so the learner never has to come back to a finished plan to check them off.
- **Don't hedge.** Every activity should leave the learner knowing what to do next. Options are fine, such as an optional extra resource or an alternative exercise, as long as the plan gives the learner the means to choose: what each option offers that the other doesn't, who or what situation it suits, and how long it takes. If the learner could only make the choice by trying every option first, make it for them. For example, don't mention an alternative resource with a vague caveat ("the blip links to another article, but it's partly paywalled"). Decide where it belongs (in a level, in "If you have extra time", or left out with a reason) and say what it adds.

### Levels

- **Levels go progressively deeper.** Each level leaves the learner with usable knowledge, so they can stop after any level. Have at least two levels, unless the plan is a quick historical plan for an obsolete topic.
- **Cover the _what_, _why_ and _how_ of the topic, at a bare minimum.** For example, Level 1 might cover what the topic is and why it exists, Level 2 how it works, and the following levels go deeper: hands-on experience, the role of the topic in the wider ecosystem, problems and issues. This is an indication: if it doesn't fit a topic, go for something else.
- **Give each level one theme.** Everything in a level serves the theme in its title. If a level needs to cover two concerns, split it into `###` subsections, each with its own theme. Don't mix concerns (for example, security resources in a "Build a server" level): it makes the learning feel chaotic. An item that fits no level goes to "If you have extra time" or the recommendation for future learning.
- **Each level has 1–4 resources**, and at most one **Do** exercise.

### Resources

- A resource can be anything: a blog post, a conference talk, a page of official documentation. Paid resources are fine only from the trusted sources.
- Prefer well-regarded conference talks and established authors. Quality always wins, so make an exception to these preferences when a resource is clearly better:
  - **Curated third-party explanations over official docs.** A good article by a respected practitioner usually explains a topic better than the reference page. Use official docs when they are the best explanation, or for the hands-on parts (quickstarts, tool pages).
  - **Short over long.** Pick the shortest resource that does the topic justice.
- **Read or Skim?** A page that explains concepts or walks through an example is a **Read**. A page that mostly describes a tool is a **Skim**: the learner skims it, tries the tool for a few minutes, and gets real practice in a later **Do**. Never ask the learner to skim dense conceptual material, such as a list of vulnerabilities or a spec that assumes background knowledge. Make it a **Read** that fits the level and the learner's background, or leave it out (and, if it matters, point to it in the recommendation for future learning).

### Time estimates

- **Every to-do item starts with the time the learner will spend on it.** Work it out from the time the content strictly needs (the length of the article or video, or the bare work in an exercise), adjusted for the pace. Use round numbers, like ~5 min, ~20 min, ~1 hour or ~1.5 hours.
- **Give the resource's own length too**, when you know it, so the learner can tell it apart from the time the activity takes.
- **Make the estimates add up.** Each level's time is roughly the sum of its activities, and **Time** is the sum of the levels. "If you have extra time" and the closing item don't count. Size the content to fit the time budget.

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
- You can include brief courses from the following sources, even paid ones, as long as they are relevant and high quality. If one is especially relevant but doesn't fit the time budget, you can recommend it in "Recommendation for future learning".
  - Coursera
  - DeepLearning.AI
  - Pluralsight

### Avoided sources

None yet.

### Link style

- The learner opens plans as notes in Obsidian. Name each file after its topic, like `Model Context Protocol (MCP).md`, and don't add a Markdown level-1 title inside (like `# MCP`): Obsidian shows the file name as the title.
- Link between plans with Obsidian links, like `[[Agent Skills]]`, or `[[Agent Scan|MCP-Scan]]` when a plan covers a topic under another name.
- Use standard Markdown links for everything else, such as resources and blips.
