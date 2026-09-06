# Craft

Restraint decides what stays. This file decides how it sits. Every rule
here is mechanical on purpose: an agent cannot "have taste", but it can
follow rules that taste wrote. Apply all of them to everything that
survives the ladder. This is what separates a designed bare screen from a
wireframe.

## The invisible channel

The rule that governs all of it: quality is added only where a screenshot
cannot see it. The count of elements is identical before and after; time,
type, speed and space are what gets richer. Anything that raises the count
is not this rule, it is decoration under another name.

Two screenshots verify it in three seconds, which is why it is a rule and
not a matter of taste.

## Type

- One real typeface beats the system stack: it upgrades every element at once without adding one. Pick a face with the features the view needs (real weights, tabular figures), and load it without layout shift: preload it, pair it with a metric-compatible fallback.
- One family. Two weights maximum, chosen once (regular + one emphasis weight).
- A deliberate scale, not sizes picked per element. Three or four sizes per view, from one ratio.
- Hierarchy shows by distance: adjacent levels differ visibly (around 1.3× or more), or by size, weight, and color moving together. Six sizes two pixels apart is no hierarchy; three sizes far apart is.
- Letter-spacing follows size: at 24px and above, tighten (-0.01em to -0.025em). At 13px and below, open slightly (+0.005em to +0.01em) for labels. Body stays at 0.
- Line-height follows size: display 1.1 to 1.2, body 1.5, labels 1.3. Never one line-height for everything.
- Wrapping is set, not left to chance: `text-wrap: pretty` on the root so every block inherits it, `text-wrap: balance` on headings and short standalone lines. And on locked copy, the last two words are joined with a non-breaking space: no line ends on a single word, whatever the browser or the width.
- Numbers that will be compared use `font-variant-numeric: tabular-nums`.
- `-webkit-font-smoothing: antialiased` on the root: on macOS the default subpixel rendering thickens light text.
- Real characters: a minus is −, not a hyphen. Multiplication is ×. Apostrophes curl. Ranges use –.
- Never an em dash, anywhere: not in copy, not in titles, not in metadata. And no middle dot as a separator. Titles separate with a period and a capital; inline metadata separates with a comma.
- One casing (sentence case) and one format per data type across the view: if one timestamp reads "18 min ago", none reads "1 hour ago". Pick the unit style once.

## Space

- One scale, stated once (4, 8, 12, 16, 24, 32, 48, 64, 96). Every margin, padding and gap comes from it. A value off the scale is a bug.
- Space encodes hierarchy: more space before a heading than after it, so the heading binds to what it introduces.
- Proximity encodes relation: tight inside a group (4 to 12), generous between groups (48 to 96). The contrast between the two is what reads as intent; near-equal spacing everywhere reads as a template.
- One oversized pause per page: a single interval, two to three times the base beat, placed before what matters most. It is paid for by tightening the base rhythm, never by widening the rest: a silence only exists against a tempo.
- Padding is symmetric unless asymmetry says something.
- A surface never touches its content. Any background behind text, hover states included, keeps a horizontal inset of 12px or more. When the text must hold the page's left edge, the surface extends outward past it; the text never moves inward, and hairlines stay at content width.

## Alignment

- One left edge. Everything hangs from it unless a real column exists.
- Numbers compared vertically are right-aligned on the decimal.
- Mixed sizes on one line align on the baseline, not on centers or boxes.
- Optical beats geometric: icons and glyphs center by visual weight, hanging punctuation hangs. When the math says centered and the eye says off, the eye wins.
- Nested radii are concentric: outer radius = inner radius + padding. Mismatched nested corners read as broken, and radius 0 nests for free.

## Color

- One ink ramp, defined once: ink, muted, faint, hairline, background. No color outside the ramp except meaning.
- Color marks meaning only: state, action, data. If a color decorates, it goes.
- Contrast floors: 4.5:1 for body text, 3:1 for large text and essential UI. Muted stays above the floor. Faint never carries text: it exists for underlines, hairline accents and decoration only. The text floor is muted.
- Hairlines are exactly 1px and use exactly one color everywhere in the view.

## States and motion

- Interactive elements have hover, focus-visible, and active states. A missing state is an unfinished element, not a minimal one.
- A string the user will copy gets a quiet copy control: invisible until hover or focus, always visible on touch, one glyph, a confirmation that lasts a breath.
- Interactions use transitions, never keyframes: a transition retargets mid-flight when the user changes their mind, a keyframe runs its fixed timeline to the end. Keyframes are for the one staged entrance only.
- An icon that swaps with a state transitions between the two (opacity, a slight scale), it never hard-swaps.
- Exits are quieter than entrances: fade and soften, do not retrace the way in. What leaves has already lost the user's attention.
- One curve for the whole system: a single strong ease-out that decelerates into its end, shared by every transition, entrance, and eased value. Mixed curves read as noise.
- A hover changes exactly one property, always through a transition, never instantly: enter around 200ms, leave around 500ms. The slow release is what reads as smooth. What cannot transition (a scrollbar thumb) does not change on hover at all. Focus indication is the one exemption: it appears immediately, by design.
- `:focus-visible` is styled, always, and not with the browser default.
- Motion is the invisible channel at its strongest: it makes a bare screen feel expensive without adding a single element to it. Spend it once.
- One orchestrated entrance per view: a single staggered sequence (60 to 110ms steps, 500 to 900ms each, a small rise and fade, one decisive ease-out curve), played once, in reading order, over the whole view or just its opening. Choreography is hierarchy in time: what matters enters first.
- The entrance never gates anything: content is present and interactive from the first frame. The animation is paint, not loading.
- One held beat per entrance: the cascade runs, stops, and after a real silence the last visible line arrives alone.
- Everything else stays still. No looping, ambient, or scroll-triggered decoration. `prefers-reduced-motion` turns the entrance off entirely.

## Speed

Perceived speed is a material. A page that stutters reads cheap in any
design.

- Nothing moves after first paint except the entrance: every image and embed has its dimensions reserved, nothing reflows when async content lands.
- Interaction acknowledges within 100ms, even when the work takes longer. Feedback first, completion after.
- No spinner for waits under 300ms: a spinner draws attention to a delay nobody would have felt.
- The page weighs what it shows. A bare screen that loads heavy is a broken promise.

## Imagery

Most pages need no image: structure, type, and space carry. Never add a
visual to fill a gap; a gap is design.

- An image earns its place the way an element does: it proves (a screenshot), it replaces prose (a diagram worth two hundred words), or it is the content itself. Mood is not a job.
- The signature budget is one: at most one visible signature element per page, and the best signature demonstrates the idea instead of decorating it.
- An image is a block like any other: aligned to the grid, radius 0, no decorative frame or shadow. A border only when the image's background would bleed into the page's.
- Dimensions always reserved, alt text always written, captions in the label style, close to the image.
- A social image (1200 × 630) is read at less than half size, in a feed, on a phone. The page's type scale does not apply; the image has its own floor: nothing under 32px in the source, the secondary line at 40px or more, the title at 96px or more, and at most three lines of text in total. Squint at the render scaled to 500px wide: whatever cannot be read there is decoration, remove it or enlarge it. (Recurring failure: kicker and tagline set at page sizes, illegible in the card.)

## The invisible

The screenshot never shows these; use does. Design them anyway: a default
blue selection or a stock scrollbar breaks the spell at first touch.

- `::selection` comes from the ink ramp, never the browser default.
- The scrollbar is thin and drawn from the ramp: quiet thumb, invisible track.
- Tap highlight is transparent, replaced by designed states. Caret and accent colors come from the ramp.
- The favicon and the browser theme color belong to the system: the tab is part of the page.
- The link preview is designed before the page is seen: the social image and metas come from the system.
- The dark scheme is the ramp inverted, decided once; the theme color and the favicon follow it.
- The 404 and the printed page are interface too: designed once, quietly.
- The overscroll zone matches the background, so the page has no edges.

## Data

- A minimal chart is finished, not naked: tuned margins, a deliberate stroke (1.5 to 2px), and a terminal marker with the current value so the reader gets the number without an axis.
- Show a zero baseline only when zero is meaningful; otherwise crop honestly and say nothing else.
- No gridlines, ticks, or legend unless reading fails without them. One series needs no legend.
- An arrow that carries data is drawn, not typed: a short tail and a tall open head, stroke matched to the weight of the figures beside it, round caps. The typed arrow glyph is too thin next to numbers.

## The finishing pass

Before shipping, three checks in order:

1. Squint at it: eyes half closed, the most important thing must read first, and groups must hold as groups.
2. Walk the edges at 100%: every gap on the scale, every baseline shared, every hairline 1px.
3. Remove one more thing. If the view survives, ship without it.
