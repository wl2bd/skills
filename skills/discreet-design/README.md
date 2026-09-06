# discreet-design

An Agent Skill for as little visible design as possible, and a lot of care
in what remains.

Most interfaces fail by addition: one more card, one more icon, one more
colour, each defensible alone, unreadable together. This skill asks, before
drawing, whether the thing needs to exist at all, and whether type, space or
fewer words already do the job. Then it draws the minimum that still reads.

A bare screen has nowhere to hide a sloppy gap, so the care goes into what
stays: type, space, the one pause, motion. A first version does less. It is
not made worse.

## Install

Part of [wl2bd/skills](https://github.com/wl2bd/skills). See that README for
the plugin install. To take just this one:

```bash
git clone https://github.com/wl2bd/skills.git
cp -r skills/skills/discreet-design ~/.claude/skills/discreet-design
```

For other runtimes, `~/.agents/skills/` works as a cross-runtime alias. Nothing
to build: there is no script.

## Use

You don't invoke it. Ask for a screen, say it's too busy, or that this is an
MVP:

> The settings page has grown three extra cards. Can you clean it up?

> First version of the export flow, just enough to ship.

> The dashboard is shouting. Less.

It works in three intensities if you ask: lite names the leaner version and
lets you pick, full is the default, ultra challenges whether the screen should
exist. MVP is a separate axis: how honest the scope looks, never how low the
craft goes.

A cut that skips a real corner is marked in the code with a `discreet:`
comment, so it can come back when the condition is met.

## What it does not do

It does not do product strategy, code architecture, or prose outside the UI.
It will not argue with you if you ask for the full version.

## Contents

| File | What's in it |
|---|---|
| `SKILL.md` | The ladder, the rules, what is never cut, levels, output |
| `references/craft.md` | How what stays sits: type, space, motion, the invisible channel |
| `references/mvp.md` | How a first version reads as unfinished in scope, not in craft |

## License

MIT. See [LICENSE](../../LICENSE).
