- **Blip:** [Foundation models for structured data](https://www.thoughtworks.com/radar/techniques/foundation-models-for-structured-data)
- **Time:** ~1 hour
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you know what a classification or regression model is, and that you can run a bit of Python.

---

## Current state (late 2026)

For predictions on tables (rows and columns, like most business data), the standard tool has long been gradient-boosted trees, such as XGBoost, with a lot of feature engineering. In January 2025 a paper in *Nature* showed TabPFN, a transformer pretrained on millions of synthetic tables, that predicts on a new table without training, by "in-context learning", and matches tuned trees on small datasets. In 2026 more models followed, including Google's TabFM, and the size limits went up. The blip is new in November 2026. One practical catch: TabPFN's recent model weights are licensed for non-commercial use, so check the license before using it at work.

## Level 1 — What it is (~20 min)

A model pretrained on tabular data can make predictions on your table right away, without feature engineering or training.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/foundation-models-for-structured-data) (~1 min) — note the contrast with gradient-boosted models, and the use cases: risk assessment, predictive analytics, customer retention.
- [ ] **~15 min** · Read: [Introducing TabFM: A zero-shot foundation model for tabular data](https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/) (Weihao Kong and Abhimanyu Das, Google Research, Jun 2026, ~4 min) — a short explanation by the researchers: classification and regression as in-context learning, and pretraining on synthetic tables. It's a launch post, so the results are only in a chart.

## Level 2 — Try it (~40 min)

Compare a tabular foundation model with the usual approach on a real dataset.

- [ ] **~40 min** · **Do:** Follow the quick start in the [TabPFN README](https://github.com/PriorLabs/TabPFN) (Prior Labs) to install it. Pick a small public dataset with a few thousand rows, such as one from scikit-learn or Kaggle. Train a gradient-boosted model with default settings (for example, scikit-learn's `HistGradientBoostingClassifier`), then fit TabPFN on the same split. Compare accuracy and time, and note how much preparation each needed.

## Wrap-up

This plan is enough for a generalist. The tool itself has its own plan, [[TabPFN]].

## Review the blip

- [ ] **~5 min** · Re-read [Foundation models for structured data](https://www.thoughtworks.com/radar/techniques/foundation-models-for-structured-data) now that you know the topic.

## Related blips

- **[[TabPFN]]**: the best-known tabular foundation model, and one of the blip's two examples.
