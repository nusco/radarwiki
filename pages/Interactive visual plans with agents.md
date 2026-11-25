- **Blip:** [Interactive visual plans with agents](https://www.thoughtworks.com/radar/techniques/interactive-visual-plans-with-agents)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

Coding agents usually present their plans as long Markdown text, which is hard to review. In 2026 developers started asking agents for plans as self-contained HTML pages instead, with diagrams, user flows and wireframes, and tools and skills appeared to make that routine. The blip is new in November 2026. It comes with a warning: a rich plan can tempt you into big upfront design, while the technique works best for small, verifiable steps.

## Level 1 — What it is (~10 min)

Ask the agent for a plan you can look at and click through, not just read, and review it before the agent writes code.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/interactive-visual-plans-with-agents) (~1 min) — note the two uses: a plan before the change, and a visual recap after, which is most useful when the implementation drifted from the plan.
- [ ] **~5 min** · Read: [Tip #34: Ask for HTML, not just text](https://kjetiljd.github.io/ai-for-coding/tips/034-ask-for-html/) (Kjetil J.D., May 2026, 2 min) — the simplest form of the technique, with a prompt you can copy. You don't need any tool to start.

## Level 2 — Try it (~35 min)

Compare a visual plan with a text plan for the same change.

- [ ] **~5 min** · Skim: [/visual-plan](https://github.com/BuilderIO/skills/blob/main/skills/visual-plan/README.md) (Builder.io, ~3 min) — the skill the blip links to. Skim "What It Does" and "What Reviewers Get" to see what a full visual plan contains: diagrams, wireframes, API specs and a map of the files to change.
- [ ] **~30 min** · **Do:** Pick a change that touches a user interface or a data flow. Ask your agent for a plan twice: once as usual, and once as a single self-contained HTML file with diagrams and, if it fits, a wireframe. Open the HTML in a browser. Which plan helped you spot a wrong assumption faster? Write down one thing you'd only have caught in the visual one, or note that the text plan was enough.

## Wrap-up

This plan covers it. The technique is young, and it's mostly a matter of habit: the tools change quickly, while the prompt from Level 1 works with any agent.

I left out Builder.io's blog post about its plan tool: it's mostly a product pitch, and the skill's README covers the same features.

## Review the blip

- [ ] **~5 min** · Re-read [Interactive visual plans with agents](https://www.thoughtworks.com/radar/techniques/interactive-visual-plans-with-agents) now that you know the topic.
