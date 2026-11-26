- **Blip:** [VAST DataStore](https://www.thoughtworks.com/radar/platforms/vast-datastore)
- **Time:** ~15 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This is a specialist platform for large GPU clusters, so it gets a short plan.

---

## Current state (late 2026)

Training and serving large models needs storage that can keep expensive GPUs busy: loading data, writing checkpoints, and loading models quickly. Traditionally that meant specialized parallel file systems. VAST DataStore, the storage layer of VAST Data's commercial platform, offers file, object and block access to the same data on all-flash storage, with compute and capacity that scale separately. VAST also works with NVIDIA on faster transfers and shared cache storage for inference. The blip is new in November 2026. It's expensive and ties you to VAST's platform, so it's mainly for teams running large training or inference clusters.

## Level 1 — What it is (~5 min)

Storage built to keep large GPU clusters fed, with file, object and block access in one system.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/vast-datastore) (~2 min) — note the comparison with Ceph, the open-source alternative.

## Level 2 — Place it (~10 min)

- [ ] **~10 min** · **Do:** Write down the three moments when storage can leave GPUs waiting (loading training data, writing checkpoints, loading models for inference), and for a workload you know, which one would matter most. That's enough to recognize when a platform like this is relevant.

## Wrap-up

This plan is enough unless you design GPU clusters. VAST's own pages are marketing, so I didn't add them.

## Review the blip

- [ ] **~5 min** · Re-read [VAST DataStore](https://www.thoughtworks.com/radar/platforms/vast-datastore) now that you know the topic.

## Related blips

- **[[Ceph]]**: an open-source alternative for block, file and object storage on commodity hardware.
