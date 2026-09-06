# discreet-design

An Agent Skill that keeps a screen quiet: it cuts extra cards, icons and
colour before drawing anything.

Most interfaces fail by addition: one more card, one more icon, one more
color, each defensible alone, unreadable together. This skill runs a ladder
before anything is drawn. Does it need to exist. Does a view, a component or
a platform pattern already cover it. Can type, space or fewer words do the
job. Only then draw the minimum that reads well.

What stays has to sit well, because a bare screen has nowhere to hide a
sloppy gap. Craft (type, space, the one oversized pause, motion) applies to
everything that survives. An MVP does less. It is not made worse.

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
