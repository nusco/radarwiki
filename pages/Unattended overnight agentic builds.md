- **Blip:** [Unattended overnight agentic builds](https://www.thoughtworks.com/radar/techniques/unattended-overnight-agentic-builds)
- **Time:** ~1 hour 15 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

By 2026, coding agents could work for hours on a feature without help, and some teams started to hand them work at the end of the day and review it in the morning. The blip is new in November 2026. It's less about the night than about what a team needs before it can trust an agent alone: a sandbox, a specification written up front, automated checks the agent can use to correct itself, and a way to validate more code than anyone can review line by line. The blip compares these requirements to the prerequisites for microservices. Few teams meet them all yet.

## Level 1 — What it is (~15 min)

Give one agent a feature-sized task when you leave, and review the result when you're back. If you can't, find out what's missing.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/unattended-overnight-agentic-builds) (~3 min) — list its prerequisites. The test it proposes is worth remembering: a team that can't leave an agent alone overnight probably isn't running fully autonomous work during the day either.
- [ ] **~10 min** · Read: [Microservice Prerequisites](https://martinfowler.com/bliki/MicroservicePrerequisites.html) (Martin Fowler, Aug 2014, ~3 min) — the analogy the blip uses. Read it to see the shape of the argument: a technique that's only safe once certain basics are in place.

## Level 2 — Run one (~1 hour)

Learn how practitioners prepare an overnight run, then try one.

- [ ] **~25 min** · Read: [Milestones, not tasks: how I run my agent overnight](https://leandrotocalini.github.io/vibe-shipping-diary/posts/overnight-agent-runs) (Leandro Tocalini Joerg, Feb 2026, 9 min) — a solo developer's working setup: specs written as milestones during the day, a script that runs them one by one at night, one commit per milestone. His main lesson is that the clarity of the spec decides the outcome.
- [ ] **~15 min** · Read: [What would make an overnight agent useful?](https://flaviocopes.com/overnight-agent-work/) (Flavio Copes, Nov 2026, ~5 min) — the other side: a good overnight job answers a named question, and its output is designed for the morning reader. Skip the promotions around the article.
- [ ] **~20 min** · **Do:** Write a brief for an overnight run on a side project: the goal, how the agent can check its own work (tests, a linter, a build), what it must not touch, and what you want to read in the morning. Run it in a sandbox before you stop for the day. Next morning, note how long the review took, and which prerequisite from the blip you'd fix first.

## Wrap-up

This plan covers the technique. Its prerequisites have their own plans: [[Agent sandboxing]], [[Spec-driven development]], [[Feedback sensors for coding agents]] and [[Harness quality evaluation]]. Where the agent runs is covered in [[Managed agents runtime]].

## Review the blip

- [ ] **~5 min** · Re-read [Unattended overnight agentic builds](https://www.thoughtworks.com/radar/techniques/unattended-overnight-agentic-builds) now that you know the topic.

## Related blips

- **[[Agent pipeline responsibility]]**: letting agents keep the build green is a complementary technique.
- **[[Managed agents runtime]]**: a natural place to run the overnight agent.
- **[[Harness quality evaluation]]**: a night's work is too large to review line by line, so the harness that validates it must be tested.
- **[[Coding agent swarms]]**: the blip notes that one agent is enough, without a swarm.
- **[[Feedback sensors for coding agents]]**: let the agent correct its own mistakes without a human.
- **[[Sandboxed execution for coding agents]]**: a prerequisite for leaving an agent alone.
- **[[Spec-driven development]]**: the work must be specified up front.
