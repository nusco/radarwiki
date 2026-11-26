- **Blip:** [Chaos Mesh](https://www.thoughtworks.com/radar/tools/chaos-mesh)
- **Time:** ~1 hour 10 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know the basics of Kubernetes.

---

## Current state (late 2026)

Chaos engineering, deliberately breaking parts of a system to learn how it copes, started at Netflix around 2010 and was on the Radar by 2019. Chaos Mesh is an open-source toolkit for doing it on Kubernetes, and a CNCF incubating project. It describes each experiment as a Kubernetes resource in YAML, so experiments can live in version control and run from the same tools as everything else. The blip is new in November 2026, and points to a new use: testing the resilience of GPU-heavy AI infrastructure, where failures are expensive. Its old install script is deprecated in favor of Helm.

## Level 1 — What it is (~20 min)

Inject controlled failures, like killed pods, network delays or stressed CPUs, into a Kubernetes cluster, defined as declarative resources.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/chaos-mesh) (~1 min) — note what makes it fit for automated testing: reproducibility and blast-radius controls.
- [ ] **~15 min** · Read: [Principles of Chaos Engineering](https://principlesofchaos.org/) (chaos engineering community, updated Mar 2019, ~4 min) — the short manifesto behind the practice: form a hypothesis about steady state, inject real-world events, and keep the blast radius small. Everything Chaos Mesh does serves these steps.

## Level 2 — Run an experiment (~50 min)

Run one chaos experiment on a test cluster, following the principles.

- [ ] **~15 min** · Read: [Simulate Pod Faults](https://chaos-mesh.org/docs/simulate-pod-chaos-on-kubernetes/) (Chaos Mesh docs, ~5 min) — the simplest experiments: kill a pod, kill a container, or make a pod fail. Note the YAML shape, and the warnings about probes.
- [ ] **~35 min** · **Do:** On a local cluster (kind or minikube), install Chaos Mesh with Helm, and deploy a small app with two replicas. Write down a hypothesis, for example "if one pod dies, requests keep succeeding". Run a `pod-kill` experiment from YAML, and check the hypothesis. Then change one thing, like dropping to one replica, and run it again.

## Wrap-up

This plan covers the tool. The practice has its own plan, [[Chaos Engineering]].

## Review the blip

- [ ] **~5 min** · Re-read [Chaos Mesh](https://www.thoughtworks.com/radar/tools/chaos-mesh) now that you know the topic.

## Related blips

- **[[Chaos Engineering]]**: the practice that Chaos Mesh implements on Kubernetes.
