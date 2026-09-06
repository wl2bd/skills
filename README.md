# skills

Agent Skills by [wl2bd](https://github.com/wl2bd).

A skill is a process an agent runs instead of improvising one. These are the
ones I use in my own work, cleaned up enough to hand over.

## Available

| Skill | What it does |
|---|---|
| [**naming-things**](skills/naming-things) | Turns naming a product, company, library or feature into a real process — brief, wide generation, brutal screening, argued shortlist — then verifies domains against authoritative registries. |

## Install

**As a plugin** — one command, and you get everything I add later:

```
/plugin marketplace add wl2bd/skills
/plugin install wl2bd@wl2bd
```

Skills then answer to `wl2bd:naming-things`.

**As a plain skill** — copy the folder you want:

```bash
git clone https://github.com/wl2bd/skills.git
cp -r skills/skills/naming-things ~/.claude/skills/naming-things
```

Installed this way it answers to `naming-things`, unprefixed. `~/.agents/skills/`
works as a cross-runtime alias for Codex, Copilot CLI and Gemini CLI.

Either way, there is nothing to build and nothing to install: the only script
in here is Python 3 standard library only.

## Using them

You don't invoke a skill. You ask for the thing, and it triggers on its own:

> Je lance une lib open source pour parser des fichiers ICS. Il me faut un nom
> de crate avant de publier.

> We're stuck between Cleary, Clario and Klaro for our accounting app.

## License

MIT — see [LICENSE](LICENSE). Use them, fork them, adapt them.
