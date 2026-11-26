- **Blip:** [Vale](https://www.thoughtworks.com/radar/tools/vale)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Vale is a linter for prose, and has been part of "docs as code" toolchains for years: it checks Markdown and other formats against style rules kept as YAML in the repository, in the editor and in CI. It's on the Radar in November 2026 because of AI: teams now get a flood of generated documents, and Vale can flag the phrasing typical of generated text, or act as a feedback sensor that lets an agent revise its own draft. Its checks are word and pattern matches, so they catch surface habits but not weak reasoning. It depends largely on one maintainer.

## Level 1 — What it is (~10 min)

A linter for writing: style rules as code, checked automatically.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/vale) (~2 min) — note the limits: deterministic patterns only.
- [ ] **~5 min** · Skim: [Vale](https://vale.sh/) (project site) — "Why Vale" and the section on agents.

## Level 2 — Lint some prose (~35 min)

- [ ] **~10 min** · Read: [Quickstart](https://docs.vale.sh/topics/quickstart) (Vale docs, ~4 min) — install, configure `.vale.ini`, sync a style package, and run it.
- [ ] **~25 min** · **Do:** Set up Vale on a folder of Markdown, such as this wiki's `pages`, with one of the packaged styles (Google or Microsoft). Add the [vale-ai-tells](https://github.com/tbhb/vale-ai-tells) package, which flags phrasing typical of AI text. Run it, and look at which warnings are useful and which are noise. Then ask your agent to fix one page using Vale's output, and check the result.

## Wrap-up

This plan covers it. Using checks like this to steer agents is covered in [[Feedback sensors for coding agents]].

## Review the blip

- [ ] **~5 min** · Re-read [Vale](https://www.thoughtworks.com/radar/tools/vale) now that you know the topic.

## Related blips

- **[[Feedback sensors for coding agents]]**: Vale works well as one, letting an agent revise its draft before anyone reads it.
