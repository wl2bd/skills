# naming-things

An Agent Skill that turns naming from a five-minute guess into a process.

We ship products faster than ever. The name is usually the last thing decided
and the first thing that can't be undone: it's on the domain, the repo, the
package registry, the invoices, the trademark filing. This skill makes an agent
run the process a naming professional would run: a precise brief, deliberately
wide generation, brutal screening, an argued shortlist, then verification
against the real world.

## Philosophy

### 1. A name is an empty vessel

Apple said nothing about computers, Amazon nothing about books. The brand
fills the name over time. So the skill looks for a name the product can
inhabit, not one that explains it.

### 2. The name comes before the logo and outlives it

This is why a designer wrote it. A logo only travels where the company puts
it; the name travels by word of mouth, without the designer. It's the first
brand asset, and the one a rebrand doesn't touch.

### 3. The first ideas are everyone's ideas

Nova, Apex, Forge, anything ending in -ly: founders reach for these first,
language models even faster. The skill reads its list of exhausted defaults
before generating, then produces 60 to 100 candidates it never shows.

### 4. The presentation must not vote before you do

Every name on the shortlist gets the same amount of text, so none reads as
the favourite. You give a gut reaction to each one, said aloud, before
reading the arguments.

### 5. It says what it cannot know

The domain checker never reports a taken domain as free (see below).
Trademark results are screening, never clearance, and say so every time.

### 6. Rules are checkpoints, the context decides

A name that is typed can be `quiet.tools`; a name that is said pays the dot
every time. An exhausted word can pass when the category is new and the word
is free, as long as the reason is written down.

### 7. The decision stays yours, and it waits a night

Availability filters the options, it never picks the name. Register nothing
in the session: reread the shortlist the next day and keep what survives the
night.

## Install

Part of [wl2bd/skills](https://github.com/wl2bd/skills). See that README for
the plugin install. To take just this one:

```bash
git clone https://github.com/wl2bd/skills.git
cp -r skills/skills/naming-things ~/.claude/skills/naming-things
```

For other runtimes, `~/.agents/skills/` works as a cross-runtime alias. No
dependencies: the one script is Python 3 standard library only.

## Use

You don't invoke it. Ask your agent for a name and the skill triggers on its
own:

> I'm launching an open-source library that parses ICS files. I need a crate
> name before I publish.

> We're stuck between Cleary, Clario and Klaro for our accounting app.

> Is "Verdance" a good name for a SaaS? Is the domain free?

It adapts: a full process for a company or product, a compressed one for a repo
or an internal tool, and a screening-plus-verification pass when you already
have a shortlist. It knows the difference between a name that will be said
(a company, a pitch, a podcast) and one that will be typed (a package, a
directory, a side project): the second may be a domain hack like
`quiet.tools`, the first pays the dot every time. And when the thing you're
naming is the first of a series, it designs the grammar of the family and
checks that the second and third names are still free.

## The domain checker

`scripts/check_domains.py` runs standalone if you want it on its own:

```bash
python3 scripts/check_domains.py lumafold amberpost verdance --tlds com,ai,io
```

```
No RDAP service for: .io. Checked over WHOIS instead, against a
known-taken and a known-free control on each registry. Say so when
you report these: the signal is WHOIS, not RDAP.

name       .com          .ai           .io
-----------------------------------------------------
lumafold   REGISTERED    AVAILABLE?    AVAILABLE?
amberpost  REGISTERED    AVAILABLE?    AVAILABLE?
verdance   REGISTERED    REGISTERED    REGISTERED

AVAILABLE? = no registration found at the authoritative registry.
             Confirm at a registrar before committing to the name
             or mentioning it publicly.
```

Domain hacks and category TLDs go in as written. Each one is checked on its
own TLD only, never flattened into `quiettools.com`:

```bash
python3 scripts/check_domains.py quiet.tools amberpost.haus
```

Bare names and full domains can be mixed in one run; the table marks with `-`
the cells that were not asked.

It is built around one failure it must never commit: **telling you a domain is
free when somebody already owns it.**

Most availability checks query a public RDAP redirector. A redirector answers
404 for every TLD it does not serve, which is indistinguishable from "no
registration found", so `.io`, `.de`, `.eu` and roughly 180 other TLDs come
back looking gloriously available. Measured against 14 domains that are all
certainly registered, that approach reported 6 of them as free, `github.io`
included.

So instead this script:

- resolves each TLD to its **authoritative registry** through the IANA
  bootstrap registry, and queries that registry directly;
- **control-tests every registry** before trusting it, using lookups whose
  answers are already known. If a registry can't demonstrate it distinguishes
  a taken domain from a free one, its results are reported `UNKNOWN`, never
  `AVAILABLE?`;
- falls back to **WHOIS** for the TLDs that publish no RDAP, learning each
  registry's own phrasing from two controls rather than parsing free text;
- treats a rate-limit notice, an empty body or a refusal as a **non-answer**,
  because a busy registry must not read as a list of free domains.

Without `--tlds` it checks `.com`, `.ai`, `.app`, `.io`, `.dev` and `.tools`:
the extensions a tech product actually wears in 2026. Country extensions
(`.fr`, `.de`, `.uk`) are a market anchor, not a default; ask for them when
the brief names the country.

`AVAILABLE?` keeps its question mark on purpose. It means no registration was
found, not that the domain is yours. Confirm at a registrar before committing
to a name, and before mentioning it publicly.

Accented candidates are transliterated, not stripped: `über` is checked as
`uber`, and the rewrite is printed, because silently checking `ber` is how
you end up confident about the wrong domain.

Two TLDs cannot be checked at all: `.ch` and `.es` refuse automated port 43
access. The script says so rather than pretending.

## What it does not do

It does not do brand strategy or positioning. The process starts from a
brief, and the brief assumes someone has already decided what this thing is,
for whom, and against what. When that work has not been done, no shortlist
fixes it: the names will be plausible and wrong. Do that work first, with
whoever does it for you; the skill takes over from there. It exists because
between a strategy nobody has budgeted and a name picked in an afternoon,
most teams get the afternoon, and the afternoon deserves a method.

It does not clear a trademark. It screens: it catches obvious conflicts early,
so dead names exit before anyone falls in love with them. Every trademark
result it produces carries that caveat verbatim. For a name that will carry a
company or a paid product, final clearance belongs to a trademark attorney.

It does not pick the name either. Availability filters options; the decision
stays yours.

## Contents

| File | What's in it |
|---|---|
| `SKILL.md` | The seven-step process and when to compress it |
| `references/anti-patterns.md` | The defaults you'll otherwise reach for |
| `references/name-types.md` | Taxonomy, examples, legal strength per type, said versus typed |
| `references/generation.md` | How to build names, sound symbolism, domain hacks, series grammars |
| `references/evaluation.md` | Kill list, tests, scoring, the visual room pass, real-world failures |
| `references/corpus.md` | Over 200 real names by type, 1870 to 2026, what each one buys and costs |
| `references/verification.md` | Domains, trademarks, handles, wording of disclaimers |
| `scripts/check_domains.py` | Domain availability, RDAP + WHOIS |

## License

MIT. See [LICENSE](../../LICENSE).
