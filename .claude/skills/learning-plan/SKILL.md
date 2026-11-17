---
name: learning-plan
description: Create a self-study plan, organized in progressive levels, for a short technical topic (30' to a weekend), with curated videos and articles. Use when the user asks for a learning plan, study plan, or how to learn a technical topic quickly.
argument-hint: "[topic] [time budget]"
---

# Learning plan

Create a self-study plan for: $TOPIC, with a specific $TIME_BUDGET

## Standing rules

- **Follow the user preferences.** Before you write or update a plan, look for a `preferences.md` file in the wiki's root folder (the folder that contains `pages`). If it exists, this file holds the learner's default length, pace, trusted and avoided sources, link style and rituals, and every plan must follow it. When the learner's preferences disagrees with the file, the preferences win for that plan. If the file is missing, say so in one line, and ask the learner for anything you can't decide without it.
- The $TOPIC can be a literal topic ("Zero trust architecture") or a URL referring to it (https://www.thoughtworks.com/radar/techniques/zero-trust-architecture)
- Write the plan to a Markdown file in the `pages` folder. Name the file, and write its links, in the link style from the user preferences.
- List every activity (resources, **Do** exercises, "If you have extra time" items, and any items that the rituals add) as GitHub Markdown todo items, so the learner can tick them off to track progress.
- Structure the file logically, beginning with the topic and the time required.
- Open the file with metadata, one field per line:
  ```
  **Time:** ~45 minutes
  **Source:** [Serena](https://oraios.github.io/serena/)
  **Created:** 2026-10-21
  ```
  **Source** links where the topic came from. The rituals in the user preferences can replace it with other fields.
  **Created** is today's date in ISO format. Keep this date when you revise the plan later. Use it to tell how old the plan's time-sensitive parts are, such as "Current state of the topic", before you update them.
- Size the content so that it fits the time budget at the pace in the user preferences.
- **Give every activity a time estimate.** Start each to-do item with how long the learner will spend on the activity, in bold and followed by a middle dot, like `- [ ] **~25 min** · Read: [Title](URL) (Author, Oct 2025, ~8 min) — ...`. This applies to every to-do item: resources, **Do** exercises, "If you have extra time" items, and the items that the rituals add. Work out each estimate from the time the content strictly needs (the length of the article or video, or the bare work in an exercise), adjusted for the pace in the user preferences. Use round numbers, like ~5 min, ~20 min, ~1 hour or ~1.5 hours.
- **Give the nominal length too.** Next to the link of each video or article, give the length of the resource itself, when you know it, so the learner can tell the resource's length apart from the time the activity takes.
- **Make the estimates add up.** Each level's estimate in its heading is roughly the sum of its activities' estimates, and **Time** is the sum of the levels. "If you have extra time" items and items outside the levels, such as the ones that the rituals add at the end, don't count toward **Time**.
- **Tell the learner what to do when they can't decide for themselves.** Every activity should leave the learner knowing what to do next. Options are fine, such as an optional extra resource or an alternative exercise, as long as the plan gives the learner the means to choose: what each option offers that the other doesn't, who or what situation it suits, and how long it takes. Don't hedge: if the learner could only make the choice by trying every option first, make it for them. For example, don't mention an alternative resource with a vague caveat ("the blip links to another article, but it's partly paywalled"). Decide where it belongs (in a level, in "If you have extra time", or left out with a reason) and say what it adds.
- When you choose or suggest a time budget, follow the rules on default length in the user preferences.
- If the learner gave a time budget that seems inappropriate (too long for an obsolete topic, or too short for an important one) supersede it with your own estimate, but explicitly say so in one line so the learner can push back or ask you to change the estimate.
- Plans must work well together. Before you write a plan, look at the existing plans in the `pages` folder. If the new topic is related to one of them, link to it. Assume what the earlier plan covers instead of repeating it, avoid reusing its resources, and build the exercises on the earlier plan's exercises when that makes sense. Keep one plan per topic: two tools that your sources list separately get two plans.
- Treat the plans as a wiki: link material, don't duplicate it. When two topics overlap, put each resource, exercise or explanation in the one plan where it fits best, usually the plan whose topic is about it. In the other plan, add a short explicit pointer that says what it will find there (for example, "Mapping the trifecta across your whole setup is covered in [[Toxic flow analysis for AI]]"). Make an exception only when removing the material would leave a big hole in a topic. In that case, keep a brief version (one resource or a one-line recap) and link to the full treatment.
  - This works in both directions. When you write a new plan, check whether existing plans already cover its material. If one does, move that material into the new plan, even if the learner has already ticked it off: move it as it is, still ticked, so their progress stays. Replace the moved material with a pointer, and fix any "Assumption:" line that no longer holds.
  - If a related topic has no plan yet, an existing plan can cover it briefly. When that topic gets its own plan, apply the rule above.
- **Structural links go to plans, not sources.** A structural link is one that helps the learner find their way between topics, such as the related topics in "Recommendation for future learning", a series list, or an entry in an index file (for example, a hypothetical `Index.md` listing all topics). When a topic has a plan, make that link a link to the plan, and don't add a second link to the topic's source next to it. Link to the source itself only when the learner needs to read it: the **Source** metadata line, a reading resource inside a level, or wherever a ritual asks for it. A topic that has no plan yet keeps its source link. When you write a new plan, replace the structural links to its source in the other plans and in any index file, such as `Index.md`, if one exists, with links to the new plan.

## Maintaining existing plans

- **Update existing plans when needed.** Whenever a change in the system is inconsistent with the existing plans (for example, because the user asked for changes that lead you to update this skill), update the existing plans in the `pages` folder to follow the new version, without waiting for the learner to ask. If an update could be destructive, such as losing progress on a plan the learner has started, explain the problem plainly and ask before you make it. Describe the change in natural language, not as a code diff or another proposal that's hard to judge at a glance.

- **Keep in-progress plans stable.** When you change a plan where some items are already ticked off, preserve the ticked items. Never untick an item without asking the learner. If a change would substantially alter a ticked item, describe the issue to the learner and let them decide.

- **Leave completed plans alone.** A plan where every item is ticked off, ignoring the optional "If you have extra time" items, is done: don't update it automatically, and don't add new items that would return it to into "in progress". This includes the changes that the wiki rules above would make, such as moving material out of the plan or updating its structural links. If you think a completed plan really needs a change, ask the learner specifically.

## Steps

1. **Pin down the inputs.** Get the topic and time budget from the arguments. If the budget is missing, choose one with the rules on default length in the user preferences and state it in one line, so the learner can change it. If the learner's background is unclear, state your assumption in one line instead of asking.

2. **Cover what the source highlights.** If the topic comes from a specific source, such as an article or a Radar blip, list everything the source explicitly mentions or links to: concepts, tools, criticisms, related specs. Each one must end up in the plan: in a level, in "If you have extra time", in the recommendation for future learning, or as a related topic with its own plan. Skip one only for a clear reason, such as time or scope, duplicated information, or obsolescence, and state that reason in one line in the plan, so the learner knows it was a choice and not an oversight.

3. **Split the time into levels that go progressively deeper**, usually 2–4, depending on the topic.

   - **Each level must leave the learner with usable knowledge**, so they can stop after any level. If time is tight, then have a minimum of two levels. The exception is a quick historical plan for an obsolete topic, which can have a single level.

   - **At a bare minimum, the levels should explain the _what_, _why_ and _how_ of the topic.** For example, Level 1 might cover what the topic is and why it exists, maybe with a short descriptive resource, a very short video video, a product page, etc. Level 2 could show how the topic works. Following levels go deeper: deeper explanations, hands-on experience, the role of the topic in the wider ecosystem, problems and issues, and so on. Note that these categories are just an indication. If they're not appropriate for a specific topic, go for something else.

   - **Give each level one theme.** Everything in a level should serve the theme in its title. If a level needs to cover two concerns, split it into subsections, each with its own consistent theme and title. Don't mix concerns in a level (for example, security resources in a "Build a server" level, or a changelog in a "Design" level): it makes the learning feel chaotic. If an item doesn't fit any level's theme, move it to "If you have extra time" or the recommendation for future learning.
   
   - **Start Level 1 with a concrete example.** After any opening items that the rituals ask for, the first item should be short and concrete, such as a worked example, a demo, a quick look at a real artifact, or a tiny hands-on step. It can be a **Read**, a **Skim** or a **Do**. Its job is to give the learner a concrete anchor for the broader, more theoretical material that follows, so save the announcements, overviews and design rationale for after it.

4. **For each level, give:**
   - a heading with the time slot and estimated time, like `## Level 2 — How it works (0:45–1:15, ~30 min)`
   - a one-line **Goal** that says what the learner will be able to do
   - 1–4 **Read** / **Watch** resources, each with a link and a short reason it was picked
   - where practice fits the level, one hands-on **Do** exercise, with later exercises building on earlier ones
5. **Curate resources carefully:**
   - A resource can be anything, including, but not limited to, a blog post, a conference talk, or a page of official documentation. Paid resources are fine only when the user preferences trust them.
   - Follow the trusted and avoided sources in the user preferences.
   - **Use only resources that look human-created.** This is a requirement, not a preference: never use content that looks LLM-generated, slop, content farms or SEO filler, even when it looks otherwise good. Some docs, including official ones, read as generated: verbose, overly detailed, meandering. Skip them in favor of a terse, well-structured narrative written by a person.
   - Prefer well-regarded conference talks and established authors. Follow these general preferences, but quality always wins, so make an exception when a resource is clearly better:
      * **Curated third-party explanations over official docs.** A good article by a respected practitioner usually explains a topic better than the reference page. Use official docs when they are the best explanation, or for the hands-on parts (quickstarts, tool pages).
      * **Short over long.** Pick the shortest resource that does the topic justice. Use a long one only when the topic really needs the length.
   - **Find every resource with a live web search, never from memory.** Even when you remember a good resource, search for it. Then fetch each page to confirm that it loads and contains what the plan says about it.
   - Always point to existing human-written or human-curated content instead of writing your own explanations or walkthroughs.
   - Use what you read when you fetched the page to say exactly how the learner should use it. A page that explains concepts or walks through an example is a **Read**. A page that mostly describes a tool, such as an overview or a reference of options, is a **Skim**. Tell the learner to skim it and try the tool for a few minutes, and let a later **Do** exercise give them real practice with it. For example: "Skim: MCP Inspector — skim the page, then launch the Inspector and click around. You'll use it properly in the exercise below."
   - Use **Skim** only for tool pages like these. Never ask the learner to skim dense conceptual material, such as a list of vulnerabilities or a spec that assumes background knowledge: skimming it leaves them with nothing they understand. Either make it a **Read** that fits the level and the learner's background, or leave it out (and, if it matters, point to it in the recommendation for future learning).
6. **Add one to three short "If you have extra time" activities**: For example, an additional video or blog post that the user can study if they want to know more about the topic.
7. **At the end, give your recommendation for future learning:**
   - Is the topic small and covered adequately by this plan?
   - Would you recommend having a longer self-study plan for this topic? How long? (Follow the rules on default length in the user preferences.)
   - Is the topic so vast that you'd recommend splitting it into multiple smaller topics?
8. **Apply the rituals.** Add every ritual from the user preferences, in the place it asks for.

Keep the whole plan scannable. It should go from a few lines to a screenful of text for a weekend-long plan.
