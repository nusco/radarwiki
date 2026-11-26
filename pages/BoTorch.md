- **Blip:** [BoTorch](https://www.thoughtworks.com/radar/languages-and-frameworks/botorch)
- **Time:** ~1 hour 30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you can read Python, and a bit of PyTorch.

---

## Current state (late 2026)

Bayesian optimization finds good settings for something that's expensive to try: it builds a statistical model of the results so far, and picks the next experiment that's most likely to improve on them. It's best known for tuning machine learning hyperparameters, but it's increasingly used for physical experiments, like product formulations, where each try costs time and money. BoTorch is Meta's open-source library for it, built on PyTorch, and Ax is its companion for running experiments. The blip is new in November 2026. BoTorch is the low-level toolkit: for most practitioners, its own docs recommend starting with Ax.

## Level 1 — What Bayesian optimization is (~1 hour)

Find the best settings with as few expensive experiments as possible.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/botorch) (~1 min) — note the use cases beyond hyperparameter tuning.
- [ ] **~55 min** · Read: [Exploring Bayesian Optimization](https://distill.pub/2020/bayesian-optimization/) (Apoorv Agnihotri and Nipun Batra, Distill, May 2020, ~20 min) — a beautifully illustrated explanation, with a running example of searching for gold. Read up to and including "Acquisition Functions" and the comparison, and skim the hyperparameter tuning examples. The interactive figures are the point, so take your time with them.

## Level 2 — Try it (~30 min)

- [ ] **~30 min** · **Do:** Install BoTorch (`pip install botorch`) and run the example on the [BoTorch home page](https://botorch.org/): fit a model to a few random points, and ask for the next candidate. Then replace the random data with a function you define, run a few rounds, and watch the candidates close in on the best value.

## Wrap-up

This plan is enough for a generalist. If you'll run real experiments, start from Ax, which the blip pairs with BoTorch.

## Review the blip

- [ ] **~5 min** · Re-read [BoTorch](https://www.thoughtworks.com/radar/languages-and-frameworks/botorch) now that you know the topic.

## Related blips

- **[[PyTorch]]**: the library BoTorch is built on.
- **[[Ax]]**: orchestrates the experiments that BoTorch optimizes.
