# Verification

Verification comes **after** screening, on the shortlist only. Its output is an availability snapshot, not a verdict: availability filters options; it never picks the name.

## 1. Domains

Run `scripts/check_domains.py` on the shortlist (Python 3, stdlib only, network required — see the fallback table below when either is missing):

```bash
python3 scripts/check_domains.py lumafold amberpost --tlds com,fr,io,ai,app
```

It resolves each TLD to its authoritative registry through the IANA bootstrap registry, then queries that registry directly — over RDAP where the TLD publishes it, over WHOIS otherwise. Every TLD is control-tested before any of its answers are trusted. Interpretation:

- `REGISTERED`: taken. (It may still be parked and buyable; note it, don't chase it unprompted.)
- `AVAILABLE?`: no registration found at the authoritative registry — an RDAP 404, or a WHOIS answer matching that registry's own "no such domain" reply. Treat as *likely available*; always confirm at a registrar before telling the user it's theirs, and before any public mention of the name.
- `NO RDAP`: nothing could be checked for that TLD. **Not a verdict about the domain.** Report it as not checked and look it up at a registrar by hand. `.ch` and `.es` sit here permanently: their registries refuse port 43 to unregistered clients.
- `UNKNOWN`: the registry was unreachable, rate-limited, or answered something unusable; check manually at a registrar.

Why the indirection matters: a public RDAP redirector answers 404 for every TLD it does not serve, which is indistinguishable from "no registration found". Reading that as availability is the single failure mode that makes this process hand the user a name somebody else already owns.

**About 180 TLDs publish no RDAP at all** — `.io`, `.de`, `.eu`, `.co`, `.it`, `.ru` among them, including two this file recommends below. The script falls back to WHOIS for those and prints which TLDs it took that route for. When you report those columns, say the signal is WHOIS rather than RDAP.

**The two controls.** WHOIS answers are free text in no agreed format, so the script does not parse them. It asks each registry two questions whose answers are already known — `nic.<tld>`, which every registry operates and is therefore always taken, and a long random label, which never is. Whatever the two replies have in common is legal boilerplate and gets subtracted; a candidate is then classified by which of the two remaining shapes it matches. Resembling both equally is `UNKNOWN`, and so is a registry that does not visibly tell its own two controls apart. RDAP needs only the first control, since its answers are structured.

**If the script won't run**, which branch you take depends on what is actually missing:

| Symptom | What to do |
|---|---|
| `python` / `python3` / `py` absent, or (on Windows) a Microsoft Store stub that exits immediately without running anything | Retry with `uv run scripts/check_domains.py …`, then with any project venv interpreter (`.venv/Scripts/python.exe`, `.venv/bin/python`). |
| Still no interpreter, but the network works | Reproduce the script's method by hand, in this order. (1) `GET https://data.iana.org/rdap/dns.json` and find the TLD's registry base URL in `services`. (2) If it is listed: `GET <base>/domain/nic.<tld>` as the control — anything but a domain object means the registry is unreliable, so report `UNKNOWN` — then `GET <base>/domain/<name>.<tld>` with `Accept: application/rdap+json`, reading 404 → `AVAILABLE?`, 200 carrying an RDAP domain object → `REGISTERED`, 200 without one → `UNKNOWN`. (3) If it is **not** listed, never fall back to a public redirector: either report that TLD `NO RDAP`, or, if you have a WHOIS client (`whois <domain>` on a terminal — this is port 43, not HTTP), run the two controls described above and classify against them, labelling the result WHOIS. Say in your answer that you did this instead of running the script. |
| No network access | Skip the check and output the list of exact `name.tld` lookups for the user to run at a registrar. |

Whatever the branch: never guess availability from memory, and report a name you could not check as `not checked` — never as free.

**Domain strategy notes:**

- The name and the domain are two decisions. A strong name with `getname.com`, `name.app`, or `namehq.com` beats a weak name with a clean `.com`. Prefix/suffix conventions (get-, use-, join-, try-, -hq, -app) are normal practice now.
- **Pick the TLD set from the brief; don't inherit the script's default.** Brief item 4 (markets and languages) and item 5 (constraints, must-have TLD) decide which TLDs are worth a request. Pass them explicitly with `--tlds`. The default list exists for when there is genuinely no brief, and it spends requests on TLDs the project has no use for.
- TLD by context: `.com` remains the credibility default for companies; `.fr`/`.eu` are natural for French/EU-anchored brands; `.ai`, `.io`, `.dev`, `.app` are accepted in tech (with `.io`/`.ai` price and renewal premiums). For a developer tool, the package name can matter more than the domain.
- Several TLDs above publish no RDAP — `.io`, `.eu`, `.co`, `.de`, `.it`, `.ru` — and are checked over WHOIS instead; say so when you report them. `.ch` and `.es` cannot be checked at all and come back `NO RDAP`; recommend them where they fit, but never report one as available on this script's say-so.
- Beware inference from a parked page: "for sale, $8,500" changes the calculus; flag the price question, don't negotiate assumptions.

## 2. Trademarks: screening, not clearance

Be precise about what this step is. A real clearance is a **similarity analysis by class and jurisdiction, done by a professional** (trademark attorney; *conseil en propriété industrielle* in France). What this skill performs is a **screening**: catching obvious conflicts early so dead names exit before anyone falls in love with them.

**Concepts you need:**

- Trademarks are registered per **Nice class** (45 classes: 34 goods, 11 services). A conflict lives in *your* classes and adjacent ones: the same word can generally coexist across unrelated classes. One exception matters more than all the others: **marks with a reputation are protected beyond their own classes** (art. 8(5) EUTMR, art. L713-3 CPI, dilution in the US). A famous name is never free just because your class is different — do not reason "different sector, therefore fine" about a household name. Identify the user's 2-4 relevant classes first (software products typically touch 9 and 42; add the business's actual domain).
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

> *Screening only: indicative, not a legal clearance. Before filing, commercial launch, or serious investment in this name, run a professional clearance search (trademark attorney / conseil en PI).*

Never output "trademark: available ✓". False legal confidence is the single worst failure mode of this skill.

## 3. Handles and registries

- **Social handles**: check manually on the platforms the brief cares about (APIs for this are unreliable and against most ToS). An exact handle everywhere is rare and not required; consistent fallbacks (`namehq`, `getname`, `name_app`) are standard.
- **Package registries**: for developer-facing projects, a name collision on npm / PyPI / crates.io can matter more than the domain. Check the exact package name; scoped packages (`@org/name`) are the npm fallback.
- **App stores**: for consumer apps, search both stores for the exact name and close variants; store search collision with a big incumbent is a findability tax.

## 4. The snapshot table

Deliver verification as one table next to the shortlist:

```
| Name | .com | .fr | .io* | TM screening (cl. 9/42) | npm |
|------|------|-----|------|--------------------------|-----|
| …    | REG  | AV? | AV?  | possible conflict: X (EUIPO, cl. 9) | free |

* .io has no RDAP service: checked over WHOIS.
```

Mark any WHOIS-sourced column, as above — the script tells you which ones. A TLD reported `NO RDAP` keeps that word in its cell: leaving it blank or writing `AV?` would claim a check that never happened.

Follow the table with the mandatory trademark label once, underneath.
