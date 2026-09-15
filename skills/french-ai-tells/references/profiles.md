# Profiles

Two independent axes. **Context profiles** set how strict to be for an audience. **Voice profiles** set how the prose should sound. A blunt blog post and a warm piece of documentation are both valid pairings.

## Context profiles

Pass `--context` or let the cues below pick one. When auto-detection is uncertain, say which profile you used and why; the writer can override.

| Profile | For | Leniency |
|---|---|---|
| `linkedin` | Short social posts, LinkedIn, X | Fragments and visual formatting accepted; hashtag and endorsement tells strict |
| `blog` | Default. Long-form prose, articles, newsletters | Every rule at full strength |
| `technique` | Technical articles with code, architecture, APIs | Technical terms pass; hedging that is accurate passes |
| `docs` | Documentation, READMEs, guides | Clarity over voice; lists and fragments are the register |
| `email` | Professional emails, cold outreach | Salutation and closing formulas are correct form; chatbot openers forbidden |
| `communique` | Press releases, investor updates, fundraising and sponsor emails | Extra strict on promotional language, inflation and closers |
| `academique` | Theses, papers, reports with a bibliography | Nominalisation, passive and impersonal forms much more tolerated |
| `management` | Internal memos, strategy notes, board reports | Extra strict on managerial boilerplate |
| `familier` | Slack, DMs, quick replies, very short texts | Only the worst offenders |

### Auto-detection cues

| Signal | Profile |
|---|---|
| Under 300 words with hashtags or mentions | `linkedin` |
| Three sentences or fewer, conversational | `familier` |
| Code blocks, API references, architecture | `technique` |
| Step-by-step instructions, parameter lists, README shape | `docs` |
| Salutation (« Bonjour », « Madame, Monsieur ») | `email` |
| Company name with figures, funding, launch or partnership news | `communique` |
| Bibliography, citations, footnotes | `academique` |
| Memo header, « Note à l'attention de », internal direction | `management` |
| No strong signal | `blog` |

### Tolerance matrix

Rules absent from the table apply at full strength everywhere. **Strict**: flag every instance. **Relaxed**: flag clear or repeated instances. **Extra strict**: flag borderline instances too; in a press release, one « écosystème dynamique » undermines the whole text. **Skip**: don't audit the category.

| Rule | linkedin | blog | technique | docs | email | communique | academique | management | familier |
|---|---|---|---|---|---|---|---|---|---|
| Chatbot artifacts, summary openers, generic closers (P0) | strict | strict | strict | strict | strict | strict | strict | strict | strict |
| Em dashes | relaxed (2 per post) | strict | strict | relaxed | strict | strict | relaxed | strict | skip |
| Bold overuse | relaxed (bold hook) | strict | strict | relaxed | strict | strict | strict | strict | skip |
| Emoji in headings | relaxed (1-2 at line end) | strict | strict | skip | strict | strict | strict | strict | skip |
| Excessive bullets | skip | strict | relaxed | skip | strict | strict | relaxed | relaxed | skip |
| Hedging, conditional-hedge | strict | strict | relaxed | relaxed | relaxed | extra strict | relaxed | strict | skip |
| Tier 1 vocabulary | strict | strict | partial (below) | relaxed | relaxed | strict | strict | strict | P0 only |
| Tier 2 vocabulary | relaxed | strict | partial (below) | relaxed | relaxed | strict | relaxed | strict | skip |
| Transitions at sentence head | skip | strict | strict | relaxed | relaxed | strict | relaxed | strict | skip |
| Impersonal distancing | strict | strict | relaxed | relaxed | relaxed | strict | skip | strict | skip |
| Managerial boilerplate | strict | strict | relaxed | relaxed | relaxed | extra strict | skip | extra strict | skip |
| Promotional language | relaxed | strict | strict | strict | strict | extra strict | strict | strict | skip |
| Significance inflation | strict | strict | strict | relaxed | strict | extra strict | strict | strict | skip |
| Copula avoidance | skip | strict | relaxed | skip | relaxed | strict | relaxed | strict | skip |
| Uniform paragraph length | skip | strict | strict | relaxed | relaxed | strict | relaxed | strict | skip |
| Numbered list inflation | relaxed | strict | relaxed | skip | strict | strict | skip | relaxed | skip |
| Rhetorical questions | relaxed (1 hook) | strict | strict | strict | relaxed | strict | strict | strict | skip |
| « Ce n'est pas X, c'est Y », negation chains | strict | strict | strict | relaxed | strict | extra strict | relaxed | strict | relaxed |
| Generic conclusions, future-narrative closers | strict | strict | strict | skip | strict | extra strict | strict | extra strict | skip |
| Hashtag stuffing | strict (P0) | relaxed | relaxed | skip | strict | extra strict (P0) | skip | skip | skip |
| Bare noun-phrase lists | strict | strict | relaxed | relaxed | strict | strict | relaxed | extra strict | skip |
| Tier 3 phrase clusters | strict | strict | strict | relaxed | strict | extra strict | relaxed | extra strict | skip |
| Social endorsement closers | strict | strict | strict | skip | strict | strict | skip | skip | relaxed (1 in a DM) |
| Hedge-stacked predictions | strict | strict | relaxed | relaxed | strict | extra strict | relaxed | strict | skip |
| « Véritable / vrai » inflation | strict | strict | strict | relaxed | strict | extra strict | strict | strict | skip |
| Calques of English | strict | strict | relaxed | relaxed | strict | strict | strict | strict | relaxed |
| Subjectless fragments, agentless passives | relaxed | strict | relaxed | skip | relaxed | strict | skip | relaxed | skip |
| Title Case, English typography | strict | strict | strict | relaxed | strict | strict | strict | strict | skip |

**`technique` vocabulary exceptions.** These have a real technical sense and pass in technical context: « robuste », « évolutif », « scalable », « performant », « optimiser », « implémenter », « écosystème » (a platform's actual ecosystem), « faciliter », « transparent » (a transparent proxy, a transparent migration), « permettre de », « contribuer à ». Still flag: « plonger dans », « tapisserie », « phare », « témoigne de », « qui change la donne », « tirer parti de » as inflation.

**`email` conventions.** « Bonjour Prénom, », a light closing (« Bien à vous », « Bonne journée ») and a short signature are correct French form, never tells. Their absence in a cold email is itself a calque of English. Formal closings in an administrative or legal letter are the register, not boilerplate.

**`academique` caution.** Nominalisation, the passive and « il convient de » are the conventions of French academic prose. Flag them only inside a cluster of other tells.

## Voice profiles

Voice is optional. When the writer names none, infer it from the source's existing register and impose no persona on a text that already has one. Every target below is bounded by "What a rewrite may add" in SKILL.md: a voice profile brings out what the source already has and manufactures nothing.

**`decontracte`**: short sentences (around 14 words on average), fragments allowed. « On » rather than « nous » where the source is already informal. Keep the source's « tu » or « vous », its first person and its concrete touches; add none. Near-zero jargon. Keep warm hedges (« je crois », « à mon avis »), cut corporate ones (« il convient de noter »). Dropped « ne » only if the source already drops it. *Blog posts, social, community.*

**`professionnel`**: active voice for most sentences. Vary length; never three sentences in a row of about the same size. A concrete claim per paragraph (figure, name, date) when the source provides one. Affirm rather than stack polite conditionals: « C'est l'écran le plus difficile à concevoir », not « il me semblerait que cet écran pourrait présenter des difficultés ». Keep the explicit ask where the source makes one; invent neither facts nor an ask. No self-deprecation (« je ne voudrais pas vous déranger », « je sais que votre temps est précieux »). *LinkedIn, investor emails, proposals.*

**`technique`**: plain « est » and « a » over inflated substitutes (« fait office de », « se positionne comme »). One idea per sentence; imperative or infinitive for instructions, consistently. Jargon allowed, defined on first use. Tables and lists only where content is list-shaped. *Docs, technical articles.*

**`chaleureux`**: address the reader directly where the source already does, and keep its acknowledgments rather than adding any. Stronger verbs instead of intensifiers (« très », « vraiment », « incroyablement »). No performative-empathy openers (« Je comprends parfaitement ce que vous ressentez »). Medium sentences (15 to 20 words) for an unhurried pace. *Mentoring, onboarding, thank-you notes.*

**`direct`**: lead with the claim; cut « Il est important de noter que » windups. Periods for emphasis, dashes rare. No padding to reach three items. Near-zero hedging; flag every « pourrait / potentiellement » stack. Short declaratives, an occasional long sentence for contrast. *Decision memos, opinion pieces, hard feedback.*

**Calibrate to a sample.** When the writer supplies their own writing (« garde mon style, voici un post »), analyse its sentence-length pattern, register (tu or vous, on or nous, dropped « ne » or not), paragraph openings and recurring word choices, and match those instead of a named profile. Keep their register: if they write « des trucs », the rewrite keeps « des trucs ».

**How voice composes with context.** Voice sets the target; context sets how hard to enforce it. A voice target always applies, even where the context skips that category: `technique` voice still prefers plain copulas in a `familier` context. Where both govern the same rule and agree, they reinforce. Where they disagree, resolve toward the stricter. Sensible default pairings: `decontracte` with `familier` or `linkedin`, `professionnel` with `email` or `communique`, `technique` with `docs` or `technique`, `direct` with `management`.
