- **Blip:** [spartan/ui](https://www.thoughtworks.com/radar/languages-and-frameworks/spartan-ui)
- **Time:** ~30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know Angular.

---

## Current state (late 2026)

In the React world, shadcn/ui changed how teams use component libraries: instead of installing styled components as a dependency, you copy them into your own code and own them, on top of unstyled, accessible building blocks. spartan/ui brings that approach to Angular. Its "brain" layer, installed from npm, handles accessibility, behavior and state. Its "helm" layer, styled with Tailwind, is copied into your project. It reached 1.0 in June 2026. The blip is new in November 2026: one team used it as the base of a branded component library, but hit rough edges when upgrading copied components with its CLI.

## Level 1 — What it is (~10 min)

shadcn's approach for Angular: accessible primitives from npm, styled components you own.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/spartan-ui) (~1 min) — note why it's a credible alternative to Angular Material.
- [ ] **~5 min** · Read: [Introduction](https://spartan.ng/documentation) (spartan docs, ~2 min) — how the brain and helm layers split the work.

## Level 2 — Try it (~20 min)

- [ ] **~20 min** · **Do:** In an Angular project, add spartan/ui and two components, such as a button and a dialog, following its installation docs. Change the styling of one in your own code. Then think about the upgrade problem the blip mentions: what happens when the library changes a component you've already edited?

## Wrap-up

This plan covers it. The React original has its own plan, [[shadcn]].

## Review the blip

- [ ] **~5 min** · Re-read [spartan/ui](https://www.thoughtworks.com/radar/languages-and-frameworks/spartan-ui) now that you know the topic.

## Related blips

- **[[shadcn]]**: the React approach that spartan/ui applies to Angular.
- **[[Angular]]**: the framework spartan/ui is built for.
