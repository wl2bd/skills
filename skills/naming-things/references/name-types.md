# Name types

The taxonomy serves two purposes: it forces spread during generation (quotas by type), and it maps roughly onto **legal strength**. Trademark law grades distinctiveness on a spectrum, from strongest to weakest protection:

**fanciful** (invented: Kodak) → **arbitrary** (real word, unrelated category: Apple for computers) → **suggestive** (hints at the benefit: Slack) → **descriptive** (says what it is: hard to protect) → **generic** (unprotectable).

The spectrum comes from US case law but the logic holds in most jurisdictions, including EU practice: the less a name describes the product, the more ownable it is, and the more marketing it takes to charge with meaning. That trade-off is the axis every type sits on.

## 1. Descriptive
*The Weather Channel, General Motors, Booking.com*
Instant comprehension, zero marketing needed to explain, and near-zero ownability. Weakest trademark position; boxes the company into today's product. Use for: features and internal tools, where clarity beats ownership. Avoid for: companies and flagship products.

## 2. Suggestive / evocative
*Amazon (scale), Slack (looseness), Pioneer*
Hints at a benefit or quality without stating it. The professional middle ground: meaningful *and* protectable. Risk: the crowded-metaphor problem: everyone in your category mines the same three metaphors. Check competitors before committing to a metaphor family.

## 3. Metaphor / symbol
*Nike (goddess of victory), Puma, Shell, Ghost*
Transfers a loaded image wholesale. Strongest storytelling per letter; instantly visual (a gift to the identity designer). Risk: cliché metaphors (lions, rockets, summits) and cultural mismatch across markets.

## 4. Arbitrary (real word, unrelated)
*Apple (computers), Camel (cigarettes), Orange (telecoms)*
A real, concrete, textured word with no category link. Legally strong, human, memorable, and it demands confidence, because it explains nothing. Often the boldest option on a shortlist. Prefer concrete nouns with sensory texture over abstractions.

## 5. Coined: morpheme-built
*Accenture ("accent on the future"), Verizon (veritas + horizon), Novartis (novae artes, "new skills")*
Invented, but assembled from meaningful roots, so it carries a faint semantic charge. Maximum ownability, clean trademark and domain landscape. Risk: pharma/corporate blandness when the roots are Latin boilerplate; see anti-patterns.

## 6. Coined: empty vessel
*Kodak, Xerox (from xerography), Häagen-Dazs (fake Danish, chosen for texture)*
Pure sound, designed for phonetics and distinctiveness. The strongest legal position that exists and the highest cost to charge with meaning. When building one, design the sound deliberately (see `generation.md` on sound symbolism): Kodak opens and closes on a plosive by design, not accident.

## 7. Compound
*Facebook, YouTube, Salesforce, Mastercard*
Two real words, welded. Clear, sayable, reasonably ownable. Risks: literalness (drifts toward descriptive), length, and the "noun+noun startup" sameness. The weld must feel inevitable, not assembled.

## 8. Blend / portmanteau
*Pinterest (pin + interest), Netflix, Microsoft*
Only keep when the seam is invisible and the result reads as one natural word. The most abused type in amateur naming: default LLM output lands here. Treat every blend as guilty until proven smooth.

## 9. Founder / eponymous
*Ford, Chanel, Bose, McKinsey*
Heritage, accountability, craft connotation. Right for studios, agencies, and craft brands; ties the brand's fate to a person and complicates a future sale.

## 10. Geographic / origin
*Patagonia, Cisco (San Francisco), Adobe (Adobe Creek), Fuji*
Borrows the qualities of a place. Works when the place's character genuinely maps to the brand. Legal note: purely geographic terms can be hard to register if they describe actual origin.

## 11. Borrowed / foreign word
*Uber (German: above/super), Lego (Danish "leg godt", play well), Hulu (Mandarin), Samsung (Korean: three stars)*
Imports meaning plus exotic texture. Mandatory: verify the real meaning, connotations, and pronunciation with sources in that language: borrowed words are the highest-risk type for hidden meanings.

## 12. Experiential
*Safari, Explorer, Quest*
Names the experience of use rather than the product. Energetic, verb-adjacent (good for products people "do"). The territory is heavily mined in consumer software; check for clichés.

## 13. Acronym / initialism
*IBM, BMW, HSBC*
Meaningless until enormous ad spend makes it mean something. Almost never right for a new brand. Legitimate only when inherited (a long legal name that already exists): and even then, consider naming the brand and letting the acronym die.

## 14. Domain-native (domain hack)
*obsidian.md, bun.sh, notion.so, remix.run, bit.ly*
The TLD is not an address, it is the last syllable of the name. The name is the full domain, read as one phrase: `remix.run`, `bolt.new`, or an invented `quiet.tools`. Nobody says "quiet"; they say "quiet dot tools". What it buys: a two-word name with a free domain in a landscape where every one-word .com is gone; the category is carried by the TLD, so the left part is free to be evocative; the URL is the wordmark. Legal strength: the left part alone is usually descriptive or generic and hard to protect; the combination is protectable as a mark but only as written with the dot, which limits stretch. Treat the TLD as part of the trademark search string. How to build one: `generation.md` §8; real cases in `corpus.md` §14.

**When to propose it, and how much.** The criterion is not company versus tool; it is **said versus typed**. A name that will live mostly in an address bar, a README, a package manager or a tweet can be a domain hack: the dot costs nothing where the name is typed. A name that will be said on the phone, in a pitch, on a podcast or on a business card pays the dot as a spelling tax every time. Brief items 1 and 5 already decide, without an extra question:

| Brief item 1 | Domain-native in the shortlist |
|---|---|
| tool, side project, package, directory, web page, internal tool | a territory in its own right; 2 to 3 of the 6-10 names |
| company, consumer product, anything with an app store listing or packaging | 1 at most, placed at the risky end of the shortlist, risk written in "Watch out" |

When item 1 is ambiguous (a tool that may become a company, a product not yet known to be sold), it is worth one of the two allowed brief questions: *"Will this name be said aloud more than it is typed?"* The user often does not know whether it is a company; they know how the name will travel. Country-code TLDs (.ng, .ly, .cv, .to, .is) carry residency rules, registry instability and geopolitical risk; flag them in "Watch out". When the name's syntax forbids a dot (a package, a CLI command, a skill folder), the quota does not apply; the nearest equivalent is a suffix that is also a live TLD, so the family could later sit on `name.<tld>`.

---

**Using the taxonomy:** during generation, tag each candidate with its type and keep rough quotas (SKILL.md step 3). During shortlisting, deliberately mix types so the decision space spans the spectrum: one descriptive-leaning safe option, several suggestive/metaphor/arbitrary, at least one coined, and domain-native dosed by the said-versus-typed rule above. During evaluation, use the spectrum position as the "ownability" input. `corpus.md` holds real names filed under each type, with what each one buys and what it costs.
