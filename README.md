# skills

Agent Skills by [wl2bd](https://github.com/wl2bd).

A skill is a process an agent runs instead of improvising one. These are the
ones I use in my own work, cleaned up enough to hand over.

## Available

| Skill | What it does |
|---|---|
| [**naming-things**](skills/naming-things) | Turns naming a product, company, library or feature into a real process: brief, wide generation, brutal screening, argued shortlist, then domain checks against authoritative registries. |
| [**discreet-design**](skills/discreet-design) | As little visible design as possible, and a lot of care in what remains. Explicit only (`/discreet-design`) — does not trigger on ordinary UI work. |

## Install

**As a plugin**: one command, and you get everything I add later:

```
/plugin marketplace add wl2bd/skills
/plugin install wl2bd@wl2bd
```

Skills then answer to `wl2bd:naming-things` and `wl2bd:discreet-design`.

**As a plain skill**: copy the folder you want:

```bash
git clone https://github.com/wl2bd/skills.git
cp -r skills/skills/naming-things ~/.claude/skills/naming-things
cp -r skills/skills/discreet-design ~/.claude/skills/discreet-design
```

Installed this way they answer unprefixed. `~/.agents/skills/` works as a
cross-runtime alias for Codex, Copilot CLI and Gemini CLI.

Either way, there is nothing to build. The only script in the repo is Python 3
standard library only, in naming-things.

## Using them

`naming-things` triggers on its own when you ask for a name:

> I'm launching an open-source library that parses ICS files. I need a crate
> name before I publish.

> We're stuck between Cleary, Clario and Klaro for our accounting app.

`discreet-design` does not. Call `/discreet-design` when you want it.

## License

MIT. See [LICENSE](LICENSE). Use them, fork them, adapt them.
