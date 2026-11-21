---
name: learning-plan
description: Create a self-study plan, organized in progressive levels, for a Thoughtworks Technology Radar blip (30' to a weekend), with curated videos and articles. Use when the user asks for a learning plan, study plan, or how to learn a Radar blip or technical topic quickly.
argument-hint: "[topic] [time budget]"
---

# Learning plan

Create a self-study plan for the Thoughtworks Technology Radar blip on: $TOPIC, with a specific $TIME_BUDGET

## Standing rules

- **Follow the learning preferences.** Every plan must follow the [learning preferences](#learning-preferences) below. When a request asks for something different, the request wins for that plan.
- The $TOPIC can be a literal topic ("Zero trust architecture") or a URL referring to it (https://www.thoughtworks.com/radar/techniques/zero-trust-architecture)
- Write the plan to a Markdown file in the `pages` folder. Name the file, and write its links, in the link style from the learning preferences.
- List every activity (resources, **Do** exercises, "If you have extra time" items, and the items that link the blip) as GitHub Markdown todo items, so the learner can tick them off to track progress.
- **Keep generated text small, and set it apart.** Write your own text only where it helps the plan read well: a goal, an assumption, an exercise brief, a one-line pointer. Keep it short, and never format it like a resource: only human-made content gets a **Read**, **Watch** or **Skim** label and a link with author and date.
- Structure the file logically, beginning with the topic and the time required.
- Open the file with metadata, as a bulleted list with one field per item. Use plain bullets, not todo items:
  ```
  - **Time:** ~45 minutes
  - **Radar edition:** November 2025
  - **Blip:** [Serena](https://www.thoughtworks.com/radar/tools/serena)
  - **Quadrant:** Tools
  - **Ring:** Assess
  - **Created:** 2026-10-21
  ```
  **Radar edition** lists every edition the blip appears in (like "November 2025 and April 2026").
  **Quadrant** is Techniques, Tools, Platforms, or Languages & Frameworks: it's the path segment after `/radar/` in the blip URL.
  **Ring** is Adopt, Trial, Assess, Hold, or Caution.
  **Created** is today's date in ISO format. Keep this date when you revise the plan later. Use it to tell how old the plan's time-sensitive parts are before you update them, unless a part shows its own date.
- Size the content so that it fits the time budget at the pace in the learning preferences.
- **Give every activity a time estimate.** Start each to-do item with how long the learner will spend on the activity, in bold and followed by a middle dot, like `- [ ] **~25 min** · Read: [Title](URL) (Author, Oct 2025, ~8 min) — ...`. This applies to every to-do item: resources, **Do** exercises, "If you have extra time" items, and the items that link the blip. Work out each estimate from the time the content strictly needs (the length of the article or video, or the bare work in an exercise), adjusted for the pace in the learning preferences. Use round numbers, like ~5 min, ~20 min, ~1 hour or ~1.5 hours.
- **Give the nominal length too.** Next to the link of each video or article, give the length of the resource itself, when you know it, so the learner can tell the resource's length apart from the time the activity takes.
- **Make the estimates add up.** Each level's estimate in its heading is roughly the sum of its activities' estimates, and **Time** is the sum of the levels. "If you have extra time" items and items outside the levels, such as the closing blip item, don't count toward **Time**.
- **Tell the learner what to do when they can't decide for themselves.** Every activity should leave the learner knowing what to do next. Options are fine, such as an optional extra resource or an alternative exercise, as long as the plan gives the learner the means to choose: what each option offers that the other doesn't, who or what situation it suits, and how long it takes. Don't hedge: if the learner could only make the choice by trying every option first, make it for them. For example, don't mention an alternative resource with a vague caveat ("the blip links to another article, but it's partly paywalled"). Decide where it belongs (in a level, in "If you have extra time", or left out with a reason) and say what it adds.
- When you choose or suggest a time budget, follow the rules on default length in the learning preferences.
- If the learner gave a time budget that seems inappropriate (too long for an obsolete topic, or too short for an important one) supersede it with your own estimate, but explicitly say so in one line so the learner can push back or ask you to change the estimate.
- Plans must work well together. Before you write a plan, look at the existing plans in the `pages` folder. If the new topic is related to one of them, link to it. Assume what the earlier plan covers instead of repeating it, avoid reusing its resources, and build the exercises on the earlier plan's exercises when that makes sense. Keep one plan per topic: two tools that your sources list separately get two plans.
- Treat the plans as a wiki: link material, don't duplicate it. When two topics overlap, put each resource, exercise or explanation in the one plan where it fits best, usually the plan whose topic is about it. In the other plan, add a short explicit pointer that says what it will find there (for example, "Mapping the trifecta across your whole setup is covered in [[Toxic flow analysis for AI]]"). Make an exception only when removing the material would leave a big hole in a topic. In that case, keep a brief version (one resource or a one-line recap) and link to the full treatment.
  - This works in both directions. When you write a new plan, check whether existing plans already cover its material. If one does, move that material into the new plan, even if the learner has already ticked it off: move it as it is, still ticked, so their progress stays. Replace the moved material with a pointer, and fix any "Assumption:" line that no longer holds.
  - If a related topic has no plan yet, an existing plan can cover it briefly. When that topic gets its own plan, apply the rule above.
- **Structural links go to plans, not sources.** A structural link is one that helps the learner find their way between topics, such as the related topics in "Recommendation for future learning", a series list, or an entry in an index file (for example, a hypothetical `Index.md` listing all topics). When a topic has a plan, make that link a link to the plan, and don't add a second link to the topic's blip next to it. Link to the blip itself only when the learner needs to read it: the **Blip** metadata line, a reading resource inside a level, or the first and closing items that link the blip. A topic that has no plan yet keeps its blip link. When you write a new plan, replace the structural links to its blip in the other plans and in any index file, such as `Index.md`, if one exists, with links to the new plan.

## Keeping up with the Radar

Before you write or revise a plan, check that the `Thoughtworks Radar` folder has the latest edition. The folder has one file per edition, numbered by volume, like `034-thoughtworks-radar-2026-april.md`. Run the download script from the folder, because it writes there.

1. **Check the date.** If the newest edition in the folder is less than 25 weeks old, go on with the request.
2. **Check the website.** Otherwise, run `python3 download-script/radar_to_todo.py < /dev/null`. It reads the [Radar archive](https://www.thoughtworks.com/radar/archive) and lists the published volumes, without downloading anything. If none is newer than the folder, go on with the request. While a Radar is late, you'll check on every request, and that's fine.
3. **Ask first.** If there are new editions, tell the learner which ones, and which existing plans they would change: read the blip page of each plan, and look for the new editions in its history. Then ask before you download anything or change any plan. If the learner says no, go on with the request.
4. **Download the new editions.** Run `printf '<volumes>\n' | python3 download-script/radar_to_todo.py`, with only the new volumes, like `35` or `35-36`. Never select a volume that's already in the folder: its file holds the learner's ticks. The script reads every blip page slowly, so the site doesn't block it. It can take an hour, so let it finish.
5. **Update the README.** Set its sentence on the edition to the newest one, like "Up to date with the Thoughtworks Radar, November 2026 (volume 35)."
6. **Update the plans.** For each plan whose blip appears in a new edition, even in the same ring, update everything that depends on the edition: **Radar edition** and **Ring** in the metadata, the current state paragraph and its date, text that counts or names editions (like "read both versions"), and the edition dates in other plans that link to it. Also update the edition dates that plans give for blips without a plan, like "[OpenClaw](https://www.thoughtworks.com/radar/tools/openclaw) (Apr 2026)" in a list of related topics. This applies to completed plans too: these changes add no tasks and reset no progress. Leave alone blips that dropped out of the new edition, and don't write plans for new blips unless the learner asks.
7. Go on with the request.

## Maintaining existing plans

- **Update existing plans when needed.** Whenever a change in the system is inconsistent with the existing plans (for example, because the user asked for changes that lead you to update this skill), update the existing plans in the `pages` folder to follow the new version, without waiting for the learner to ask. If an update could be destructive, such as losing progress on a plan the learner has started, explain the problem plainly and ask before you make it. Describe the change in natural language, not as a code diff or another proposal that's hard to judge at a glance.

- **Keep in-progress plans stable.** When you change a plan where some items are already ticked off, preserve the ticked items. Never untick an item without asking the learner. If a change would substantially alter a ticked item, describe the issue to the learner and let them decide.

- **Leave completed plans alone.** A plan where every item is ticked off, ignoring the optional "If you have extra time" items, is done: don't update it automatically, and don't add new items that would return it to into "in progress". This includes the changes that the wiki rules above would make, such as moving material out of the plan or updating its structural links. If you think a completed plan really needs a change, ask the learner specifically. The one exception is the update for a new Radar edition, in [Keeping up with the Radar](#keeping-up-with-the-radar).

## Learning preferences

### Default length

- The learner's goal is to become an up-to-date **generalist**: to understand the current state of technology and how it got here, not to master each topic. All plans together form one larger curriculum. So, when you choose or suggest a time budget, base it on how relevant the topic is to that general understanding, not on how broad the topic is. A niche tool can get 30'–60' even if it has a lot of features. A subtopic usually gets less time than its parent topic. For example, if "Model Context Protocol (MCP)" takes 6 hours, then FastMCP (a framework for MCP) might get two hours, and a single MCP server such as Context7 might get one or less. This is a guideline, not a hard rule: a subtopic can get more time when it's more relevant than its parent. Judge each case, and when you depart from the guideline, say why in one line so the learner can disagree and ask for correction.
- Relevance means relevance **today**, not when the topic was hot. Before choosing a budget, check which Radar editions in the `Thoughtworks Radar` folder list the topic, and how it has fared since:
  - If the topic appears in one of the recent editions, it's probably current: give it the full time its relevance deserves.
  - If it only appears in older editions, judge how relevant it still is. A topic that has matured into a widely used foundation can still deserve real time. A topic that has since been superseded, abandoned, or made moot (like a tool replaced by newer tools, or a migration that everyone finished years ago) gets a quick plan of 15'–30', no matter how important it once was. One example is [IE6 end-of-life](https://www.thoughtworks.com/radar/platforms/ie6-end-of-life). Such a plan is mostly historical: what the topic was, what role it played, what replaced it, and what lessons or ideas survive from it. It can have a single level, and no hands-on exercise.

### Pace

- Design for slow, thoughtful learning. Assume that the learner will re-read, pause/rewind videos, take notes, and pick up on new threads. Estimate every activity at about **three times** the time needed to just read, watch or do the content. For example, two 30' videos take about 3 hours, a 10-minute article takes about 30 minutes, and hands-on exercises take at least three times what you'd expect.

### Trusted sources

- The `Thoughtworks Radar` folder lists all the Radar's topics by edition.
- You can include brief courses from the following sources, even paid ones, as long as they are relevant and high quality. If one is especially relevant but doesn't fit the time budget, you can recommend it in "Recommendation for future learning".
  * Coursera
  * DeepLearning.AI
  * Pluralsight

### Avoided sources

- None yet.

### Link style

- The learner opens plans as notes in Obsidian. Name each file after its topic, like "Model Context Protocol (MCP).md", and don't add a Markdown level-1 title inside (like `# MCP`): Obsidian shows the file name as the title.
- Link between plans with Obsidian links, like `[[Agent Skills]]`, or `[[Agent Scan|MCP-Scan]]` when a plan covers a topic under another name.
- Use standard Markdown links for everything else, such as resources and blips.

## Steps

1. **Find the blip.** If the learner gave the blip's URL, that's the blip. Otherwise, look for it in the `Thoughtworks Radar` folder. A blip can use a different name for the topic (for example, Grafana Agent is in the Radar as Grafana Alloy), so match the topic, not just the name. But if the Radar has a blip under the name the learner used, that's the blip, even if another blip seems to cover the same topic: blips that the Radar lists separately stay separate. Every topic should have a blip, so if you can't find one, something is wrong: maybe the learner misspelled the topic, or the folder is missing an edition. Don't write the plan. Tell the learner that you found no blip, and list any close matches in the folder.

2. **Pin down the inputs.** Get the topic and time budget from the arguments. If the budget is missing, choose one with the rules on default length in the learning preferences and state it in one line, so the learner can change it. If the learner's background is unclear, state your assumption in one line instead of asking.

3. **Cover what the blip highlights.** List everything the blip explicitly mentions or links to: concepts, tools, criticisms, related specs. Each one must end up in the plan: in a level, in "If you have extra time", in the recommendation for future learning, or as a related topic with its own plan. Skip one only for a clear reason, such as time or scope, duplicated information, or obsolescence, and state that reason in one line in the plan, so the learner knows it was a choice and not an oversight.

4. **Add the current state of the topic.** Before Level 1, add a section headed `## Current state of the topic (as of <date>)`, so the learner knows what they're getting into before they start. The date is when you wrote the section, in ISO format. In one short paragraph, tell the learner what they need to know that the activities won't make clear: Is the topic still relevant today? Did anything major happen to it, like a rename, an acquisition, or an open-source product going commercial? Was it superseded by a competing technology? Is it still changing fast? Don't repeat what the levels teach. When you update the paragraph, update its date too.

5. **Split the time into levels that go progressively deeper**, usually 2–4, depending on the topic.

   - **Each level must leave the learner with usable knowledge**, so they can stop after any level. If time is tight, then have a minimum of two levels. The exception is a quick historical plan for an obsolete topic, which can have a single level.

   - **At a bare minimum, the levels should explain the _what_, _why_ and _how_ of the topic.** For example, Level 1 might cover what the topic is and why it exists, maybe with a short descriptive resource, a very short video video, a product page, etc. Level 2 could show how the topic works. Following levels go deeper: deeper explanations, hands-on experience, the role of the topic in the wider ecosystem, problems and issues, and so on. Note that these categories are just an indication. If they're not appropriate for a specific topic, go for something else.

   - **Give each level one theme.** Everything in a level should serve the theme in its title. If a level needs to cover two concerns, split it into subsections, each with its own consistent theme and title. Don't mix concerns in a level (for example, security resources in a "Build a server" level, or a changelog in a "Design" level): it makes the learning feel chaotic. If an item doesn't fit any level's theme, move it to "If you have extra time" or the recommendation for future learning.
   
   - **Start Level 1 with the blip, then a concrete example.** The blip is the first item of Level 1. The item after it should be short and concrete, such as a worked example, a demo, a quick look at a real artifact, or a tiny hands-on step. It can be a **Read**, a **Skim** or a **Do**. Its job is to give the learner a concrete anchor for the broader, more theoretical material that follows, so save the announcements, overviews and design rationale for after it.

6. **For each level, give:**
   - a heading with the time slot and estimated time, like `## Level 2 — How it works (0:45–1:15, ~30 min)`
   - a one-line **Goal** that says what the learner will be able to do
   - 1–4 **Read** / **Watch** resources, each with a link and a short reason it was picked
   - where practice fits the level, one hands-on **Do** exercise that ends with something concrete to produce, compare or decide, so the learner knows when it's done. Later exercises build on earlier ones.
7. **Curate resources carefully:**
   - A resource can be anything, including, but not limited to, a blog post, a conference talk, or a page of official documentation. Paid resources are fine only from the trusted sources in the learning preferences.
   - Follow the trusted and avoided sources in the learning preferences.
   - **Use only resources that look human-created.** This is a requirement, not a preference: never use content that looks LLM-generated, slop, content farms or SEO filler, even when it looks otherwise good. Some docs, including official ones, read as generated: verbose, overly detailed, meandering. Skip them in favor of a terse, well-structured narrative written by a person.
   - Prefer well-regarded conference talks and established authors. Follow these general preferences, but quality always wins, so make an exception when a resource is clearly better:
      * **Curated third-party explanations over official docs.** A good article by a respected practitioner usually explains a topic better than the reference page. Use official docs when they are the best explanation, or for the hands-on parts (quickstarts, tool pages).
      * **Short over long.** Pick the shortest resource that does the topic justice. Use a long one only when the topic really needs the length.
   - **Find every resource with a live web search, never from memory.** Even when you remember a good resource, search for it. Then fetch each page to confirm that it loads and contains what the plan says about it.
   - Always point to existing human-written or human-curated content instead of writing your own explanations or walkthroughs.
   - Use what you read when you fetched the page to say exactly how the learner should use it. A page that explains concepts or walks through an example is a **Read**. A page that mostly describes a tool, such as an overview or a reference of options, is a **Skim**. Tell the learner to skim it and try the tool for a few minutes, and let a later **Do** exercise give them real practice with it. For example: "Skim: MCP Inspector — skim the page, then launch the Inspector and click around. You'll use it properly in the exercise below."
   - Use **Skim** only for tool pages like these. Never ask the learner to skim dense conceptual material, such as a list of vulnerabilities or a spec that assumes background knowledge: skimming it leaves them with nothing they understand. Either make it a **Read** that fits the level and the learner's background, or leave it out (and, if it matters, point to it in the recommendation for future learning).
8. **Add one to three short "If you have extra time" activities**: For example, an additional video or blog post that the user can study if they want to know more about the topic.
9. **At the end, give your recommendation for future learning:**
   - Is the topic small and covered adequately by this plan?
   - Would you recommend having a longer self-study plan for this topic? How long? (Follow the rules on default length in the learning preferences.)
   - Is the topic so vast that you'd recommend splitting it into multiple smaller topics?
   - At the end of the recommendation, list all related topics in the Thoughtworks Radar. Make them plain list items, not checkboxes: they're pointers, not tasks, so the learner never has to come back to a finished plan to check them off. Follow the rule on structural links: link a topic that has a plan to the plan, like `[[Agent Skills]] (Apr 2026)`, and link a topic without a plan to its blip.
10. **Close with the blip.** End the file with a horizontal rule and this to-do item, linking the blip: `- [ ] **~10 min** · **Close:** [Review the blip](<blip URL>) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.`

Keep the whole plan scannable. It should go from a few lines to a screenful of text for a weekend-long plan.
