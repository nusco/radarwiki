- **Blip:** [Figma Code Connect](https://www.thoughtworks.com/radar/tools/figma-code-connect)
- **Time:** ~30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know what a design system is, and that you've seen Figma.

---

## Current state (late 2026)

Design-to-code tools usually turn a Figma frame into raw markup that ignores the components a team already has. Figma Code Connect links each Figma component to the real component in code, so that Figma's Dev Mode, and AI agents reading designs through Figma's MCP server, see the actual component and its props. The blip is new in November 2026, and comes from a Thoughtworks team that used it on a mobile design system. It needs a paid Figma plan, and the mappings need upkeep. Figma has also deprecated its framework-specific parsers in favor of template files, so older examples are out of date.

## Level 1 — What it is, and where it fits (~15 min)

Map design components to code components, so that generated code uses your design system instead of guessing.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/figma-code-connect) (~2 min) — note how the team used it: mappings for iOS and Android, published from CI, with checks for drift. Note the limits too: it works at component level, not for whole screens.
- [ ] **~5 min** · Skim: [Code Connect](https://github.com/figma/code-connect) (Figma, README) — read the deprecation notice, the plan requirements, and the links to the guides for each platform.

## Level 2 — Check your own components (~15 min)

See how an agent handles your design system today, and what a mapping would change.

- [ ] **~15 min** · **Do:** If your team has a design system in Figma, pick three components and check how a coding agent writes them today from a Figma link: does it use your components, or raw markup? Write down what a Code Connect mapping would change. If you have no design system, write down which parts of the blip's setup (CI publishing, drift checks, lint rules) you'd need first.

## Wrap-up

This plan is enough unless you work on a design system. In that case, follow the Code Connect guide for your platform.

## Review the blip

- [ ] **~5 min** · Re-read [Figma Code Connect](https://www.thoughtworks.com/radar/tools/figma-code-connect) now that you know the topic.
