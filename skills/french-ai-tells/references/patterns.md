# Pattern catalog

Every pattern below is a French manifestation of a tell language models overproduce. Examples in « » are illustrations of the tell or of the fix; quote them as such.

Provenance matters for how much weight a hit carries. Entries marked **(FR sources)** come from French-language practitioner research (Blog du Modérateur, Rédacteur.com, Projet Voltaire, Cours NDRC, Startups Nation, French Wikipedia guidance), listed in [sources.md](sources.md). Everything else is a French transposition of a pattern documented in English by avoid-ai-writing: the shape is well attested in LLM output across languages, but its French frequency has not been measured. No French study with a published protocol compares word frequencies in human and machine text, so every threshold here is a convention, not a statistic.

## 1. Formatting and typography

- **Em dashes (—) and en dashes used as dashes (–)**: replace with a comma, a colon, parentheses, or two sentences. Target: zero. Hard maximum: one per 1,000 words, headings included. Two carve-outs: the dialogue dash (tiret de dialogue) opening a line of speech in fiction or an interview, and a dash separating a bold lead term or a link from its description in a list item (`- **Terme** – description`). A dash splice mid-sentence always counts.
- **Bold overuse**: at most one bolded phrase per major section, often none. If something deserves bold, restructure the sentence to lead with it.
- **Emoji in headings**: remove. Social posts may keep one or two, at the end of a line.
- **Excessive bullet lists**: turn bullet-heavy sections into paragraphs. Bullets stay for genuinely list-shaped content (comparisons, steps, parameters).
- **Title Case headings**: French capitalises only the first word and proper nouns. « Les Enjeux De La Transformation Numérique » → « Les enjeux de la transformation numérique ». Same tell in body text: capitalised months and days (« Lundi 3 Mars »), capitalised nationality adjectives (« une startup Française »). This one is both a calque and a strong signal in French.
- **English typography in French prose**: straight or English curly quotes ("…", “…”) where the rest of the text uses « », amounts written `1,500€` or `€1500` instead of `1 500 €`, a decimal point instead of a comma. Weak and corroborating on its own, since many French writers type without « » or non-breaking spaces. The stronger tell is inconsistency inside one text. Fix toward the convention the text mostly uses; see the marks pass in SKILL.md.
- **Immaculate typography in a casual register**: perfect non-breaking spaces before `? ! : ;` in a Slack message or a quick comment is corroborating evidence, never proof. The inverse matters more: when editing someone's casual text, keep their typos, abbreviations and missing accents on capitals. Smoothing them away erases the fingerprint that marks the text as theirs.

## 2. Sentence structure

- **« Ce n'est pas X, c'est Y »**: and its relatives « Il ne s'agit pas de X, mais de Y », « Moins X que Y », « X ? Non. Y. ». Rewrite as a direct positive statement. Maximum one per piece, and only when it serves the argument. Catch the **split form**, where negation and correction fall in two sentences: « Le sujet n'est pas la vitesse. Le vrai sujet, c'est la confiance. » Each sentence looks innocent alone, which is why it slips past. Catch the **countdown**: « Ce n'est pas le prix. Ce n'est pas la fonctionnalité. C'est la confiance. » Cut straight to the positive claim. Catch the **tailing negation**, a bare negative fragment tacked onto a sentence: « Les options viennent de l'élément sélectionné, sans prise de tête. » Write a real clause or cut it. Carve-out: negations listing spec constraints (« aucune dépendance, aucune télémétrie ») are list content.
- **Negation chains**: two or more « pas de… » / « sans… » / « aucun… » items in a row (« Pas de blabla. Pas de jargon. Juste du concret. », « Sans engagement, sans carte bancaire, sans surprise. »), stacked « Il n'a pas… » clauses for rhythm (« Il n'a pas demandé. Il n'a pas attendu. »), and the negated-then-repeated verb (« Ne dites pas pivot. Dites correction. »). The chain performs decisiveness. Fix: say what the thing is. One negation earns its place when the reader would otherwise assume the opposite. Carve-outs: factual inventories mid-sentence (« l'appel ne prend ni argument, ni en-tête, ni corps ») and narration with restated subjects.
- **Binary set pieces**: « non seulement X, mais aussi Y », « à la fois X et Y ». Once in a piece is fine; repeated, it is a pattern. **(FR sources)**
- **Hollow intensifiers**: cut « véritable » and « vrai » when they only intensify (« un véritable atout »), « réellement », « vraiment », « littéralement », « clairement », « franchement », « pour être honnête », « soyons clairs ». Default fix is deletion: « Cela simplifie vraiment le processus » → « Cela simplifie le processus ». Keep « en réalité » when it marks a real gap between expectation and fact (« on attendait un gain ; en réalité, le temps de réponse a doublé »).
- **Vague endorsement**: « à lire absolument », « mérite le détour », « vaut le coup d'œil », « à ne pas manquer », « à suivre de près ». A generic thumbs-up replacing a reason. Say why it matters.
- **Hedging**: cut « peut-être », « potentiellement », « il est important de noter que », « il convient de préciser que ». Make the point.
- **Conditional-hedge overuse**: « cela pourrait améliorer les résultats », « il serait intéressant de noter », « il semblerait que ». State it in the indicative when the source supports the claim. **(FR sources)** The polite conditional stacked three deep (« Je serais ravi de pouvoir vous proposer un échange qui pourrait vous intéresser ») is the same move in business French.
- **Sentence-initial hedge adverbs**: « Fondamentalement, », « En substance, », « Globalement, », « Essentiellement, ». Cut or state directly. **(FR sources)**
- **Missing bridges**: if paragraphs could be rearranged without the reader noticing, the piece lacks connective tissue.
- **Compulsive rule of three**: vary the groupings. Two items, four, or a full sentence. At most one « adjectif, adjectif et adjectif » per piece.
- **Adjective stacking**: « une solution fiable, performante, évolutive et sécurisée ». Each word may be defensible; the pile is the tell. Keep the one that matters and prove it.

## 3. Vocabulary

Words sit in three tiers by how reliably they signal machine text.

- **Tier 1: always flag.** Replace on sight.
- **Tier 2: flag in clusters.** Fine alone; two or more in one paragraph is a strong signal.
- **Tier 3: flag by density.** Common words that models overuse; flag when they saturate the text.

**Match inflected forms.** Each entry covers gender, number, conjugations and derived adverbs (« crucial » flags « cruciale », « cruciaux » ; « optimiser » flags « optimisé », « optimisation ») unless a variant carries a distinct legitimate sense.

### Tier 1: always replace

Tier 1 splits in two bands. The edit is the same; what a flag means differs.

**1A: AI frequency markers.** Words far more frequent in machine text. A cluster is evidence about how a passage was produced.

**1B: clarity edits.** Wordiness and inflated formality. Replacing them is good writing whoever wrote the sentence, and a 1B hit is **not** evidence of machine authorship. In detect mode, report the two bands separately.

#### Tier 1A: AI frequency markers

| Replace | With |
|---|---|
| plonger dans, plongeons dans, plongée au cœur de | examiner, regarder, entrer dans le détail de |
| paysage (metaphor: « le paysage numérique ») | secteur, marché, domaine |
| tapisserie, mosaïque (metaphor) | (describe the actual complexity) |
| paradigme, changement de paradigme | modèle, approche (or say what changed) |
| embarquer (« embarquez pour »), se lancer dans l'aventure | commencer, lancer |
| phare (metaphor: « un phare pour ») | exemple, référence (name what it guides) |
| témoigne de, est un témoignage de | montre, prouve |
| robuste | solide, fiable |
| de pointe, à la pointe de | récent, avancé (or cite the benchmark) |
| tirer parti de, capitaliser sur | utiliser, s'appuyer sur |
| charnière, un moment charnière, un tournant décisif | (state what happened) |
| souligne (« souligne l'importance de ») | montre |
| méticuleux, minutieusement | soigné, précis |
| fluide, sans friction, sans couture | simple, rapide (or say what is removed) |
| révolutionnaire, qui change la donne | (say what changed and why it matters) |
| l'avenir s'annonce prometteur, seul le temps nous le dira | (cut: say something specific or nothing) |
| niché | situé, se trouve |
| florissant, en plein essor, prospère | en croissance (or cite a number) |
| malgré les défis… continue de prospérer | (name the challenge and the response, or cut) |
| mettre en lumière, mettre en exergue | montrer |
| décortiquer | expliquer, détailler |
| effervescent, foisonnant | actif (or cite what makes it busy) |
| subtilités, complexités | (name them, or « détails », « problèmes ») |
| en constante évolution, en perpétuelle mutation | qui change (or describe how) |
| holistique | complet, global (or say what is included) |
| actionnable | concret, applicable |
| impactant | efficace, marquant (or describe the effect) |
| apprentissages (for "learnings") | enseignements, leçons, ce qu'on a appris |
| leader d'opinion, thought leader | expert (or describe the contribution) |
| synergie | (describe the combined effect) |
| symphonie, alchimie (metaphor) | (describe the coordination) |
| embrasser (« embrasser le changement ») | adopter, accepter, passer à |
| au cœur de **(FR sources)** | dans, au centre de (or cut) |
| naviguer (metaphor: « naviguer dans la complexité ») **(FR sources)** | gérer, traverser, s'y retrouver |
| crucial **(FR sources)** | important, décisif (or a figure) |
| essentiel, « il est essentiel de » **(FR sources)** | nécessaire, indispensable (or rephrase) |
| fondamental **(FR sources)** | de base, central |
| captivant, fascinant, troublant **(FR sources)** | (describe concretely what holds attention) |
| harmonie, harmonieux **(FR sources)** | (describe concretely) |
| réinventé **(FR sources)** | transformé, refait (or a concrete verb) |
| verdoyant **(FR sources)** | (keep only in a real description of nature) |
| dynamique (as praise) **(FR sources)** | (cut or say what moves) |
| innovant, innovation (as a claim) **(FR sources)** | (say what is new) |

**On the (FR sources) figures.** « Réinventé » is reported as about 1,033 times more frequent in ChatGPT output than in human web text, « verdoyant » about 600 times (Blog du Modérateur, Startups Nation). These come from practitioner analyses without a published protocol. Treat them as well-supported conventions.

#### Tier 1B: clarity edits

Wordiness and administrative inflation, not authorship evidence.

| Replace | With |
|---|---|
| procéder à (« procéder à l'analyse ») | analyser (the direct verb) |
| effectuer, réaliser (« réaliser une mise à jour ») | mettre à jour (the direct verb) |
| permettre de (« cela permet de gagner du temps ») | cela fait gagner du temps |
| en raison du fait que, du fait que | parce que |
| dans le but de, dans l'optique de | pour |
| s'avérer être | être |
| au niveau de (vague) | pour, dans, sur (name the relation) |
| en termes de | pour, côté (or rewrite) |
| mettre en place | créer, installer, lancer |
| être en mesure de | pouvoir |
| à l'heure actuelle, au jour d'aujourd'hui | aujourd'hui |

### Tier 2: flag when 2+ appear in the same paragraph

| Replace | With |
|---|---|
| exploiter, optimiser | utiliser, améliorer |
| favoriser, encourager | aider, soutenir |
| renforcer, consolider | (say what gets stronger, by how much) |
| sublimer, rehausser | améliorer |
| libérer (« libérez le potentiel ») | permettre (or say what becomes possible) |
| fluidifier, rationaliser | simplifier, accélérer |
| donner les moyens de, autonomiser | permettre |
| piloter, porter (a project, as inflation) | diriger, mener |
| résonner, résonner avec | parler à, toucher |
| révolutionner, transformer | changer (or describe the change) |
| faciliter | aider, permettre |
| sous-tendre | fonder |
| nuancé | précis (or name the nuance) |
| multidimensionnel, à multiples facettes | (name the facets, or cut) |
| écosystème (metaphor) | marché, réseau, communauté |
| une myriade de, une pléthore de, une multitude de, un large éventail de **(FR sources)** | beaucoup de, plusieurs (or a number) |
| englober | inclure, couvrir |
| catalyser, galvaniser | déclencher, mobiliser |
| repenser, réinventer | refaire, reconcevoir |
| cultiver | développer |
| éclairer, illustrer | expliquer, montrer |
| pierre angulaire, pilier | base, élément central |
| primordial | le plus important |
| en passe de, sur le point de, appelé à | va, devrait |
| émergent, naissant | nouveau, récent |
| quintessence | exemple type |
| transversal, global (as vague umbrella) | (name the scope) |
| discrètement (« transforme discrètement ») | (cut, or name the concrete contrast) |
| profondément (significance only: « profondément ancré ») | (cut, or say what runs deep) |
| levier, leviers | moyen (or name the action) |
| enjeux, enjeu clé | question, risque (or name it) |
| incontournable, clé (adjective) | important (or say why) |
| accompagner (« nous vous accompagnons ») | aider, travailler avec (say what is done) |
| valeur ajoutée | (name the gain) |
| agilité, résilience | (describe the behaviour) |
| notamment, particulièrement, essentiellement **(FR sources)** | en particulier, surtout (or cut) |
| dorénavant, en outre, cependant **(FR sources)** | désormais, aussi, mais |
| s'inscrire dans, s'articuler autour de **(FR sources)** | faire partie de, porter sur |
| contribuer à, se traduire par **(FR sources)** | aider à, donner (a precise verb) |
| mettre en œuvre **(FR sources)** | appliquer, lancer (legal texts excepted) |
| efficacement **(FR sources)** | (cut, or a metric) |
| transparence, transparent (managerial buzzword) **(FR sources)** | (say what can be consulted) |

### Tier 3: flag only at high density

Normal words. Flag when the text is saturated with them, a sign that vague praise filled the space of specifics.

| Word | What to do |
|---|---|
| significatif, considérable | a number, a comparison |
| efficace | how, or a metric |
| performant, performance | cite the measure |
| évolutif, scalable | what scales, to what |
| percutant, convaincant | why |
| sans précédent, inédit | name the precedent it breaks, or cut |
| exceptionnel, remarquable | what makes it so |
| sophistiqué, avancé | describe it |
| déterminant | the role it played |
| de classe mondiale, haut de gamme, premium | a benchmark or comparison |
| durable, pérenne | the time horizon and the constraint |
| potentiel | what exactly is possible |
| optimal | optimal against what |

### Tier 3 phrases: flag at 2+ uses of one phrase, or 3+ distinct phrases in a piece

The cluster rule catches the shape models take when they vary their own boilerplate to seem less repetitive.

| Phrase | What to do |
|---|---|
| « Dans le paysage actuel de… » **(FR sources)** | cut; open on the news |
| « À l'ère de… », « À l'heure de… », « À l'heure où… » **(FR sources)** | cut or give the specific context |
| « Dans un monde qui évolue à un rythme effréné », « Dans un monde en constante mutation » **(FR sources)** | cut |
| « Il est important de noter que », « Il est crucial de noter que » **(FR sources)** | state the fact |
| « En conclusion », « Pour conclure », « En résumé », « En somme » **(FR sources)** | the conclusion should be evident |
| « besoin urgent », « nous devons » (generic rallying) **(FR sources)** | say who must do what, by when |
| « enjeux et opportunités », « défis et perspectives » **(FR sources)** | name one enjeu, one opportunity |
| « transformation numérique », « transformation digitale » **(FR sources)** | say what is being digitised |
| « bonnes pratiques » **(FR sources)** | say which |
| « création de valeur », « proposition de valeur » | name the value |
| « conduite du changement », « montée en compétences » | name the change, the skill |
| « approche globale et cohérente », « vision à long terme » | describe the approach, cite the horizon |
| « à l'intersection de X et Y », « l'intégration de X et Y » | pick the overlap that matters |
| « expérience utilisateur optimale », « parcours client fluide » | describe what the user does |
| « pensé pour », « conçu pour » (as filler) | cut; state the property |

## 4. Template phrases

A sentence with a slot where any noun or adjective fits and still sounds the same was generated, not written.

- « une [adj] avancée vers une [adj] infrastructure », « un pas de géant pour [nom] » → the specific capability, benchmark or outcome.
- « Que vous soyez [X] ou [Y] » → false breadth. Address the audience you mean, or cut. « Que vous soyez fondateur de startup ou DSI d'un grand groupe » means « tout le monde ».
- « J'ai récemment eu le plaisir de », « J'ai l'immense plaisir de vous annoncer », « Je suis ravi(e) de partager » → say what happened: « J'ai parlé avec », « Nous lançons ».

## 5. Transitions and frames

- « Par ailleurs », « De plus », « En outre », « Ainsi », « Dès lors », « Par conséquent », « Enfin », « Cependant » at the head of sentence after sentence → restructure so the link is evident, or use « et », « aussi », « mais ». **(FR sources)**
- « À l'ère de », « Dans un monde où », « À l'heure où » → cut or give the concrete context.
- « Il est à noter que », « Notons que », « Il convient de souligner que », « Il faut souligner que », « Il est intéressant de constater que » → state the fact. **(FR sources)**
- « Voici ce qui est intéressant », « Ce qui retient l'attention », « Voici ce qui m'a marqué » → reader-steering frames. Let the content signal its importance, or make the lead-in specific: « Le chiffre de revenu compte parce que… ».
- « En conclusion, il convient de souligner… », « Il ressort de cette analyse que… », « Il y a lieu de noter que… » → AI summary openers, P0. Cut or rewrite entirely. **(FR sources)**
- « Quand il s'agit de », « En ce qui concerne », « S'agissant de » → talk about the thing directly.
- « Au final », « En fin de compte », « Au bout du compte » → cut.
- « Cela étant dit », « Ceci dit », « Cela dit » → cut or « mais », « pourtant ». No single one repeated.

## 6. Impersonal distancing (French-specific)

« Il s'avère que », « Il apparaît que », « Il semblerait que », « Force est de constater que », « Il n'est pas inutile de rappeler que ». The preferred French form of impersonal AI hedging. Fix: the direct form, « Les chiffres montrent que », « X montre que », or the claim itself. **(FR sources)** The impersonal « il » is native French; flag these frames when they stack or replace a claim the writer could make directly.

## 7. French managerial boilerplate (French-specific)

« s'inscrit dans une démarche de… », « mise en œuvre d'une approche globale », « dans une logique de… », « démarche qualité », « leviers de performance », « atout différenciateur majeur », « capitaliser sur nos fondamentaux », « fédérer les énergies ». Strongest in internal memos, strategy notes and business-school register. Rewrite concretely: who does what, with which result. **(FR sources)**

Variant, **managerial noun lists**: `• Transformation numérique • Enjeux stratégiques • Vision globale • Excellence opérationnelle`. Abstract nouns, no verb, no data. Rewrite as full claims or prose. **(FR sources)**

## 8. Calques of English (French-specific)

The French is correct and a French reader still feels it comes from elsewhere. These are structure tics, not errors, and they overlap heavily with machine output because models think in English-shaped templates. Judgment calls unless marked.

- « J'espère que ce message vous trouve bien » (from "I hope this email finds you well"): template marker, P1. Cut.
- « Je vous aide à… », « J'aide les X à Y » (from "I help X do Y"): say what you do.
- The marketing imperative: « Découvrez », « Boostez », « Libérez », « Transformez » as hooks.
- Possessive in every sentence: « votre équipe », « vos utilisateurs », « votre produit ». French prefers the definite article or an impersonal turn.
- « faire sens » (from "make sense"): « avoir du sens », « se tenir ».
- « adresser un problème / un sujet » (from "address"): « traiter », « s'attaquer à ».
- Business anglicisms that read as pretentious in French: « délivrables » (livrables), « insights » (enseignements), « actionnable » (applicable), « leverager » (s'appuyer sur), « reach out » (contacter), « scope » (périmètre). Trade terms the field actually uses in French (design, dashboard, onboarding, SaaS, repo) are not calques; keep them.
- A cold email opening on the first name alone (« Thomas, ») or ending with no closing formula: in French it reads as automated mailing, the opposite of direct. In `email`, « Bonjour Thomas, » and a light close are the correct form, never a tell.
- **Back-translation test.** Translate the text into English without touching sentence structure. If it passes as native English, it was written in English and translated.

## 9. Significance and inflation

### Significance inflation
« marquant un tournant décisif dans l'évolution de… », « un moment charnière pour tout le secteur ». State what happened and let the reader judge. If the sentence still works after deleting the inflation clause, delete it.

### Aphorism formulas
Slot-fill profundity: « X est le langage de Y », « la confiance est la nouvelle monnaie », « l'architecture de la confiance », « X devient un piège », « X n'est pas un outil, c'est un miroir ». Replace with the concrete claim: « la symétrie est le langage de la confiance » → « les mises en page symétriques paraissent plus prévisibles ». Carve-out: quotations and established sayings (« le temps, c'est de l'argent »).

### Generic future-narrative closers
« pourrait bien devenir l'un des grands enjeux de la prochaine décennie », « est en passe de devenir le prochain chapitre de ». Modal + « devenir » + « l'un des plus… ». Grammatically a prediction, no testable content. Fix: the falsifiable version (« X dépassera Y d'ici 2027 ») or cut.

### Hedge-stacked predictions
« pourrait potentiellement créer », « pourrait à terme permettre », « serait susceptible de peut-être ». Either word alone is acceptable; the stack cancels itself. Pick one. **(FR sources)** document the same accumulation in French.

### « Véritable / vrai / réel » inflation
« une véritable stratégie data », « un vrai modèle économique », « une réelle valeur ajoutée ». The intensifier on an abstract noun implies the rest of the field is fake without naming what makes this one real. Carve-out, named contrast: « de vrais revenus clients, pas des subventions » is honest contrastive writing. Fix otherwise: drop the adjective and add the claim.

### Moral-adjective category errors
Moral adjectives on non-agentic nouns: « une courbe honnête », « un chiffre sincère », « une représentation plus fidèle » (when it means clearer), « signalé honnêtement ». State the concrete property: « une courbe plus réaliste », « noté ». Related: gratuitous universals, « enseigné dans tous les cours de première année » → « enseigné en première année ».

### Transformation crutch
Repeated unexplained relabeling: « l'inquiétude se transforme en panique », « la fonctionnalité devient une stratégie », « le risque devient réel ». P2 judgment. Ask what changed; use supplied facts, never invent a mechanism. Preserve literal changes (« l'eau se transforme en glace ») and changes explained in the passage.

### Novelty inflation
« un concept dont personne ne parle », « il a inventé un terme que je ne connaissais pas », « ce que personne ne vous dit sur ». Describe what the person did with the concept. Also flag invented labels coined mid-sentence and never defined (« le paradoxe de la supervision », « la taxe de coordination »): define on first use or describe the mechanism. **(FR sources)** for the novelty frame.

### Promotional language
Brochure prose: « niché au cœur d'un écrin de verdure », « un pôle d'innovation dynamique », « au cœur du dynamique écosystème de la French Tech ». Plain description: « situé à Lyon 7e », « 12 startups ». **(FR sources)**

### Formulaic challenges
« Malgré les défis, l'entreprise continue de prospérer », « Face aux vents contraires, l'organisation reste résiliente ». Name the challenge and the response, or cut. **(FR sources)**

## 10. Attribution and credibility

### Vague attributions
« Les experts estiment », « Des études montrent », « Selon de nombreux spécialistes », « Les leaders du secteur s'accordent à dire ». Cite the source (« selon l'enquête INSEE 2024, n = 2 400 ») or state the claim directly. **(FR sources)**

### Notability name-dropping
« cité par Les Échos, Le Monde, BFM Business et Forbes ». One source with context beats four names. Related, **historical analogy stacking**: « comme l'imprimerie, le télégraphe et Internet avant elle ». Keep the one parallel that explains something.

### Vague third-party validation
« des tests indépendants confirment », « un organisme extérieur nous classe premiers », « selon les analystes ». Name the source, the test, the result. Carve-out: checkable validation (« audit SOC 2 Type II par X, mars 2026 »).

### Hollow participial clauses
« illustrant ainsi l'engagement de la région, reflétant des décennies d'investissement et soulignant une nouvelle ère de collaboration ». Pseudo-analysis. **(FR sources)** The same move without the participle: « cela reflète une tendance plus large », « cette décision symbolise un engagement envers l'excellence ». Show a consequence or cut.

### Cutoff disclaimers
« À ma connaissance », « Selon les informations dont je dispose », « À la date de ma dernière mise à jour », « Je n'ai pas accès aux données en temps réel ». Find the information or remove the sentence. **(FR sources)**

### Speculative gap-filling
Guesses formatted as background: « reste relativement discret sur », « aurait débuté sa carrière dans », « semble avoir étudié à ». Worse than a disclaimer, because the reader can't tell known from invented. Cut or source it.

### Unfilled placeholders
`[Votre nom]`, `[Insérer le lien]`, `[Nom de l'entreprise]`, `2026-XX-XX`, `<!-- ajouter la source -->`. A publishing bug: fill or delete.

### Chatbot citation markup leaks
`citeturn0search0`, `contentReference[oaicite:0]{index=0}`, `oai_citation`, `[attached_file:1]`, `grok_card`. Fingerprints, not patterns. Strip every token; replace a meaningful citation with a real reference.

### AI-tool URL parameters
`utm_source=chatgpt.com`, `utm_source=copilot.com`, `utm_source=openai`, `utm_source=claude.ai`, `utm_source=perplexity.ai`, `referrer=grok.com`. Strip the tracking parameter, keep the link and any functional parameter.

## 11. Conversational residue

### Chatbot artifacts
« Bien sûr ! », « Avec plaisir ! », « Absolument ! », « Certainement ! », « Je serais ravi(e) de… », « J'espère que cela vous aide ! », « N'hésitez pas si vous avez d'autres questions », « Dans cet article, nous allons explorer… », « C'est parti ! ». Remove. **(FR sources)**

### « Plongeons / Explorons ensemble » openers
« Plongeons dans… », « Explorons ensemble… », « Regardons de plus près… », « Parcourons… », « Voyons cela ». A false-collaborative opener delaying the point. Start with the point. Documented as the top French AI tic by Rédacteur.com. **(FR sources)**

### Sycophantic tone
« Excellente question ! », « Vous avez tout à fait raison ! », « C'est un sujet vraiment important. », « Merci pour cette question stimulante. » Remove. **(FR sources)**

### Acknowledgment loops
« Vous me demandez… », « Pour répondre à votre question… », « C'est une question intéressante parce que… ». The reader knows what they asked. Deletion test: cut the opener; if nothing is lost, it was a loop. Carve-out: replies that orient (« Pour votre question de mardi : la facture est partie le 3 »). **(FR sources)**

### Recap-flattery opener
Summarising someone's own work back to them as praise before the point: « Merci pour tout ce travail : le script de migration et le plan de retour arrière que tu as préparés ont rendu cela possible. » Substance first; one plain clause of thanks if any.

### Reasoning chain artifacts
« Procédons étape par étape », « Décomposons cela », « Laissez-moi réfléchir », « Dans l'ordre : », « Commençons par examiner ». Scaffolding leaking into prose. Conclusion first, then evidence. **(FR sources)**

### Narrated candor
Announcing a disclosure instead of making it: « Je préfère être transparent : », « Pour être tout à fait honnête, », « En toute transparence, », « Plutôt que de le passer sous silence, je le dis clairement : ». Deletion test: « Deux réserves que je préfère signaler plutôt que de vous les laisser découvrir : X et Y » says the same as « Deux réserves : X et Y ». Carve-outs: the substantive admission itself (« je n'ai pas testé sous Windows »), and conflict-of-interest disclosure (« Par souci de transparence, je précise que je détiens des parts dans cette société »), which carries a material fact. Judgment only.

### Wall-of-text replies
In conversational registers (comments, chat, DMs, quick emails), a reply under about 150 words with four or more sentences and no line break. Break at thought boundaries. Carve-out: a dense paragraph is correct in formal long-form prose.

## 12. Performed engagement

### Infomercial engagement hooks
« Le hic ? », « Le meilleur dans tout ça ? », « Le résultat ? », « Le twist ? », « Mais ce n'est pas tout. », « Et c'est là que ça devient intéressant. ». Fake suspense around ordinary information. Delete the hook and state the thing: « Le hic ? Ça ne marche que le week-end. » → « Ça ne marche que le week-end. » Same move in fake-candid register: « Franchement ? », « Soyons honnêtes : », « Parlons vrai : », « Bon, » as standalone openers staging a pause. Mid-sentence « franchement » in casual prose is ordinary French.

### Launch-copy dramatic introductions
« Voici Flowdesk. », « Découvrez Flowdesk, votre nouvel allié trésorerie », « Dites bonjour à Flowdesk », « Flowdesk, c'est Notion qui rencontre Figma ». Say what it does and for whom: « Flowdesk affiche toute la trésorerie d'un fonds sur un écran. » Oral dislocation (« Flowdesk, c'est un tableau de bord de trésorerie ») is ordinary French; only the mash-up and the game-show introduction are the tell.

### Fake-casual register
The costume models wear when asked for a relaxed social voice: one-word verdict closers (« Dingue. », « Fou. », « Incroyable. »), stage directions (« *soupir* », « *chef's kiss* », « *lâche le micro* »), wink asides (« (oui, vraiment) », « (non, sérieusement) »), label openers (« Spoiler : », « Petit rappel : », « Avis impopulaire : », « Fun fact : », « Astuce : »), the self-QA volley (« C'est rapide ? Oui. C'est cher ? Pas du tout. »). The drama is outsourced to the prop. Delete the label, say the thing. Carve-out: a writer whose established voice runs on these keeps them.

### Social endorsement closers
« À lire absolument : », « Un must-read. », « Gardez ça sous le coude. », « Enregistrez ce post. », « Vous me remercierez plus tard. », « Ne passez pas à côté. ». A recommendation with no reason. Say what it is and who it's for, or let the link stand alone.

### Lingering-attention claims
« La phrase qui me trotte dans la tête », « Je n'arrête pas d'y penser », « Ça fait une semaine que j'y repense ». A claim about the writer's attention before the reader has a reason to care. Carve-out: the reason is given (« J'y reviens parce que ce cadre prédit qui démissionne »). Otherwise open on the thing.

### Stock reaction framing
« Ce qui m'a le plus frappé », « J'ai été fasciné de découvrir », « Le plus intéressant, c'est », section labels like « Point intéressant : ». Style heuristic, not an authorship signal. Keep authentic specific reactions; fix only the empty frame (« Je m'attendais à X ; la baisse de 40 % m'a surpris parce que Y »). **(FR sources)**

### Confidence calibration phrases
« Il est intéressant de noter », « Fait intéressant, », « Étonnamment, », « Chose importante, », « Sans aucun doute », « Assurément », « Indéniablement ». One in 2,000 words is fine; three in 500 is stacking. Related **persuasive-authority tropes**: « La vraie question, c'est », « Au fond, », « Ne nous y trompons pas », « La vérité, c'est que ». Cut and lead with substance. **Consequence-free explanation**: « C'est important parce que c'est essentiel. » flags; « C'est important parce que la relance facture le client deux fois » passes. Never invent stakes.

### Self-labeling significance
Pointing back at an item to label it: « C'est ce dernier point qui change tout. », « Et c'est là que c'est malin. », « Le troisième point, c'est le vrai sujet. ». The label does the content's job. Cut it, or put the item first and expand it.

### Dramatized contrast against the crowd
« …en 2022, pendant que tout le monde débattait encore », « en un week-end, pendant que le secteur écrivait des tribunes ». An invented lagging crowd. State the fact, or name the competitor and what they did. Carve-out: literal simultaneity in narration.

### Performed-insight phrases
« Prenez un instant pour y réfléchir », « Ce n'est pas rien », « Vous connaissez déjà la réponse », « La chute, c'est que », « Ne me croyez pas sur parole », « Tout est là », « C'est tout l'enjeu », « C'est la partie dont personne ne parle », « Le seul indicateur qui compte », « X est mort, vive X ». Each stages a reveal without adding a fact. One can be a choice; several is a tell. State the claim.

### Dev-blog boilerplate
« tout-en-un », « ça marche, tout simplement », « zéro configuration », « clé en main », « prêt à l'emploi » (as slogan). Name the behaviour: « s'installe sans fichier de configuration ».

### Speculative scenario openers
« Imaginez un monde où… », « Et si… ? » opening an argument, « Projetez-vous dans un futur où… ». The scenario persuades instead of evidence. State the claim. Carve-outs: fiction, a thought experiment with a stated payoff, and teaching (« imaginez un tableau trié »). **(FR sources)** for « Et si… ? ».

## 13. Rhythm devices

### Rhetorical question openers
« Mais qu'est-ce que cela signifie pour les développeurs ? », « Pourquoi est-ce important ? », « Et maintenant ? ». If you know the answer, say it. **(FR sources)**

### Stacked rhetorical questions
« Est-ce que je sais comment ça marche ? Où ça casse ? Quels raccourcis ont été pris ? ». Keep at most one, answer it, turn the rest into statements. Interviews, FAQs and dialogue stack questions legitimately.

### Same-opener sentence runs
« Peut-être que personne n'en avait besoin. Peut-être que ça résolvait le mauvais problème. Peut-être que le moment était mal choisi. », and the repeated skeleton (« Un panier est un objet du système. Un salon de discussion est un objet du système. »). Keep the first, vary or merge the rest. Pronoun runs in narration are ordinary.

### Stranded auxiliary contrast
« L'outil a lâché, les données non. », « La lecture passait. L'écriture, non. ». Fine once; as a recurring rhythm it poses as insight. Ration it and write the next contrast out in full.

### Colon into a triple
A colon opening onto exactly three items: « des ports, des processus et un état local distincts ». Audit the list: two things, or four, or the one that matters. Noisy in technical writing where three is often true; weigh by genre.

### Manufactured punchlines and staccato drama
Clipped same-shape fragments engineered as closers: « Aucune préférence pour la symétrie. Aucun a priori esthétique. Aucune nostalgie du goût humain. Les anciennes règles avaient disparu. ». Keep the one fragment that earns its emphasis, fold the rest into sentences. Variation is the human signal; three matched fragments is its opposite.

- **Repeated empty concessions**: « Pas toujours. Pas parfaitement. » repeated across a passage without saying where the claim fails. P2. Preserve meaningful pairs (« Pas pendant une bascule. Pas pour un jeton expiré. »). Never invent a failure case.
- **Repeated setup/reversal punchlines** (P2, judgment only): « Nous avions prévu tous les scénarios de panne. Sauf celui qui est arrivé. La migration s'est déroulée sans accroc, et c'est comme ça qu'on a su que quelque chose clochait. ». Flag two or more reversals standing in for a missing explanation. Fix: « Nous avons raté un scénario de panne. » and ask for the failure; never invent it. One supported reversal, comedy, fiction and quotations pass.

### False concession structure
« Si X présente des limites, il reste remarquable », « Bien que X ait progressé, Y demeure un défi ». Balanced-sounding, both halves vague. Name the trade-off or pick a side. **(FR sources)**

### Invented contrast-pair mirroring
One half is a real term of art, the other an invented mirror for balance: « une fausse précision plutôt qu'une exactitude authentique ». If you need a contrast, use a real opposite; otherwise state the positive claim.

### False ranges
« du Big Bang à la matière noire », « de la recherche fondamentale à la mise sur le marché ». List the real topics or pick one. **(FR sources)**

### Parenthetical hedging
« (et, de plus en plus, Z) », « (ou, plus précisément, Y) », « (et peut-être surtout W) ». Give the aside its own sentence or cut it. **(FR sources)**

## 14. Lists and structure

### Bullet lists of bare noun phrases
Five or more short verbless items of the same shape: « Efficacité stable / Connectivité fiable / Performances optimisées / Faible taux d'échec / Stabilité thermique constante ». Symmetry and nothing checkable. Convert to prose or full claims (« Moins de 1 % d'échecs sur un test de 12 heures »). Carve-out: changelogs, to-do lists, parameter docs, ingredient lists.

### Inline-header lists
« **Performance :** la performance s'est améliorée… ». Strip the repeating header or use paragraphs.

### List-label periods
« **Présentations.** Des années de conférences. ». A human writes « **Présentations :** des années de conférences », with French spacing before the colon. Fix the period to a colon and lowercase the gloss. Carve-out: when the label is a full sentence.

### Numbered list inflation
« 7 raisons pour lesquelles… », « Les 5 choses à savoir ». Only when the content has that many parallel items. **(FR sources)**

### Excessive structure
More than three headings under 300 words, eight-plus bullets under 200 words, stock headers (« Introduction », « Aperçu », « Points clés », « En bref », « Conclusion »), and fragmented headers (« ## Performance » followed by « La vitesse compte. »). Merge sections, use specific headings, cut warm-ups. **(FR sources)**

### Copula avoidance
« s'impose comme », « se positionne comme », « fait office de », « se veut », « constitue », « représente », « s'inscrit dans », « se traduit par », « s'articule autour de », « bénéficie de », « dispose de », « affiche ». Press-release verbs replacing « est » and « a ». Default to « est » or « a » unless the verb adds meaning. **(FR sources)**

### Subjectless fragments and agentless passives
« Aucun fichier de configuration nécessaire. », « Les résultats sont conservés automatiquement. », « La prise en charge des requêtes imbriquées a été ajoutée. ». Name the actor when it clarifies. French caution: the passive is native in formal French, so flag it in flowing prose only when it hides who decided or combines with other tells. Carve-outs: READMEs, changelogs, parameter docs, commit subjects.

### False agency
« La décision a émergé à l'issue du séminaire. ». P2, judgment: flag only when a specific person or team chose and naming them matters. Name the actor only when the source does; otherwise ask. Conventional personification (« les données montrent ») passes.

### Synonym cycling
« développeurs… ingénieurs… praticiens… concepteurs » in one paragraph. Repeat the right word. **(FR sources)**

### Diff-anchored writing
Documentation narrating a change: « Cette fonction a été ajoutée pour remplacer l'ancienne approche qui parcourait tous les éléments. ». Describe the thing as it is and why. Carve-out: changelogs, release notes, migration guides, decision records.

### Hashtag stuffing
A trailing block of generic tags (#Innovation #Leadership #Transformation #Avenir #Performance). Soft tell at 5+ on `linkedin` and `communique`, hard flag at 6+ anywhere, P0 on those two profiles. Generic category tags weigh more than a project tag. Not tags: issue references (#88), hex colours, `#include`, URL fragments, anything in code. Fix: two or three specific tags, or none. **(FR sources)**

### Generic conclusions
« L'avenir s'annonce prometteur. », « Seul le temps nous le dira. », « Une nouvelle ère s'ouvre. », « Une chose est sûre : », « Des temps passionnants nous attendent. ». P0. A specific closing thought, or none. **(FR sources)**

## 15. Whole-text signals

### Rhythm and uniformity
Structure is the strongest detection signal, stronger than vocabulary: fixing every Tier 1 word and leaving a metronomic rhythm still reads as machine text.

- **Sentence length**: most sentences between 15 and 25 words sounds robotic. Mix 3 to 8 words with 20-plus.
- **Paragraph length**: every paragraph three to five sentences and the same weight. Vary it; some paragraphs are one sentence. The « lettre de motivation » skeleton (three equal paragraphs, each a complete argument) is the French short-email form of this. **(FR sources)**
- **Repetition versus cycling**: repeat when the word is right, vary when it's natural.
- **Read-aloud test**: prose a text-to-speech engine could read without sounding odd is probably too uniform. For French, ask whether you could say the sentence out loud to someone met two minutes ago.
- **Missing perspective**: where the genre carries a voice, total neutrality is itself a tell. The fix belongs to the author; see "What a rewrite may add" in SKILL.md.
- **Over-polishing**: sanding every irregularity pushes human text toward machine statistics. Keep natural unevenness. A deliberate typo is not humanity, it's sloppiness; irregular rhythm is. **(FR sources)**

### Vocabulary diversity
In pieces over about 200 words, a flat vocabulary (the same few abstract nouns recycled) is worth a look. The type-token thresholds published for English (roughly 0.50 to 0.65 human, under 0.40 suspect) are not calibrated for French, whose inflection raises the ratio; use it by eye only. The fix is broadening the *what*: name specific things, cite cases, replace a recycled abstraction with its concrete instance.

### Paragraph-reshuffle test
Can two body paragraphs swap without breaking the piece? Then it's a list of points, not an argument. Build a through-line, or make it an explicit list.

### Treadmill effect
For each paragraph, ask what is new. Prose that restates the premise in fresh words can lose 40 to 60% with no information lost. Name each paragraph's one contribution, lead with it, cut the throat-clearing.

### When to rewrite from scratch
Five or more Tier 1 hits, three or more distinct pattern categories, and uniform sentence and paragraph length: patching won't fix it, the structure itself is generated. Recommend a full rewrite, say why patching is not enough, and rebuild from the core point stated in one sentence. **(FR sources)**
