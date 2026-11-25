- **Blip:** [AI-accelerated shadow IT](https://www.thoughtworks.com/radar/techniques/ai-accelerated-shadow-it)
- **Time:** ~30 minutes
- **Radar edition:** April 2025, November 2025, April 2026 and November 2026
- **Quadrant:** Techniques
- **Ring:** Caution (formerly Hold)
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

"Shadow IT" is the software people build or buy without the IT department: the spreadsheet that quietly runs the business is the classic example. AI made it much bigger. In 2025 the worry was no-code platforms with AI "duct tape". In 2026 non-developers moved on to agentic tools like Claude Cowork, and then to coding agents like Claude Code and Codex. The blip has been on every Radar since April 2025. Its tone has changed: from a warning, to advice on governance, to an explicit "don't extinguish their enthusiasm".

## Level 1 — What it is, and how to handle it (~30 min)

People outside IT build real software with AI, and it lacks the security, testing, pipelines and observability that real software needs, especially once a team depends on it.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/ai-accelerated-shadow-it) (~2 min per version) — read all four versions, newest first. Notice the shift in advice, from caution to governance to giving people safe places to experiment.
- [ ] **~20 min** · **Do:** List the AI-built tools you know of in your organization, or in a friend's: scripts, internal apps, automated workflows. For each one, note who depends on it, what data it touches, and who would fix it if it broke. Pick the riskiest, and write the one guideline or environment (like a sandbox or a shared catalog) that would have prevented its biggest risk.

## Wrap-up

This plan covers it. Giving people a safe, shared setup to experiment in is covered in [[Enterprise harness]].

## Review the blip

- [ ] **~5 min** · Re-read [AI-accelerated shadow IT](https://www.thoughtworks.com/radar/techniques/ai-accelerated-shadow-it) now that you know the topic.

## Related blips

- **[[OpenAI Codex]]**: one of the coding agents that non-developers have moved on to.
- **[[Enterprise harness]]**: the blip recommends enterprise harnesses as safe environments for experimentation.
- **[[Claude Code]]**: the other coding agent the blip names.
