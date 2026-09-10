---
name: discreet-design
description: Cuts an interface down to what it needs, then holds what stays to strict craft rules (type, spacing, alignment, colour, motion), with an MVP mode for first versions that go public. Runs only when called by name (`/discreet-design` or the user names this skill); it does not trigger on ordinary UI work.
disable-model-invocation: true
---

# Discreet design

The quietest screen that does the job is the right screen. Most interfaces fail by addition: one more card, one more icon, one more color, one more sentence, each defensible alone, unreadable together. This skill removes before it draws, and raises the craft bar on everything that stays, because a bare screen has nowhere to hide a sloppy gap.

Two files carry the method. This one decides **what stays**. `references/craft.md` decides **how it sits**, and applies to everything that survives; read it before producing or editing any UI. `references/mvp.md` decides **how honest the scope looks** when the build is a first version; read it when the user says MVP, v0, first version, or the thing is going public before it is finished.

## 1. Understand before cutting

Restraint shortens the interface, never the understanding of it. Before any decision: who lands on this screen, with what intent, and which single action matters most. The answer decides the one primary action per view and the reading order. Only then start cutting.

## 2. The ladder

Work top down, structure, then surface, then words. Stop at the first rung that holds.

1. **Does it need to exist?** A screen, a step, a modal, a setting, a section. Speculative need means skip it and say so in one line. A good default beats a setting; one step beats three.
2. **Does an existing view already carry it?** Extend a state of a screen that exists before minting a new one. New screens are the most expensive thing you can add.
3. **Does the design system already have it?** Existing component, existing variant, existing token. Never a new component when a variant fits, never a new color or size when the scale has one. Look before you draw.
4. **Does the platform pattern cover it?** Native controls and boring conventions (select, date input, system dialogs, standard navigation) over invented interactions. Users have already learned the boring version.
5. **Can structure alone do it?** Hierarchy from type scale, spacing and alignment before any box, border, background, divider, shadow or icon. Whitespace separates before a line does, a line before a box.
6. **Can it be fewer words?** A label over a sentence. Cut helper text that restates the control. No greeting headers, no exclamation marks, no emoji in UI copy.
7. **Only then** draw the minimum that reads well.

Two rungs hold: take the higher one and move on.

## 3. Rules

- Deletion over decoration. Every element earns its place or leaves.
- Off by default, on only when the system or the user asks: gradients, a card inside a card, an icon per list item, badges as seasoning, decorative shadows and glows, more than two font weights in a view, animation that does not communicate state, borders doing a job spacing already does.
- One primary action per view. When two things shout, nothing reads.
- A new color, size or radius is a system decision, not a local fix. If the scale lacks it, question the need before extending the scale.
- Two patterns of equal weight: take the more conventional one. Fewer inventions, not flimsier usability.
- A complex request gets the restrained version first, with the rest named in one line: "Did X; Y covers it. Need the full X? Say so." Never stall on an answer you can default.
- A deliberate omission that cuts a real corner is marked in the code with a `discreet:` comment naming what was cut and when to bring it back: `<!-- discreet: no filters, add when list > 20 items -->`.

## 4. What is never cut

Legible hierarchy (the view must survive an actual squint), interaction states (empty, loading, error, disabled, focus), contrast and accessibility basics, touch and click target sizes, affordances (interactive must look interactive), and anything explicitly requested. When the user insists on the full version, build it without re-arguing.

Precision is not optional either. Removing decoration raises the craft cost of what remains: alignment, rhythm and optical balance are the work, not the finish. `references/craft.md` holds the rules; its governing idea, the invisible channel, is that quality goes only into what a screenshot cannot see: time, type, speed and space.

## 5. Levels

The default is **full**: the ladder enforced, structure before decoration, system before invention, fewest elements that read well. Two others exist for when the user asks:

| Level | What changes |
|---|---|
| lite | Build what is asked, and name the leaner version in one line. The user picks. |
| ultra | A deletion pass is mandatory: every element justified or removed, and the screen's own existence challenged in the same breath. |

Example, "add a stats section to the dashboard": lite adds four stat cards and says three figures inline under the header would carry it; full ships three figures, one type step up, no cards, no icons; ultra ships the one figure that moves decisions, inline, and says a stats section is a dashboard inside the dashboard.

The level holds for the session once set. MVP mode is a separate axis, not a fourth level: it decides how honest the scope looks, never how low the craft goes.

## 6. Output

The work first. Then at most three short lines: what was removed or skipped, and when to add it. No tour of the layout, no paragraph of rationale; prose defending a decoration is decoration in words. A review or a walkthrough the user asked for is given in full.

When asked what changed, report counts before and after: elements, distinct colors, type sizes, font weights, shadows, radii.

## 7. Boundaries

This skill governs what goes on the screen: structure, surface and the words inside the interface. It does not govern product strategy, code architecture, or prose outside the UI.
