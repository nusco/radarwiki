- **Blip:** [SolidJS](https://www.thoughtworks.com/radar/languages-and-frameworks/solidjs)
- **Time:** ~1 hour 20 minutes
- **Radar edition:** April 2023 and November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know a component-based UI framework, such as React.

---

## Current state (late 2026)

SolidJS, created by Ryan Carniato, looks a lot like React, but works differently: there's no virtual DOM, components run only once, and "signals" update exactly the parts of the page that depend on them. That "fine-grained reactivity" influenced the whole frontend world, and by 2026 several major frameworks had adopted signals. The Radar first covered Solid in 2023. It returns in November 2026 after Solid 2.0, released that month, which builds asynchronous data loading into the framework, with control over the order in which loading parts of the page appear. SolidStart is its full-stack framework, much as Next.js is for React.

## Level 1 — What it is (~10 min)

A UI library where signals update exactly what changed, without a virtual DOM.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/solidjs) (~1 min per version) — read both versions. 2023 explains the model, and 2026 the new async features.

## Level 2 — How reactivity works (~1 hour 10 minutes)

Learn Solid's mental model, then try it.

- [ ] **~45 min** · Read: [Reactivity](https://docs.solidjs.com/concepts/reactivity) (SolidJS docs, Nov 2026, ~15 min) — signals, derived values, effects and when updates happen, with a "Common problems" section that shows where React habits lead you astray. It's the core of the framework.
- [ ] **~25 min** · **Do:** Work through the first lessons of the [Solid tutorial](https://docs.solidjs.com/tutorial/), which runs in your browser, up to signals and memos. Then build a small counter that also shows a derived value, and add a `console.log` in the component body: notice that it runs only once.

## Wrap-up

This plan is enough for a generalist, unless you're choosing a frontend framework.

## Review the blip

- [ ] **~5 min** · Re-read [SolidJS](https://www.thoughtworks.com/radar/languages-and-frameworks/solidjs) now that you know the topic.
