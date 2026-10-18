---
name: learning-plan
description: Create a layered self-study plan for a short technical topic (a few hours to a weekend), with curated videos and articles. Use when the user asks for a learning plan, study plan, or how to learn a technical topic quickly.
argument-hint: "[topic] [time budget]"
---

# Learning plan

Create a self-study plan for: $TOPIC, with a specific $TIME_BUDGET

## Standing rules

- The $TOPIC can be a literal topic ("Zero trust architecture") or a URL referring to it (https://www.thoughtworks.com/radar/techniques/zero-trust-architecture)
- Write the plan to a Markdown file.
- In the file, use Markdown syntax for links. Also, list resources as GitHub Markdown todo items.
- Structure the file logically, beginning with the topic and the time required.
- Have the file name communicate the topic, as in "test-driven-development-learning-plan.md".
- The learner might be a slow reader/learner, so don't be tight with the time. For example, don't assume they'll take one hour to consume two 30' videos. It's more likely they'll rewind at times or pause to take notes, so they're more likely to take maybe 1.5 hours overall.

## Steps

1. **Pin down the inputs.** Get the topic and time budget from the arguments. If the budget is missing, ask the learner. If the learner's background is unclear, state your assumption in one line instead of asking.
2. **Split the time into 2–4 layers**, from fundamentals (that might be just one short description or a 5 minutes video) to applied use. Each layer must leave the learner with something usable, so they can stop after any layer. If time is tight, then have a minimum of two layers.
3. **For each layer, give:**
   - a heading with the time slot and estimated hours
   - a one-line **Goal**
   - 1–4 **Read** / **Watch** resources, each with a link and a short reason it was picked
   - in levels 3-4, one hands-on **Do** exercise, with later exercises building on earlier ones
4. **Curate resources carefully:**
   - Prefer official docs, well-regarded conference talks, and established authors.
   - Use only resources you are confident exist. Verify any you are unsure of with a web search.
   - Give video lengths when you know them.
5. **Close with a short "If you have extra time" note**.

Keep the whole plan scannable. It should go from a few lines to a screenful of text for a weekend-long plan.
