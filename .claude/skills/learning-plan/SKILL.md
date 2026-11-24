---
name: learning-plan
description: Create a self-study plan, organized in progressive levels, for a Thoughtworks Technology Radar blip (30' to a weekend), with curated videos and articles. Use when the user asks for a learning plan, study plan, or how to learn a Radar blip or technical topic quickly.
argument-hint: "[topic] [time budget]"
---

# Learning plan

Create a self-study plan for the Thoughtworks Technology Radar blip on: $TOPIC, with a specific $TIME_BUDGET

## Standing rules

- **Follow the template and the guide.** [`templates/template.md`](../../../templates/template.md) is the layout of every plan: its sections in order, with text in `{curly braces}` describing what goes there. [`templates/Learning plan.md`](../../../templates/Learning%20plan.md) says how to fill it in: writing rules, what each section holds, and the learner's learning preferences (default length, pace, trusted and avoided sources, link style). Read both before you write or change a plan, and follow them in every plan. When a request asks for something different, the request wins for that plan.
- The $TOPIC can be a literal topic ("Zero trust architecture") or a URL referring to it (https://www.thoughtworks.com/radar/techniques/zero-trust-architecture)
- Write the plan to a Markdown file in the `pages` folder. Name the file, and write its links, in the link style from the learning preferences.
- Plans must work well together. Before you write a plan, look at the existing plans in the `pages` folder. If the new topic is related to one of them, link to it. Assume what the earlier plan covers instead of repeating it, avoid reusing its resources, and build the exercises on the earlier plan's exercises when that makes sense. Keep one plan per topic: two tools that your sources list separately get two plans.
- Treat the plans as a wiki: link material, don't duplicate it. When two topics overlap, put each resource, exercise or explanation in the one plan where it fits best, usually the plan whose topic is about it. In the other plan, add a short explicit pointer that says what it will find there (for example, "Mapping the trifecta across your whole setup is covered in [[Toxic flow analysis for AI]]"). Make an exception only when removing the material would leave a big hole in a topic. In that case, keep a brief version (one resource or a one-line recap) and link to the full treatment.
  - This works in both directions. When you write a new plan, check whether existing plans already cover its material. If one does, move that material into the new plan, even if the learner has already ticked it off: move it as it is, still ticked, so their progress stays. Replace the moved material with a pointer, and fix any "Assumption:" line that no longer holds.
  - If a related topic has no plan yet, an existing plan can cover it briefly. When that topic gets its own plan, apply the rule above.
- **Structural links go to plans, not sources.** A structural link is one that helps the learner find their way between topics, such as the "Related Radar topics" list, a series list, or an entry in an index file (for example, a hypothetical `Index.md` listing all topics). When a topic has a plan, make that link a link to the plan, and don't add a second link to the topic's blip next to it. Link to the blip itself only when the learner needs to read it: the **Blip** metadata line, a reading resource inside a level, or the first item of Level 1 and the "Review the blip" item. A topic that has no plan yet keeps its blip link. When you write a new plan, replace the structural links to its blip in the other plans and in any index file, such as `Index.md`, if one exists, with links to the new plan.

## Keeping up with the Radar

Before you write or revise a plan, check that the `Thoughtworks Radar` folder has the latest edition. The folder has one file per edition, numbered by volume, like `034-thoughtworks-radar-2026-april.md`. Run the download script from the folder, because it writes there.

1. **Check the date.** If the newest edition in the folder is less than 25 weeks old, go on with the request.
2. **Check the website.** Otherwise, run `python3 download-script/radar_to_todo.py < /dev/null`. It reads the [Radar archive](https://www.thoughtworks.com/radar/archive) and lists the published volumes, without downloading anything. If none is newer than the folder, go on with the request. While a Radar is late, you'll check on every request, and that's fine.
3. **Ask first.** If there are new editions, tell the learner which ones, and which existing plans they would change: read the blip page of each plan, and look for the new editions in its history. Then ask before you download anything or change any plan. If the learner says no, go on with the request.
4. **Download the new editions.** Run `printf '<volumes>\n' | python3 download-script/radar_to_todo.py`, with only the new volumes, like `35` or `35-36`. Never select a volume that's already in the folder: its file holds the learner's ticks. The script reads every blip page slowly, so the site doesn't block it. It can take an hour, so let it finish.
5. **Update the README.** Set its sentence on the edition to the newest one, like "Up to date with the Thoughtworks Radar, November 2026 (volume 35)."
6. **Update the plans.** For each plan whose blip appears in a new edition, even in the same ring, update everything that depends on the edition: **Radar edition** and **Ring** in the metadata, the current state paragraph and its date, and text that counts or names editions (like "read both versions"). This applies to completed plans too: these changes add no tasks and reset no progress. Leave alone blips that dropped out of the new edition, and don't write plans for new blips unless the learner asks.
7. Go on with the request.

## Maintaining existing plans

- **Update existing plans when needed.** Whenever a change in the system is inconsistent with the existing plans (for example, because the user asked for changes that lead you to update this skill), update the existing plans in the `pages` folder to follow the new version, without waiting for the learner to ask. If an update could be destructive, such as losing progress on a plan the learner has started, explain the problem plainly and ask before you make it. Describe the change in natural language, not as a code diff or another proposal that's hard to judge at a glance.

- **Except for changes to the template.** The learner edits `templates/template.md` and `templates/Learning plan.md` to change the style of the wiki, and there can be hundreds of plans. So a change to either file doesn't update the existing plans by itself: update them only when the learner asks. The rules above and below still apply when you do.

- **Keep in-progress plans stable.** When you change a plan where some items are already ticked off, preserve the ticked items. Never untick an item without asking the learner. If a change would substantially alter a ticked item, describe the issue to the learner and let them decide.

- **Leave completed plans alone.** A plan where every item is ticked off, ignoring the optional "If you have extra time" items, is done: don't update it automatically, and don't add new items that would return it to into "in progress". This includes the changes that the wiki rules above would make, such as moving material out of the plan or updating its structural links. If you think a completed plan really needs a change, ask the learner specifically. The one exception is the update for a new Radar edition, in [Keeping up with the Radar](#keeping-up-with-the-radar).

## Steps

1. **Find the blip.** If the learner gave the blip's URL, that's the blip. Otherwise, look for it in the `Thoughtworks Radar` folder. A blip can use a different name for the topic (for example, Grafana Agent is in the Radar as Grafana Alloy), so match the topic, not just the name. But if the Radar has a blip under the name the learner used, that's the blip, even if another blip seems to cover the same topic: blips that the Radar lists separately stay separate. Every topic should have a blip, so if you can't find one, something is wrong: maybe the learner misspelled the topic, or the folder is missing an edition. Don't write the plan. Tell the learner that you found no blip, and list any close matches in the folder.

2. **Pin down the inputs.** Get the topic and time budget from the arguments. If the budget is missing, choose one with the rules on default length in the learning preferences. If the learner gave a budget that seems inappropriate (too long for an obsolete topic, or too short for an important one), supersede it with your own estimate. If the learner's background is unclear, assume one instead of asking. `templates/Learning plan.md` says how to state each of these choices in the plan, so the learner can push back.

3. **Cover what the blip highlights.** List everything the blip explicitly mentions or links to: concepts, tools, criticisms, related specs. Each one must end up in the plan: in a level, in "If you have extra time", in the wrap-up, or as a related topic with its own plan. Skip one only for a clear reason, such as time or scope, duplicated information, or obsolescence, and state that reason in one line in the plan, so the learner knows it was a choice and not an oversight.

4. **Find the resources.** `templates/Learning plan.md` says which resources to prefer and how to present them. Whatever it says, these rules always hold:
   - **Find every resource with a live web search, never from memory.** Even when you remember a good resource, search for it. Then fetch each page to confirm that it loads and contains what the plan says about it.
   - **Use only resources that look human-created.** This is a requirement, not a preference: never use content that looks LLM-generated, slop, content farms or SEO filler, even when it looks otherwise good. Some docs, including official ones, read as generated: verbose, overly detailed, meandering. Skip them in favor of a terse, well-structured narrative written by a person.
   - Always point to existing human-written or human-curated content instead of writing your own explanations or walkthroughs.
   - Follow the trusted and avoided sources in the learning preferences.

5. **Write the plan** following the template, section by section, and the guidance for each section in `templates/Learning plan.md`.
