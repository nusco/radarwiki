- **Blip:** [F#](https://www.thoughtworks.com/radar/languages-and-frameworks/f)
- **Time:** ~1 hour
- **Radar edition:** April 2010 to October 2012 (six editions)
- **Quadrant:** Languages & Frameworks
- **Ring:** Assess
- **Updated:** 2026-11-27
- **Status:** #undone

The Radar last mentioned F# in 2012, and it never became mainstream, so this plan is short. It focuses on the idea from F# that matters most today: designing with types.

---

## Current state (late 2026)

F# is Microsoft's functional-first language for .NET, derived from OCaml. The blip tracked it in Assess for three years, together with Clojure and Scala, during the first wave of interest in functional programming. F# stayed a niche language, but a healthy one: it's open source and cross-platform, and it ships with every .NET release (F# 10 came with .NET 10 in November 2025). Its bigger influence is indirect. Its style of modeling a domain with records and unions, and of "making illegal states unrepresentable", spread well beyond F#, helped by Scott Wlaschin's writing.

## Level 1 — What it is (~25 min)

A concise, functional-first language that runs on .NET.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/f) (~2 min) — read all three versions. Note the 2012 advice: write the domain logic in F#, and keep the plumbing in C#.
- [ ] **~10 min** · Read: [Why use F#?](https://fsharpforfunandprofit.com/why-use-fsharp/) (Scott Wlaschin, F# for fun and profit, ~3 min) — the case for F# in five points, each with a snippet. Some tooling it mentions is dated, but the language features aren't.
- [ ] **~10 min** · Skim: [Tour of F#](https://learn.microsoft.com/en-us/dotnet/fsharp/tour) (Microsoft Learn) — a long tour, so read only "Record and Discriminated Union Types", "Pattern Matching" and "Options". You'll need these three features in the next level. You can run the snippets in your browser, as "Executing the code online" explains.

## Level 2 — Designing with types (~35 min)

Use the type system to make wrong data impossible to build.

- [ ] **~15 min** · Read: [Designing with types: Introduction](https://fsharpforfunandprofit.com/posts/designing-with-types-intro/) (Scott Wlaschin, Jan 2013, ~5 min) — a familiar `Contact` record, split into types that say what belongs together.
- [ ] **~20 min** · Read: [Designing with types: Making illegal states unrepresentable](https://fsharpforfunandprofit.com/posts/designing-with-types-making-illegal-states-unrepresentable/) (Scott Wlaschin, Jan 2013, ~6 min) — the best-known post in the series. A business rule becomes a union type, so the compiler enforces it. Think of a rule in your own code that you could enforce the same way, in whatever language you use.

## If you have extra time

- [ ] **~2.5 hours** · Watch: [Domain Modeling Made Functional](https://www.youtube.com/watch?v=Up7LcbGZFuo) (Scott Wlaschin, NDC Oslo, Jul 2017, ~52 min) — the talk version of these ideas, and of his book of the same name. It needs no F# knowledge, and it's one of the most popular talks on functional design.

## Wrap-up

This plan covers it. If you want to write F# for real, the rest of the [Designing with types](https://fsharpforfunandprofit.com/posts/designing-with-types-intro/) series is the next step. The blip compares F# with [[Clojure]] and Scala, which have their own blips (Scala's is [[Scala, the good parts]]). I left out the blip's mention of the F# 3.0 beta: it's long obsolete.

## Review the blip

- [ ] **~5 min** · Re-read [F#](https://www.thoughtworks.com/radar/languages-and-frameworks/f) now that you know the topic.
