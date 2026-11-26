- **Blip:** [Apple container](https://www.thoughtworks.com/radar/tools/apple-container)
- **Time:** ~35 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you've used Docker, and that you have an Apple silicon Mac.

---

## Current state (late 2026)

On a Mac, Linux containers usually run inside one shared Linux virtual machine, managed by Docker Desktop or alternatives like Colima. Apple container, an open-source Swift tool from Apple, takes a different approach: each container gets its own lightweight VM, which isolates containers better and gives memory back to macOS when a container stops. It also avoids Docker Desktop's licensing. It needs Apple silicon and a recent macOS (26 or later), and it isn't Docker-compatible out of the box: community bridges like Socktainer fill that gap. The blip is new in November 2026.

## Level 1 — What it is (~10 min)

Run Linux containers on a Mac, each in its own lightweight virtual machine.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/apple-container) (~1 min) — note the use case it highlights: local [[Testcontainers]] setups that need fast starts and strict resource limits.
- [ ] **~5 min** · Skim: [container](https://github.com/apple/container) (Apple, README) — the requirements and "Get started". Note the support boundaries: Apple silicon only, and compatibility only within a major version.

## Level 2 — Try it (~25 min)

- [ ] **~25 min** · **Do:** Install it, start it with `container system start`, and run `container run --rm alpine echo hello`. Then run a container you normally run with Docker, and compare start time and memory use in Activity Monitor. Decide whether you could replace your current setup, or what you'd miss (for example, Docker API compatibility).

## Wrap-up

This plan covers it. Containers as an isolation boundary for agents are covered in [[Agent sandboxing]].

## Review the blip

- [ ] **~5 min** · Re-read [Apple container](https://www.thoughtworks.com/radar/tools/apple-container) now that you know the topic.

## Related blips

- **[[Testcontainers]]**: Apple container works well for local Testcontainers setups.
