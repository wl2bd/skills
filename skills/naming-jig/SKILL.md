---
name: naming-jig
description: Use when the user wants to find, create, evaluate, rename, or check a name for a project, product, company, feature, app, library, package, or brand — including casual asks like "help me name this", "name ideas for X", "is X a good name?", and availability questions about domains or trademarks. Also use when naming is only one part of a bigger task: launching a product, starting a company, or publishing a tool or an open-source package.
---

# Naming jig

Naming looks like a creative free-for-all. It isn't. Professional naming is a process with a funnel shape: a precise brief, deliberately wide generation, brutal screening, and a short argued list, then verification against the real world (domains, trademarks, other languages). Skipping the funnel is why most first-pass names are either taken, generic, or embarrassing in another language.

One principle governs everything here: **a name is an empty vessel**. Apple said nothing about computers, Amazon nothing about books. The brand charges the name with meaning over time; the name's job is to be distinctive, sayable, ownable, and free of defects. Do not search for a name that "explains" the product; search for one the product can inhabit.

## Modes

Pick the mode from what the user actually needs:

- **Full process**: naming a company, product, or public-facing project. Run all steps below.
- **Quick ideas**: the user wants a handful of options fast (a repo, an internal tool, a feature). Compress: micro-brief (2-3 answers max), read `references/anti-patterns.md`, generate 30+ privately, screen them against the step 4 kill list, deliver 5-7 names with one-line rationales. Never skip the anti-patterns read: quick mode without it produces exactly the generic output this skill exists to prevent.
- **Evaluate an existing name**: the user already has a name or a shortlist. Skip to step 4 (screen), then step 6 (verify). Be honest: an evaluation that only reassures is worthless.

## 1. Brief

The five items below are what you need to **know**: not a questionnaire. Extract them from the conversation and context first, default what you reasonably can, and ask **at most two questions**, only for what is both essential and missing. Remaining assumptions get surfaced in the write-back below, where correcting them is cheap.

1. **What is being named**: company, product, feature, project, package? (The stakes and the legal exposure differ.)
2. **Positioning in one line**: what it does, for whom, against what alternative.
3. **Tone**: 3 adjectives the name should feel like, and 1-2 it must not.
4. **Markets and languages**: where will this name be read and said aloud? This decides which languages get the negative-meaning check.
5. **Constraints**: must-have TLD? Words to avoid? Competitor names to distance from? Sibling products it must sit next to? Will it need a trademark?

Write the brief back in 3-4 lines before generating. A wrong brief silently invalidates everything downstream.

## 2. Territories

From the positioning, define 3-5 **semantic territories**: distinct angles from which the name could come (e.g., for a backup tool: memory, vaults/protection, time, redundancy in nature, calm/relief). For each, list a lexical field: nouns, verbs, images, tools, places, myths.

Why: without territories, generation collapses onto the first obvious metaphor and produces forty variations of one idea. Territories force genuine spread.

## 3. Generate wide

Read `references/anti-patterns.md` **before** generating: it is the single highest-leverage read in this skill, because it lists the defaults you will otherwise reach for. Then read `references/name-types.md` and `references/generation.md` for the type taxonomy and construction techniques.

Rules of generation:

- Produce **60-100+ raw candidates** for a full process (30+ in quick mode). This is working material; never show the raw list.
- Spread across name types deliberately, using these proportions as guardrails against mode collapse, not as law: real words (suggestive, metaphor, arbitrary) ~40%, compounds ~15%, coined/morpheme-built ~20%, borrowed/foreign ~10%, experiential and other ~15%.
- Work territory by territory. Exhaust the obvious layer of each on purpose: the good names live behind it.
- Every candidate must be sayable on first read by the target markets. If you have to explain how to pronounce it, it fails later anyway.

## 4. Screen

Two passes, in order (details and tests in `references/evaluation.md`):

1. **Kill list**: eliminate anything that: matches an anti-pattern without written justification; fails the radio test (heard once → spelled correctly); is unpronounceable in a target market; has a negative or vulgar meaning in a target language; sits too close to a competitor or a major brand; is a category cliché.
2. **Scoring**: score survivors on distinctiveness, fit, sayability, memorability, stretch, and ownability. Scores rank the middle of the pack; the top and bottom are usually obvious.

## 5. Shortlist

Deliver **6-10 names**, deliberately mixed in type and risk level, from a safe compound to a bold coined word. A shortlist of ten variations of one idea is a failed shortlist: the point is to give a real decision space.

For each name use this structure:

```
### Name
Type + territory: e.g., Metaphor, from the "time" territory
Rationale: 2-3 sentences: why this name, what it evokes, why it fits the brief
Say it: pronunciation if not obvious
Watch out: the honest risk (crowded metaphor, spelling tax, class 9 conflict likely…)
```

## 6. Verify

Read `references/verification.md` for the full workflow. In short:

- **Domains**: run `scripts/check_domains.py` (Python 3, stdlib only; queries each TLD's authoritative registry over RDAP, or WHOIS for the ~180 TLDs that publish no RDAP) on the shortlist, passing `--tlds` derived from the brief's markets and constraints. Availability filters options; it must never pick the name. A `NO RDAP` result means the TLD could not be checked, not that the domain is free.
- **Trademarks**: screening, not clearance. Exact + sound-alike search on the relevant registries (EUIPO/TMview, INPI, USPTO, WIPO), in the Nice classes the user will actually operate in. Every trademark result you report must carry the label *indicative, not a legal clearance*.
- **Handles and registries**: social handles checked manually; for developer tools, check npm/PyPI/crates for package-name collisions.

Present results as an availability snapshot table alongside the shortlist.

## 7. Recommend

Commit to 2-3 recommendations and argue them against the brief, not against your taste. State the trade-off each one makes. Close with the standing caveat: for any name that will carry a company or a paid product, final trademark clearance belongs to a trademark attorney (conseil en PI in France); this process gets the user to a defensible shortlist, not to legal safety.

## Reference map

| File | Read when |
|---|---|
| `references/anti-patterns.md` | Always, before generating anything |
| `references/name-types.md` | Before generation: taxonomy, examples, legal strength per type |
| `references/generation.md` | During generation: techniques, sound symbolism, morphology |
| `references/evaluation.md` | During screening: kill list, tests, scoring, real-world failures |
| `references/verification.md` | During verification: domains, trademarks, handles, wording of disclaimers |
| `scripts/check_domains.py` | Step 6: RDAP domain availability check |
