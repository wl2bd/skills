# Verification

Verification comes **after** screening, on the shortlist only. Its output is an availability snapshot, not a verdict: availability filters options; it never picks the name.

## 1. Domains

Run `scripts/check_domains.py` on the shortlist (Python 3, stdlib only, network required; see the fallback table below when either is missing):

```bash
python3 scripts/check_domains.py lumafold amberpost --tlds com,ai,io,app
python3 scripts/check_domains.py quiet.tools amberpost.haus   # domain hacks, as written
```

A candidate given as a full domain is checked on its own TLD only; bare names get every `--tlds` column. Never pass a domain hack as a bare compound (`quiettools`): that checks a different name.

It resolves each TLD to its authoritative registry through the IANA bootstrap registry, then queries that registry directly: over RDAP where the TLD publishes it, over WHOIS otherwise. Every TLD is control-tested before any of its answers are trusted. Interpretation:

- `REGISTERED`: taken. (It may still be parked and buyable; note it, don't chase it unprompted.) The script cannot price a domain, but the report should not leave the cost implicit: for each name reported `REGISTERED` on a TLD the brief cares about, and for any TLD with premium pricing (`.ai`, `.io`, most category gTLDs, every "premium" second-level label flagged by a registry), give an order of magnitude in the snapshot table: standard registration (under 50 EUR/yr), premium tier (50 to 500 EUR/yr), aftermarket (a parked page with a price: quote it). Classify on the renewal price, not the first-year promotion (`.press` at 5 USD the first year and 64 USD after is premium). Check the registrar page by hand; never guess a price from memory. Cost is a filter like availability: it informs the choice, it never makes it.
- `AVAILABLE?`: no registration found at the authoritative registry: an RDAP 404, or a WHOIS answer matching that registry's own "no such domain" reply. Treat as *likely available*; always confirm at a registrar before telling the user it's theirs, and before any public mention of the name.
- `NO RDAP`: nothing could be checked for that TLD. **Not a verdict about the domain.** Report it as not checked and look it up at a registrar by hand. `.ch` and `.es` sit here permanently: their registries refuse port 43 to unregistered clients.
- `UNKNOWN`: the registry was unreachable, rate-limited, or answered something unusable; check manually at a registrar.

Why the indirection matters: a public RDAP redirector answers 404 for every TLD it does not serve, which is indistinguishable from "no registration found". Reading that as availability is the single failure mode that makes this process hand the user a name somebody else already owns.

**About 180 TLDs publish no RDAP at all**: `.io`, `.de`, `.eu`, `.co`, `.it`, `.ru` among them, including two this file recommends below. The script falls back to WHOIS for those and prints which TLDs it took that route for. When you report those columns, say the signal is WHOIS rather than RDAP.

**The two controls.** WHOIS answers are free text in no agreed format, so the script does not parse them. It asks each registry two questions whose answers are already known: `nic.<tld>`, which every registry operates and is therefore always taken, and a long random label, which never is. Whatever the two replies have in common is legal boilerplate and gets subtracted; a candidate is then classified by which of the two remaining shapes it matches. Resembling both equally is `UNKNOWN`, and so is a registry that does not visibly tell its own two controls apart. RDAP needs only the first control, since its answers are structured.

**If the script won't run**, which branch you take depends on what is actually missing:

| Symptom | What to do |
|---|---|
| `python` / `python3` / `py` absent, or (on Windows) a Microsoft Store stub that exits immediately without running anything | Retry with `uv run scripts/check_domains.py …`, then with any project venv interpreter (`.venv/Scripts/python.exe`, `.venv/bin/python`). |
| Still no interpreter, but the network works | Reproduce the script's method by hand, in this order. (1) `GET https://data.iana.org/rdap/dns.json` and find the TLD's registry base URL in `services`. (2) If it is listed: `GET <base>/domain/nic.<tld>` as the control (anything but a domain object means the registry is unreliable, so report `UNKNOWN`), then `GET <base>/domain/<name>.<tld>` with `Accept: application/rdap+json`, reading 404 → `AVAILABLE?`, 200 carrying an RDAP domain object → `REGISTERED`, 200 without one → `UNKNOWN`. (3) If it is **not** listed, never fall back to a public redirector: either report that TLD `NO RDAP`, or, if you have a WHOIS client (`whois <domain>` on a terminal; this is port 43, not HTTP), run the two controls described above and classify against them, labelling the result WHOIS. Say in your answer that you did this instead of running the script. |
| No network access | Skip the check and output the list of exact `name.tld` lookups for the user to run at a registrar. |

Whatever the branch: never guess availability from memory, and report a name you could not check as `not checked`, never as free.

**Domain strategy notes:**

- The name and the domain are two decisions. A strong name with `getname.com`, `name.app`, or `namehq.com` beats a weak name with a clean `.com`. Prefix/suffix conventions (get-, use-, join-, try-, -hq, -app) are normal practice now.
- **Pick the TLD set from the brief; don't inherit the script's default.** Brief item 4 (markets and languages) and item 5 (constraints, must-have TLD) decide which TLDs are worth a request. Pass them explicitly with `--tlds`. The default list (`com, ai, app, io, dev, tools`) exists for when there is genuinely no brief.
- **The 2026 stack for a tech product**, in order: `.com` stays the credibility default for companies; `.ai` is the namespace of the cycle (over a million registrations, high renewal, and a price of roughly 70 to 140 USD a year); `.io` still signals SaaS and devtools, with slowing growth and WHOIS-only checks; `.app` and `.dev` are Google Registry TLDs with HTTPS enforced, right for products and developer tools and a wrong signal for a consumer brand; category TLDs (`.tools`, `.page`, `.menu`, `.studio`, `.design`) for web-native products where the domain is the name; `.co` only as a fallback for a US or global startup brief when `.com` is dead.
- **Country TLDs are a market anchor, not a default.** `.fr`, `.eu`, `.de`, `.uk`, `.nl` measure a national market, not what a product brand wears; request them only when brief item 4 names that country. `.xyz`, `.online`, `.site` are volume TLDs with low renewal and a crypto tail: never a shortlist column unless the brief is crypto or disposable. `.shop` and `.store` are e-commerce only.
- **When a shortlist name is a compound, test the second word as a TLD before testing it as a second-level label**: `quiet.tools` before `quiettools.com`. See `name-types.md` §14 for when a domain hack is allowed at all, and `generation.md` §8 for the construction rules. Country-code TLDs used as hacks (`.ly`, `.ng`, `.cv`, `.to`, `.is`) carry residency rules and registry risk (bit.ly moved to bitly.com after the Libyan registry seized domains it objected to); write that into "Watch out".
- **A `.ai` domain never licenses "AI" in the name.** The TLD is a namespace decision; the morpheme in the word is the dated defect (see `anti-patterns.md`).
- Several TLDs above publish no RDAP (`.io`, `.eu`, `.co`, `.de`, `.it`, `.ru`) and are checked over WHOIS instead; say so when you report them. `.ch` and `.es` cannot be checked at all and come back `NO RDAP`; recommend them where they fit, but never report one as available on this script's say-so.
- Beware inference from a parked page: "for sale, $8,500" changes the calculus; flag the price question, don't negotiate assumptions.
- **Series test.** When the brief says the name is the first of a series (`generation.md` §9), run the script on the shortlist name **and on 2-3 plausible future members**, invented for the purpose, even if those tools do not exist. Do this for the 2-3 families that survive scoring, not for every shortlist entry: the script warns against hundred-name lists for a reason. A system whose second name is already taken is a dead system; better to know before the first name is chosen. Report the future members in the snapshot table under a "series test" header, clearly marked as fictional.

## 2. Trademarks: screening, not clearance

Be precise about what this step is. A real clearance is a **similarity analysis by class and jurisdiction, done by a professional** (a trademark attorney). What this skill performs is a **screening**: catching obvious conflicts early so dead names exit before anyone falls in love with them.

**Concepts you need:**

- Trademarks are registered per **Nice class** (45 classes: 34 goods, 11 services). A conflict lives in *your* classes and adjacent ones: the same word can generally coexist across unrelated classes. One exception matters more than all the others: **marks with a reputation are protected beyond their own classes** (art. 8(5) EUTMR, art. L713-3 CPI, dilution in the US). A famous name is never free just because your class is different: do not reason "different sector, therefore fine" about a household name. Identify the user's 2-4 relevant classes first (software products typically touch 9 and 42; add the business's actual domain).
- Conflict is judged on **likelihood of confusion**: phonetic, visual, and conceptual similarity, not exact string match. "Lumafold" vs "Loomafold" is a conflict candidate.

**Screening workflow per shortlisted name:**

1. Exact search on the relevant registries:
   - **EUIPO** (eSearch plus) and **TMview**: EU and cross-registry aggregate
   - **INPI** (data.inpi.fr): France
   - **USPTO Trademark Search**: United States
   - **WIPO Global Brand Database**: international registrations
2. Sound-alike variants: swap vowels, c/k, i/y, s/z, double letters; search the strongest 2-3 variants.
3. Filter hits to the relevant Nice classes and *live* marks; note dead/expired marks separately.
4. Report per name: `clear at screening level` / `possible conflict (mark, class, jurisdiction)` / `likely blocked`.

**Mandatory wording**: every trademark result ships with this label, verbatim or equivalent:

> *Screening only: indicative, not a legal clearance. Before filing, commercial launch, or serious investment in this name, run a professional clearance search (trademark attorney).*

Never output "trademark: available ✓". False legal confidence is the single worst failure mode of this skill.

## 3. Handles and registries

- **Social handles**: check manually on the platforms the brief cares about (APIs for this are unreliable and against most ToS). An exact handle everywhere is rare and not required; consistent fallbacks (`namehq`, `getname`, `name_app`) are standard.
- **Package registries**: for developer-facing projects, a name collision on npm / PyPI / crates.io can matter more than the domain. Check the exact package name; scoped packages (`@org/name`) are the npm fallback.
- **Agent Skills and plugins**: the collision that matters is the folder namespace (`~/.claude/skills/<name>`, plugin marketplaces) and GitHub repository names; `api.github.com/search/repositories?q=<name>+in:name` answers where the HTML search page does not.
- **App stores**: for consumer apps, search both stores for the exact name and close variants; store search collision with a big incumbent is a findability tax.

## 4. The snapshot table

Deliver verification as one table next to the shortlist:

```
| Name | .com | .ai | .io* | .app | Cost note | TM screening (cl. 9/42) | npm |
|------|------|-----|------|------|-----------|--------------------------|-----|
| …    | REG  | AV? | AV?  | AV?  | .ai premium tier | possible conflict: X (EUIPO, cl. 9) | free |

* .io has no RDAP service: checked over WHOIS.
```

Columns follow the brief's TLD set, not this example. Add a `series test` block under the table when the brief is a series, and drop the cost column only when every checked TLD is standard-priced and free.

Mark any WHOIS-sourced column, as above; the script tells you which ones. A TLD reported `NO RDAP` keeps that word in its cell: leaving it blank or writing `AV?` would claim a check that never happened.

Follow the table with the mandatory trademark label once, underneath.
