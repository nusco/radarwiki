- **Blip:** [Git AI](https://www.thoughtworks.com/radar/tools/git-ai)
- **Time:** ~40 minutes
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

As more code is written by agents, `git blame` stops telling the whole story: it shows who committed a line, not whether an agent wrote it, or why. Git AI is an open-source Git extension that records, line by line, which code came from which agent, model and prompt, stored with an open standard based on Git notes. Agents call it while they work, and the attribution follows the code through rebases and squashes. The blip moved from *Assess* to *Trial* in November 2026, because the record turned out useful for accountability and for understanding old code later.

## Level 1 — What it is (~15 min)

Track which lines in a repository an AI wrote, and keep the session behind them, so people and agents can later ask why the code is the way it is.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/git-ai) (~2 min) — read both versions. Note why checkpoints beat counting lines at commit time.
- [ ] **~10 min** · Skim: [Get Started with Git AI](https://usegitai.com/docs) (Git AI docs, ~5 min) — read the install steps, "How does it work?" and the table of limitations (some Git operations aren't tracked).

## Level 2 — Use it (~25 min)

- [ ] **~25 min** · **Do:** Install Git AI in a test repository, and make a change partly by hand and partly with your coding agent. Commit, then look at the attribution: which lines it marks as AI-written, and what session it links to. Then ask your agent why one of its lines is there, and see whether the archived session helps it answer.

## Wrap-up

This plan covers it. Recording whole agent sessions, rather than line attribution, is covered in [[Entire CLI]].

## Review the blip

- [ ] **~5 min** · Re-read [Git AI](https://www.thoughtworks.com/radar/tools/git-ai) now that you know the topic.
