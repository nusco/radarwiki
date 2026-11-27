- **Blip:** [.NET Aspire](https://www.thoughtworks.com/radar/languages-and-frameworks/net-aspire)
- **Time:** ~1.25 hours
- **Radar edition:** April 2025
- **Quadrant:** Languages & Frameworks
- **Ring:** Assess
- **Updated:** 2026-11-27
- **Status:** #undone

This plan assumes that you know Docker. You'll need a container runtime, such as Docker Desktop or Podman, for the exercise.

---

## Current state (late 2026)

The blip is from April 2025, when the product was still .NET-only. In November 2025, with version 13, Microsoft dropped the ".NET" from the name: it's now just Aspire, its docs moved to [aspire.dev](https://aspire.dev), and it can orchestrate Python, JavaScript and Go services as well as .NET ones. You can even write the AppHost, the file that describes your app, in TypeScript instead of C#. Aspire 17, released in November 2026, needs .NET 10 for C# AppHosts. The core idea is the one in the blip: one command starts your whole distributed app on your laptop, with a dashboard for its logs, traces and metrics.

## Level 1 — What it is (~20 min)

Start a whole distributed app locally with one command, and watch it in one dashboard.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/net-aspire) (~1 min) — note the two halves: local orchestration and local observability. The blip's link to Microsoft Learn now redirects to aspire.dev.
- [ ] **~15 min** · Read: [What is Aspire?](https://aspire.dev/get-started/what-is-aspire/) (Aspire docs, ~5 min) — read "Why Aspire?" for the before-and-after comparison, and "How Aspire works". Note what it says in "What Aspire is and isn't".

## Level 2 — Run an app (~35 min)

Create a starter app, run it, and find your way around the dashboard.

- [ ] **~35 min** · **Do:** Follow [Build your first Aspire app](https://aspire.dev/get-started/first-app/) (Aspire docs), in C# or TypeScript, after checking the [prerequisites](https://aspire.dev/get-started/prerequisites/). Run it with `aspire run` and open the dashboard. Use the frontend, then find the trace of one request that crosses from the frontend to the API, and the logs it produced. If you get lost, [Explore the Aspire dashboard](https://aspire.dev/dashboard/explore/) is a reference to its pages.

## Level 3 — Replace your local setup (~20 min)

See what Aspire changes in a real project's local environment.

- [ ] **~20 min** · Read: [Running a production-like local environment with Aspire](https://timdeschryver.dev/blog/running-a-production-like-local-environment-with-aspire) (Tim Deschryver, May 2026, ~7 min) — a worked example with Azure Blob Storage: an emulator locally, the real service in production, and one AppHost for both. Then think of your current local setup (a `docker-compose.yml`, a shared dev database, mocks) and decide which parts Aspire would replace.

## If you have extra time

- [ ] **~45 min** · Read: [Converting a docker-compose file to .NET Aspire](https://andrewlock.net/converting-a-docker-compose-file-to-aspire/) (Andrew Lock, May 2025, ~16 min) — a step-by-step migration of a real app and its database, then back to a compose file for deployment. It targets Aspire 9.3, so some APIs have changed, but the reasoning hasn't.
- [ ] **~20 min** · Read: [.NET Aspire: A Game-Changer for Cloud-Native Development?](https://www.milanjovanovic.tech/blog/dotnet-aspire-a-game-changer-for-cloud-native-development) (Milan Jovanović, Sep 2024, ~7 min) — a hands-on review that's honest about the drawbacks, in "Orchestration - The Bad Parts".

## Wrap-up

This plan covers it, unless you work on .NET or distributed apps daily: then Aspire's deployment features, such as publishing to Kubernetes, are the next thing to learn, from the [Aspire docs](https://aspire.dev).

## Review the blip

- [ ] **~5 min** · Re-read [.NET Aspire](https://www.thoughtworks.com/radar/languages-and-frameworks/net-aspire) now that you know the topic.
