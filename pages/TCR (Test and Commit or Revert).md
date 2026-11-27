- **Blip:** [TCR (Test && Commit || Revert)](https://www.thoughtworks.com/radar/techniques/tcr-test-commit-revert)
- **Time:** ~2 hours
- **Radar edition:** November 2025
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-27
- **Status:** #undone

This plan assumes that you know test-driven development (TDD).

---

## Current state (late 2026)

Kent Beck introduced TCR in 2018 as an experiment: run the tests after every change, commit if they pass, and throw the change away if they fail. It stayed a niche practice for coding dojos until coding agents arrived. An agent doesn't mind losing its work, and a hard revert keeps it from piling up broken changes, so in 2025 and 2026 people started to package TCR as agent skills and loops, Beck among them. That's why the blip appeared in late 2025.

## Level 1 — What it is (~15 min)

A test run that commits or reverts your change, so you learn to take tiny steps.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/tcr-test-commit-revert) (~1 min) — note the claim that TCR reinforces [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) and [KISS](https://en.wikipedia.org/wiki/KISS_principle), and the hint about GenAI.
- [ ] **~10 min** · Read: [test && commit || revert](https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864) (Kent Beck, Sep 2018, ~3 min) — the original article, linked from the blip. Notice how Beck answers his own objection: if you don't want a lot of code wiped out, don't write a lot of code between greens.

## Level 2 — Work in tiny steps (~1.25 hours)

See how TCR changes the way you program, then try it yourself.

- [ ] **~45 min** · Watch: [substring, TCR style](https://www.youtube.com/watch?v=ZrHBVTCbcE0) (Kent Beck, Jan 2019, ~16 min) — Beck solves a tricky little problem under TCR. Pause whenever a change gets reverted, and look at how he makes the next step smaller.
- [ ] **~30 min** · **Do:** Pick a small kata, such as Fibonacci or the substring problem from the video, and set up TCR with one of the ready-made scripts in [tcr-workshop](https://github.com/islomar/tcr-workshop) (islomar), which covers Python, Java, C#, Ruby, Go and more. Turn off auto-save in your editor first, as the README suggests. Solve the kata, then count how many of your changes got reverted, and write down what you'd do differently next time.

## Level 3 — TCR for coding agents (~30 min)

Use TCR to keep a coding agent's changes small and its tests green.

- [ ] **~10 min** · Read: [Test && Commit || Revert with AI](https://worksonmymachine.ai/p/test-and-and-commit-revert-with-ai) (Scott Werner, Mar 2025, ~3 min) — a small agent that runs a strict TCR loop: you write the tests, and the LLM writes code until they pass or gets reverted. Note the idea that tests become an "executable prompt".
- [ ] **~20 min** · **Do:** Take the TCR script from the exercise above and tell your coding agent to run it after every change, and never to edit the script or the tests. Give it the next step of the kata, or a small feature with a test you wrote. Then look at the Git history: are the agent's commits smaller than its usual changes? Did any reverts lead to a better approach?

## If you have extra time

- [ ] **~40 min** · Read: [How Practicing TCR (Test && Commit || Revert) Reduces Batch Size](https://www.infoq.com/articles/test-commit-revert) (Philippe Bourgau, InfoQ, Feb 2023, ~13 min) — two practitioners on using TCR for coaching and production work, including the downsides: you never see a test go red, and the history fills up with useless commit messages.
- [ ] **~35 min** · Watch: [Understanding Legacy Code with TCR](https://www.youtube.com/watch?v=FFzHOyFeovE) (Kent Beck, Oct 2019, ~12 min) — TCR used to write tests for code you didn't write, instead of new code.
- [ ] **~2.5 hours** · Watch: [Genie Sessions: TCR Skill](https://newsletter.kentbeck.com/p/genie-sessions-tcr-skill) (Kent Beck, Apr 2026, ~51 min) — a recording of a live session where Beck tries to get an AI agent to work TCR-style with a skill. It's unedited and meandering, but it's the inventor applying TCR to agents.

## Wrap-up

This plan covers it. If you use TCR with an agent, [[Agent Skills]] are a natural way to package the loop.

## Review the blip

- [ ] **~5 min** · Re-read [TCR (Test && Commit || Revert)](https://www.thoughtworks.com/radar/techniques/tcr-test-commit-revert) now that you know the topic.
