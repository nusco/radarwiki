Yes. Collapsing everything into skills is feasible, and I think it's the right shape. The user's whole setup becomes: install the skills into an empty folder, then say "set up a learning wiki here." Five things will make it work well:

**1. Ship templates; don't let the model write config from scratch.** Put the files `init` needs inside the skill folder (the Agent Skills format has an `assets/` directory for this): the page template, a profile skeleton, the `.obsidian/` config, and a per-harness permissions file. `init` then copies the files and fills in only the profile from its interview. Copying is deterministic, which matters a lot for weaker models. An Ollama model inventing a `settings.json` from memory is a bug waiting to happen.

**2. Harness-specific knowledge still has to live somewhere.** "Generate whatever reduces friction" assumes the agent knows its own harness's config format. Claude knows Claude Code's, but a local model in Pi may not know Pi's. Keep a small reference file per known harness (`harnesses/claude-code.md`, `harnesses/pi.md`) holding the config snippet and where it goes, and have `init` read only the one that applies. For harnesses you don't know, the fallback is: "tell the user which permissions to grant, and don't guess." Adding support for a new harness then means adding one file.

**3. Make self-granted permissions visible.** An agent writing its own permission rules is exactly what a careful user, and a careful harness, should see. Claude Code will ask before editing its settings file, and the change may only take effect after a restart. Have `init` show what it's about to allow (for example, "fetch any web page, run the link checker") and ask for confirmation. It's a one-time prompt, and it's the right one.

**4. Some Obsidian steps can't be done from inside the folder.** `init` can write `.obsidian/` config, and with bash it could even download plugin files from GitHub releases. But the user still has to open the folder as a vault and turn on community plugins, and Obsidian may need a reload to pick up the changes. So `init` should end with a short checklist for the user, and anything it downloads into the vault should be shown, since that's third-party code.

**5. Two robustness details:**

- **Make `init` safe to rerun.** It should never overwrite the profile or existing pages, so that "run init again" also works as repair and upgrade.
- **Scope the skill descriptions.** If someone installs the skills globally instead of per folder, a vague `plan` skill could trigger while they're writing code. Word every description to apply only "inside a learning wiki (a folder containing `_profile.md`)."

Put together, this is close to the single umbrella skill from before:

```
learning-wiki/
├── SKILL.md            # entry point: routes to init / plan / tweak / refresh
├── init.md, plan.md, tweak.md, refresh.md
├── reference/          # page format, link rules, source quality
├── harnesses/          # claude-code.md, pi.md, …
├── scripts/            # check-links.py
└── assets/             # page template, profile skeleton, .obsidian/, settings files
```

One skill folder, installed with `npx skills add`. Everything else is created by `init`, and there's nothing Claude-specific in it except one file in `harnesses/`.