- **Blip:** [Risk-tiered human oversight](https://www.thoughtworks.com/radar/techniques/risk-tiered-human-oversight)
- **Time:** ~1 hour
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

As coding agents produce more changes than people can review carefully, teams have started to sort changes by risk and spend human attention where it matters. The idea isn't new: change management in operations has long sorted changes into standard, normal and emergency. What's new is applying it to agent output, and having large companies report on it. In 2026 Meta published how it lets an automated pipeline review and land low-risk code changes, and AWS added tiered oversight to its guidance for agentic systems. The blip is new in November 2026, and comes with a *Caution* twin, [[Human-in-the-loop theater]], about what happens without it.

## Level 1 — What it is (~25 min)

Match the depth of review to what a change could break: humans apply the riskiest changes, review the medium ones, and let agents merge the low-risk ones through CI.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/risk-tiered-human-oversight) (~2 min) — note the two ways to decide the tier: zones of the codebase that always need more review, and an LLM that classifies each change, which is fallible.
- [ ] **~20 min** · Read: [Establish tiered human oversight and approval workflows](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel02-bp05.html) (AWS Well-Architected, ~4 min) — the page the blip links to. Read "Desired outcome", "Common anti-patterns" and "Implementation steps", and skip the list of AWS services. Its three tiers (autonomous, notify, approve) and its focus on reversibility are the core of the technique.

## Level 2 — How Meta does it (~35 min)

See the technique at scale, with numbers, and apply it to your own codebase.

- [ ] **~15 min** · Read: [Automating Low-Risk Code Review at Meta](https://arxiv.org/abs/2605.30208) (Chris Adams and others, Meta, May 2026) — the process the blip mentions. Read the abstract only (~2 min): a pipeline that scores each change for risk, has an LLM review the low-risk ones, and lands them, with fewer reverts than the changes reviewed by people. Then skim the paper's figures if you want to see how the risk threshold changes the results.
- [ ] **~20 min** · **Do:** For a repository you know, write a short risk policy with three tiers. List the zones that always need a human (for example, authentication, payments, migrations, CI configuration), what counts as low-risk, and what an agent may merge on its own after CI passes. Then check your last ten merged changes against it: how many would have needed less review than they got, and how many more?

## Wrap-up

This plan covers the technique. What goes wrong when a human approves changes they can't really judge is covered in [[Human-in-the-loop theater]].

## Review the blip

- [ ] **~5 min** · Re-read [Risk-tiered human oversight](https://www.thoughtworks.com/radar/techniques/risk-tiered-human-oversight) now that you know the topic.

## Related blips

- **[[Human-in-the-loop theater]]**: reviewing everything with the same intensity ends in theater, and risk tiers are the way out.
