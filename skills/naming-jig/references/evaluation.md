# Evaluation

Evaluation runs in two passes: a fast **kill list** that removes defective candidates, then **scoring** to rank what survives. Do them in that order: scoring a defective name is wasted work and creates attachment to names that must die.

## Pass 1: kill list

Eliminate any candidate that:

1. **Matches an anti-pattern** without a written justification (see `anti-patterns.md`).
2. **Fails the radio test**: say it aloud once to someone who has never seen it; if they can't spell it, every referral, podcast mention, and word-of-mouth moment will leak. (Also called the phone test / bar test.) For a name that must carry a separator (a package, a CLI, a skill folder), the test includes it: heard once, does the listener type `naming-jig`, `namingjig` or `naming_jig`?
3. **Is unpronounceable in a target market**: consonant clusters, ambiguous vowels, sounds that don't exist in the market's language.
4. **Carries a negative or vulgar meaning in a target language.** This check is mandatory, not paranoid; the classics are all real: Mitsubishi renamed the Pajero to *Montero* for Spanish-speaking markets (pajero is vulgar slang); Honda's *Fitta* became the Jazz/Fit after the Nordic launch check (vulgar in Swedish and Norwegian); Rolls-Royce dropped *Silver Mist* for *Silver Shadow* (Mist is manure in German); Vicks trades as *Wick* in Germany (V pronounced F collides with an obscenity). Check every shortlist name in every brief-listed language, plus the big trade languages if the product is global. Method, at minimum: a dictionary that lists slang senses (Wiktionary, Urban Dictionary) per target language for each shortlist name, and a web search when the word is a proper noun or the homophone of one. "I know the word" is not a check.
5. **Sits too close to a competitor or a famous mark**: phonetically or visually, not just letter-for-letter. Closeness reads as either confusion or imitation; both are fatal. The same applies to the reserved words of the environment the name will live in: a developer tool called `fixture`, `slug`, `run` or `loop` collides with the vocabulary of every framework and CLI around it.
6. **Is a category cliché**: the metaphor every competitor already uses (shields in security, rockets in growth tools, brains in AI).
7. **Needs an explanation to be spelled AND to be said.** One tax may be payable; two never are.
8. **Promises a feeling the product cannot deliver in its first minute of use.** Friend (pendant), Rabbit (r1), Humane (Ai Pin): each name set an emotional contract (companionship, a pet, humanity) the product then had to honour on day one, and when it did not, the name became the headline. A name that promises a feeling is only allowed when the product delivers that feeling immediately; otherwise choose a name that promises less.
9. **Its plain reading points at a different function**: a `-guide` that is not a document, a `-press` that does not publish, a `-drill` that produces no exercises. An empty vessel explains nothing; a name that explains the wrong thing is worse.
10. **For domain hacks only: the dot falls inside a word.** If saying the name aloud requires saying "dot" mid-word, it fails the radio test twice (see `generation.md` §8).

Before killing on a language or homonym worry, check `corpus.md` §18: the Chevrolet Nova and Coca-Cola stories are myths, and citing them undermines the real cases above.

## Pass 2: scoring

Score survivors 1-5 on six dimensions. Scoring's job is to rank the ambiguous middle: the best and worst candidates are usually obvious without it.

| Dimension | Question |
|---|---|
| **Distinctiveness** | Does it stand apart from the category's naming landscape? |
| **Fit** | Does it match the brief's positioning and tone adjectives? |
| **Sayability** | Effortless to pronounce, first try, in every target market? |
| **Memorability** | Sticky after one exposure? (Sound frame, imagery, surprise all feed this.) |
| **Stretch** | Does it survive a pivot, a product-line extension, a decade? (Names that encode today's feature, or today's technology, age worst.) |
| **Ownability** | Position on the distinctiveness spectrum (see `name-types.md`) + search uniqueness: can it be found? A name that's also a common word pays a permanent SEO and findability tax (fine for Apple-scale budgets, expensive for everyone else). |

Weight dimensions by the brief: a CLI tool weights sayability and search uniqueness; a luxury brand weights distinctiveness and imagery.

## Supplementary tests

- **The résumé test** (companies and products only): "I work at ___." Does the sentence carry pride, or need a smile of apology?
- **The flexion test** (companies and products only): can it verb, plural, and possessive cleanly? ("We ___ed the files.") Not required, but names that flex become language.
- **The identity test**: can you already see the wordmark and hear the tagline rhythm? Names with a visual handle (metaphor, texture) give the design phase a head start.
- **The neighbor test**: say it in a sentence next to the product category and the sibling product names. Family fit matters when the brief includes a portfolio. In series mode, the siblings are the two fictional "+2" members built on the same grammar (`generation.md` §9): a name that is great alone and awkward with siblings is a failed series candidate.
- **The corpus test**: find the closest real name of the same type in `corpus.md` and ask whether the candidate pays the same tax with the same budget. A tiny tool cannot afford Apple's tax; a company cannot afford a domain hack's.

## The visual room pass (shortlist only)

The name precedes the logo and survives it: it circulates by word of mouth without the designer, while the logo only travels where the company puts it. Typography, colour and symbol house the name; they do not replace it. So before any drawing, ask three questions of each shortlist name, and write the answers into "Watch out" when they bite:

- Does the word hold as a wordmark: length, rhythm of the letterforms, awkward capitals, a double letter that will look like a typo at small sizes?
- Does it open a formal territory of its own, or will it force a symbol to compensate for a soft word?
- Do the sound register and the probable visual register contradict each other (a percussive name that the brief's tone will have set in a light, rounded face)?

Two handoff failures to name when you see them coming: a strong name paired with a logo too expressive to let it speak, and a typeface that contradicts the tone the word implies. A name strong enough to carry a system, not only a logotype, is the goal. This pass produces no logo; it only tells the identity designer where the name leaves room.

For a complementary published lens, Alexandra Watkins' *Hello, My Name Is Awesome* proposes the SMILE/SCRATCH pair of checklists: five qualities a name should have and seven defects that disqualify it. It overlaps heavily with the kill list above; use it as a cross-check vocabulary when the user knows it, not as a replacement.

## Presenting evaluations

- Argue against the **brief**, never from taste. "I like it" is not a rationale; "it's the only candidate that carries the calm-tone requirement into a crowded category of aggressive names" is.
- Be honest about defects in names the user loves. An evaluation that only reassures is a disservice: the defect will surface later, at higher cost.
- Expect and say this: distinctive names polarize on first contact, then normalize fast (iPad and Wii were both mocked at launch; `corpus.md` §17 lists eight more). First-reaction "I'm not sure" is not a kill signal; a spelling failure is.
- **Gut reaction before rationale.** Before the user reads any argument, ask them for a one-word reaction to each shortlist name (yes / maybe / no) and to say each name aloud once. Keep those reactions next to the scores. A name the user says "no" to on sight rarely recovers; a "maybe" usually does.
- **Do not decide in the session.** Recommend that the shortlist be reread the next day, ideally shown to one person from the target market, before anything is registered. First-contact enthusiasm and first-contact rejection both fade; what survives the night is the signal.
- **Give every shortlist name the same amount of text**, the same level of detail and the same tone. A longer rationale reads as a recommendation, a shorter one as a filler; the presentation must not vote before the user does.
