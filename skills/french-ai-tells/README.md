# french-ai-tells

An Agent Skill that finds and removes AI tells in French prose.

Language models write French the way they write English, then translate. The result is correct and still recognisable: « Dans le paysage actuel », « Il est crucial de noter que », « Ce n'est pas X, c'est Y », a memo that could be translated back into English without touching a single sentence. This skill audits a French text for those patterns, quotes each one, and rewrites them out while keeping every fact and the author's voice.

## Where it comes from

Two MIT projects, merged and brought up to date.

- [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) by Conor Bronsdon, the reference skill for English. This adaptation follows v3.35.0: its modes, severity tiers, profiles, rewrite guardrails, and its full pattern catalog, transposed into French.
- [avoid-ai-writing-multilingual](https://github.com/jurigis/avoid-ai-writing-multilingual) by Jürgen Kraus, whose French version was researched in French rather than translated. It supplies the French vocabulary tiers, the French-specific patterns (managerial boilerplate, impersonal distancing, conditional hedging) and the sources. It was built on avoid-ai-writing v3.4, so about thirty patterns added upstream since then were missing, among them negation chains, « ce n'est pas X, c'est Y » in its split and countdown forms, manufactured punchlines, aphorism formulas and narrated candor.

## What this version adds

1. **The current catalog in French.** Every upstream pattern, with French examples and French carve-outs, rather than the v3.4 subset.
2. **Calques of English.** A section of structure tics that read as translated: « J'espère que ce message vous trouve bien », « Je vous aide à… », the marketing imperative, the possessive in every sentence, and a back-translation test.
3. **French typography, handled carefully.** Title Case, capitalised months, English quotes and number formats are flagged, and the marks pass matches the convention the source already uses instead of imposing « » and non-breaking spaces on a text that doesn't have them.
4. **A guardrail against forced orality.** The French humanizer fingerprint is dislocations, « Bon. » and « Franchement, » sprinkled into a text that was never oral. A rewrite may not add them.
5. **Provenance on every entry.** Entries backed by French research are marked; the rest are transpositions of English findings, and the skill treats their thresholds as conventions.

The upstream Node scripts (detector, quote normaliser, style checker) are not included: their word lists are English. The checks they automate are described in the skill and applied by the agent.

## Install

As part of the collection, see the [repository README](../../README.md). As a plain skill:

```bash
git clone https://github.com/wl2bd/skills.git
cp -r skills/skills/french-ai-tells ~/.claude/skills/french-ai-tells
```

## Using it

It triggers on its own when a French text needs cleaning:

> Ce post LinkedIn sonne IA, tu peux le reprendre ?

> Scanne ce mémo sans le réécrire.

> Nettoie `billet.md` directement, profil blog, voix directe.

For English prose, use avoid-ai-writing.

## License

MIT, with the notices of both original works. See [LICENSE](LICENSE).
