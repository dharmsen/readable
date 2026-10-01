# Style reference

Simplified Technical English (ASD-STE100) was written so that maintenance manuals could be read by non-native speakers under time pressure. The same pressure applies to a person reading a plan at the end of a long day. This file applies the STE writing rules to technical prose. It does not enforce the STE dictionary.

## Contents

1. Sentence rules
2. Word choice
3. Paragraph and section rules
4. Definitions
5. Calibrating claims
6. Before and after pairs

## 1. Sentence rules

- **One instruction or one idea per sentence.** If a sentence has two verbs joined by "and", check whether it is two ideas.
- **Length**: 12 to 25 words, one new idea per sentence. Twenty-five is the hard ceiling. Short is not the goal; even is. If cutting words would stack two facts into one clause, keep the words and split the facts instead. More than two numbers in one sentence is a stack; give the third number its own sentence.
- **Active voice.** The actor comes first. Passive is allowed when the actor is unknown or irrelevant: "The file is read once."
- **Present tense** for how things work. Past tense for what happened. Future only for what will happen at a stated time.
- **Keep subject and verb close.** Do not put a clause between them. If a long clause must interrupt, move it before the sentence or after the main clause instead.
- **Old before new.** Start a sentence from something the reader already has; put the new material at the end. Each sentence hands the next one its topic. A sentence that opens with three new things forces the reader to hold them all before any of them pay off.
- **Split on these words**: and, but, which, while, whereas, so that, in order to, semicolon, em-dash. Each is usually a sentence boundary in disguise.
- **Put the condition first** in a conditional: "If the queue is full, the producer blocks." The reader learns when the rule applies before learning the rule.
- **Negatives**: prefer one negative per sentence. "Do not skip validation" is fine. "It is not uncommon for validation to not run" is not.

## 2. Word choice

- **One term per concept.** If the source says "job", "task", and "work item" for the same thing, pick one and use it everywhere. Mention the alternates once, in the definition, if the reader will meet them elsewhere.
- **Concrete verbs.** "Drops", "retries", "allocates", "blocks". Avoid "handles", "deals with", "manages", "involves" when a specific verb exists.
- **Cut filler**: it is worth noting, in order to, essentially, basically, actually, very, quite, fairly, a number of, in terms of, at the end of the day, going forward, leverage (as a verb), utilize.
- **Cut empty hedges**: "somewhat", "arguably", "to some extent". Replace with a calibrated word from section 5, or delete.
- **Numbers as digits.** "3 retries", not "three retries". Units always attached: "40 ms", "2 GB".
- **Avoid nominalizations.** "Perform validation of" is "validate". "Make a decision" is "decide".
- **Pronouns need a clear referent.** If "it" or "this" could point at two things, repeat the noun.

## 3. Paragraph and section rules

- A paragraph makes one point. First sentence states the point. The rest supports it.
- The first sentence of a section picks up where the previous section ended, then states what this one answers. Do not open a section cold. This is the storyline the reader follows.
- Four sentences is the comfortable ceiling. Five is the hard one.
- Headings state the conclusion or the concrete topic. Compare "Caching" to "Caching cuts p50 by half but not p99".
- Use lists when items are parallel and independent. Use a numbered list when order matters. Use a table when the reader will compare items across two or more attributes.
- Do not bullet an argument. If step 2 depends on step 1's reasoning, that is prose.
- Bold at most a few words per paragraph. Bold is for defined terms and for the first words of a bullet. It is not emphasis.

## 4. Definitions

Define a term the first time it appears, in bold, in one sentence, in the running text. Do not put definitions in a glossary the reader has to jump to unless there are more than about ten.

Pattern: **Term** is a [category] that [distinguishing property].

- **A write-ahead log** is a file that records each change before the change is applied.
- **Idempotent** means that running an operation twice gives the same result as running it once.

Define only what the reader may not know. Do not define "function" for a programmer. Do define project-specific names, acronyms, and any term the source uses in a narrower sense than usual.

If a definition pushes its sentence past the length limit, do not fold the definition into a rule. Define the term in its own sentence first, then state the rule in the next sentence.

## 5. Calibrating claims

Every non-trivial claim carries a signal of how much to trust it. Use a consistent vocabulary:

| Word | Means |
|---|---|
| measured, observed | Someone ran it and saw this |
| documented | A source says this. Name the source if the original did |
| expected | Follows from a known mechanism, not yet tested |
| likely, probably | Best guess with reasons given |
| guess, speculation | Best guess without strong reasons |
| unknown | Nobody checked |

Mark speculation inline, not in a footnote: "The cache is likely the cause (speculation; not profiled)." A reader who acts on a guess as if it were a measurement will be hurt by the document.

## 6. Before and after pairs

**Before**
> Given the fact that the migration touches both the users table and the sessions table, and considering that these are accessed by basically every request, we'll want to be careful to ensure that the migration is done in a way that doesn't lock either table for any significant period, which could be achieved via an online schema change tool.

**After**
> The migration changes the users and sessions tables. Every request reads both. A long lock on either table would stall the service. Use an online schema change tool so that the migration does not hold a lock.

**Before**
> Performance was found to be somewhat degraded under load.

**After**
> Under load, p99 latency rose from 80 ms to 210 ms (measured, staging, 500 rps).

If the source does not contain the numbers, do not invent them. Write: "Under load, latency rose (the source gives no numbers)."

**Before**
> The system leverages a novel approach to handle failures.

**After**
> When a node fails, the coordinator reassigns its shards to the two nearest healthy nodes.

If the source does not say what the approach is, keep the vagueness and mark it: "The source does not describe the failure handling."
