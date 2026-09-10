# discreet-design

An Agent Skill that cuts an interface down to what it needs, and holds what
stays to strict craft rules.

Before drawing anything, it makes the agent run a fixed order: does this need
to exist, does a screen or a component the product already has carry it, can
type and spacing do the job, can it be fewer words. Only then does it draw.
Everything that survives goes through the craft rules: type, space,
alignment, colour, motion.

## Philosophy

### 1. Most interfaces fail by addition

One more card, one more icon, one more sentence: each is defensible alone,
and together they stop reading. So the first question on any screen is what
can go, and the last one before shipping is the same.

### 2. Understand before cutting

Restraint shortens the interface, never the understanding of it. Before
anything is removed: who lands on this screen, with what intent, and which
single action matters most.

### 3. A bare screen has nowhere to hide

Removing decoration raises the craft cost of what stays. A gap that a card
used to hide is now the first thing you see, so alignment, rhythm and optical
balance are the work, not the finish.

### 4. Quality goes where a screenshot can't see

The element count is the same before and after; what gets richer is time,
type, speed and space. In practice: a real typeface instead of the system
stack, one long pause before what matters most, one entrance that plays once,
and nothing that moves after the first paint.

### 5. Taste, written as rules

An agent can't have taste, but it can follow rules that taste wrote. So the
craft file is mechanical on purpose: one spacing scale, two font weights,
contrast floors, one easing curve for everything.

### 6. Some things are never cut

Interaction states, contrast, target sizes, affordances, and anything you
asked for explicitly. Restraint is about what's added, never about whether
the screen still works.

### 7. A first version does less, it isn't made worse

In MVP mode the scope shrinks and says so: a quiet version marker, empty
states that name what doesn't exist yet. The craft stays at full. The marker
announces scope; it never apologises for quality.

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

Explicit only. It does not trigger on ordinary UI work. Call it by name:

```
/discreet-design
/discreet-design the settings page has grown three extra cards
```

Or say you want the discreet-design skill. It has three levels if you ask
for one: lite builds what you asked and names the leaner version, full is the
default, ultra questions whether the screen should exist at all. MVP mode is
separate: it decides how honest the scope looks, never how low the craft goes.

A cut that skips a real corner is marked in the code with a `discreet:`
comment, so it can come back when the condition is met.

## What it does not do

It does not do product strategy, code architecture, or prose outside the UI.
It will not argue with you if you ask for the full version.

## Contents

| File | What's in it |
|---|---|
| `SKILL.md` | The ladder, the rules, what is never cut, levels, output |
| `references/craft.md` | How what stays is set: type, space, alignment, colour, motion |
| `references/mvp.md` | How a first version reads as unfinished in scope, not in craft |

## License

MIT. See [LICENSE](../../LICENSE).
