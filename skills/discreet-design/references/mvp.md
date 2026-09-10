# MVP mode

Read this when the build is an MVP, a first version, a prototype meant to go
public, or when the user says "MVP", "v0", "first version", "just enough to
ship".

## 1. The principle

An MVP reads as an MVP because it **does less**, not because it is **made
worse**. Craft stays at full: the ladder still runs, `craft.md` still applies to
everything that survives. What shrinks is the surface, and the surface says so.

Two different failures, often confused:

| It looks thrown together | It looks finished |
|---|---|
| A craft failure | A scope failure |
| Sloppy gaps, default styles, no states, no rhythm | Marketing shell, dead controls, fake data |
| Fixed by the ladder and `craft.md` | Fixed by this file |

Done means: someone outside can use it today, and a designer is not ashamed to
show it. Not: it is finished.

## 2. Write the done line first

Before building anything, one sentence: **it does X, for Y, and nothing else.**

Everything absent from that sentence is out of scope by definition. Do not
argue it case by case later; the sentence already decided. If the sentence
needs an "and" to be true, the scope is too wide, cut until it does not.

Write it in the repo, at the top of the readme or the main view's file. It is
the gate every later question gets measured against.

## 3. Cut list, signals of a finished product

- Marketing shell: landing page, hero, feature grid, pricing, testimonials, logos
- Fake anything: seeded users, placeholder avatars, lorem, invented numbers
- Dead controls: a settings screen, toggles wired to nothing, greyed menu items, "coming soon" tiles
- Accounts and onboarding when the thing works without them
- More than one level of navigation
- A second primary flow. One flow, or it is not an MVP
- Polish spent on the edges of the product instead of its centre: a 404 page, a loading mascot, an about screen

## 4. Keep list, signals of an MVP

- One screen, one task, and navigation that promises nothing beyond it
- A version marker, visible and quiet: `v0.1` set in the system's own type, in the header or footer. Never a ribbon, never a badge, never a colour reserved for warnings
- Empty states that name what does not exist yet, in plain words, instead of hiding it
- One line, in one place, on what it does not do yet. Not a roadmap, not a changelog
- Real data or nothing at all. An empty state beats a convincing fake
- Every state the user can actually reach: empty, loading, error. These are craft, they are never cut

## 5. The marker rule

The marker announces **scope**. It never apologises for **quality**.

- Good: `v0.1, converts EPUBs only`
- Bad: `work in progress, sorry for the rough edges`, `beta, expect bugs`

The first sets an expectation. The second asks for forgiveness, and a designer
asking for forgiveness reads as a designer who did not do the work.

## 6. Ship gate

Answer all six before calling it done. Any no is the next task, and the only
next task.

1. Does the done line still describe what is on screen?
2. Can a stranger reach the one useful outcome without being told anything?
2 bis. How many decisions does that take? See section 8. One is the target, three is the ceiling.
3. Is every control on screen wired to something real?
4. Do empty, loading, and error exist and read well?
5. Is the scope legible in under five seconds, from the marker and the empty states alone?
6. Would you put your name under a screenshot of it?

Six yeses means public. It does not mean finished, and the difference is the
whole point.

## 7. What this mode does not license

Restraint of scope is not permission to lower the bar on what remains. Fewer
screens raise the craft cost of each one. The alignment, the rhythm, the
motion, the type: all of it stays exactly as demanding as on a finished
product. An MVP that looks unfinished has failed this mode, not passed it.

## 8. The load test

Count decisions, not elements. Elements are what a screenshot shows; decisions
are what the screen costs. A screen can carry twenty quiet elements and ask for
one choice, or four elements and ask for five.

Walk the path to the one useful outcome and count every point where the user
must choose, compare, or wonder which of two things applies to them. An MVP
asks for one: the input itself. Three is the ceiling. Past that, the product is
not too big, it is undecided, and it is handing its indecision to the user.

Most of what gets added is not decoration. It is a doubt made visible: a piece
of helper text because they might not understand, a feature list because they
might not stay, a setting because someone might prefer the other way. Each one
answers a question the maker had, not one the user asked, and each one is
invisible to the maker, who knows why it is there. Every doubt you resolve
yourself is a decision the screen no longer has to ask for.
