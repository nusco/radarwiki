- **Blip:** [Anchoring coding agents to a reference application](https://www.thoughtworks.com/radar/techniques/anchoring-coding-agents-to-a-reference-application)
- **Time:** ~45 minutes
- **Radar edition:** November 2025 and November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

The technique is the AI-era successor of service templates. Teams used to start new services from a template, but templates drift: dependencies and practices change, and old services fall behind. In 2025 Thoughtworks experimented with giving coding agents a live, compilable reference application as the source of examples, exposed through an MCP server. In November 2026 the idea moved to *Trial* and changed shape: keep scaffolding templates lean, and let agents look up current conventions at runtime from a central, maintained knowledge source, such as an [[Agent-maintained knowledge bases|agent-maintained knowledge base]] or [[OpenWiki]].

## Level 1 — What it is (~20 min)

Instead of baking conventions into templates or prompts, point the agent at something that's kept up to date, and let it copy from there.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/anchoring-coding-agents-to-a-reference-application) (~3 min) — read both versions. November 2025 anchors agents to a reference app through MCP, and November 2026 moves the conventions into knowledge sources the agent queries.
- [ ] **~10 min** · Read: [Anchoring AI to a reference application](https://martinfowler.com/articles/exploring-gen-ai/anchoring-to-reference.html) (Birgitta Böckeler, martinfowler.com, Sep 2025, ~3 min) — the experiment behind the first blip. Note two lessons: drift detection worked only when scoped to specific commits, and simple changes are better done with deterministic codemods than with AI.

## Level 2 — Try it (~25 min)

See the difference between describing a convention and showing a working example of it.

- [ ] **~25 min** · **Do:** Pick a convention that your projects share but implement inconsistently, like logging setup, error handling or the CI configuration. Choose the project that does it best as the reference. Then ask your coding agent to bring a second project in line with it, giving it the reference project's path (or a commit that introduced the convention). Compare with what the agent does when you only describe the convention in words.

## Wrap-up

This plan covers it. The technique depends on keeping the reference up to date, and that's the topic of [[Agent-maintained knowledge bases]].

## Review the blip

- [ ] **~5 min** · Re-read [Anchoring coding agents to a reference application](https://www.thoughtworks.com/radar/techniques/anchoring-coding-agents-to-a-reference-application) now that you know the topic.

## Related blips

- **[[OpenWiki]]**: one of the central, up-to-date sources that agents can query for current conventions.
- **[[Agent-maintained knowledge bases]]**: the other kind of source the November 2026 version points agents to.
