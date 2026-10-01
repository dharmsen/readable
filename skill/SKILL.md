---
name: readable
description: Rewrite a markdown file or the last response into simple, textbook-style prose. Invoked only via /readable [path] [--compress].
disable-model-invocation: true
---

# Readable

Turn dense prose into text a tired reader can follow on the first pass. The reader is the user: technical, but reading fast and without the context Claude had when it wrote the original.

## Invocation

`$ARGUMENTS` is one of:

| Form | Mode | Output |
|---|---|---|
| `/readable path/to/doc.md` | file mode | `path/to/doc.readable.md` next to the source. Never overwrite the source. |
| `/readable` | last-response mode | Print the rewrite in chat. End with one line offering to save it to a file. |
| either form + `--compress` | compress mode | Same outputs, but redundancy and low-value detail are cut. |

If the sibling file already exists, overwrite it. It is the skill's own output, not the user's.

Default is **preserve** mode: every fact, decision, number, caveat, and open question in the source survives in the rewrite. Move tangents to an appendix instead of deleting them. In **compress** mode, merge repeated points, drop detail that changes no decision, and drop tangents. Still keep every decision, number, and caveat. After writing, tell the user in chat what you cut: one short line per cut.

## Process

Work in this order. Each step feeds the next, and skipping the inventory is how facts get lost.

1. **Read the whole source.** In last-response mode, the source is your previous prose message. Code blocks, commands, and file paths are content, not prose. Keep them verbatim.
2. **Classify the document.** Plan, spec, explanation, or mixed. The type decides which sections the output gets. See `references/structure.md`.
3. **Build an inventory.** List every fact, decision, number, caveat, open question, and term of art in the source. In preserve mode this is a checklist: the final text must cover each item. Keep the inventory in your head or the scratchpad, not in the output.
4. **Pick the figures.** Usually zero to three. A figure earns its place only if it shows a relationship, flow, or shape of data that a sentence would state badly. Read `references/figures.md` before drawing anything.
5. **Write the rewrite** using the structure for the document type and the style rules below.
6. **Self-check** against the checklist at the end of this file. Fix what fails, then deliver.

## Style rules

These follow ASD-STE100 Simplified Technical English in spirit: the writing rules, not the restricted dictionary. Full detail and before/after pairs are in `references/style.md`. The core:

- **One new idea per sentence.** Split at "and", "which", "while", and semicolons. Short is not the goal; even is. A 25-word sentence that flows beats a 14-word sentence carrying three facts. Keep at most one new concept and two numbers per sentence.
- **Active voice, present tense** unless the meaning needs otherwise. "The scheduler drops the job" beats "the job is dropped".
- **One name per thing.** Pick a term at first use and reuse it. Synonyms read as new concepts.
- **Define terms at first use, in bold, in one sentence — only terms the reader may not know.** Example: **Backpressure** is the signal a consumer sends when it cannot keep up. Do not define vocabulary the audience already shares.
- **Short paragraphs.** Four sentences is a good ceiling. A paragraph holds one point.
- **Lists for parallel items, tables for comparisons, prose for argument.** Do not force an argument into bullets.
- **Concrete before abstract.** Lead a mechanism with a small worked example, then generalize.
- **Calibrate claims.** Say "measured", "expected", "likely", or "guess" so the reader knows how much to trust each line. Mark speculation as speculation.
- **No filler.** Cut "it is worth noting", "in order to", "essentially", and hedges that carry no information.
- **Headings say what the section concludes,** not what it is about. "Retries double tail latency" beats "Retry analysis".

## Content shape

Every output opens with the frame and narrows to the problem, states the question the document answers in one line, then the scope in one or two lines. The middle depends on the document type. Each section opens by picking up where the previous section left off, so the reader always knows where they are in the storyline. The end lists open problems. `references/structure.md` gives the section template per type and shows how to explain a mechanism in three layers:

1. **Intuition**: the one-sentence picture and a concrete example.
2. **Formal**: the precise statement, rule, or equation.
3. **Operational**: what to do, run, or check.

Use all three layers sparingly, and only for the one or two mechanisms the document's conclusion depends on. A plan step usually needs only the operational layer. If the source asserts a mechanism without explaining it, keep the assertion. Do not add derivations or textbook background the source never gave.

## Figures

Two tools, chosen by what the figure shows:

| Figure shows | Use |
|---|---|
| Structure, flow, sequence, states, dependencies | Mermaid block inline in the markdown |
| Quantities, trends, distributions, comparisons of numbers | `scripts/plot.py` template, saved as PNG in `assets/<doc-name>/` next to the output |

Every figure gets a caption that states the takeaway, not the contents. "Figure 2: p99 latency doubles once queue depth passes 40" is a caption. "Figure 2: latency vs queue depth" is a label. Details, Mermaid conventions, and the plotting workflow are in `references/figures.md`.

Skip a figure when the data is made up, when the rendering target is unknown, or when the figure would restate a table. If the same numbers appear in a table in the output, keep one of the two: the table when it has roughly six rows or fewer, the figure when it shows a shape or overlay the table cannot. Never deliver both for the same data. Three good figures beat eight decorative ones.

## Self-check before delivering

Read the draft as the user would, then confirm:

- [ ] Every inventory item appears (preserve mode) or was cut on purpose and reported (compress mode).
- [ ] Code, commands, paths, and numbers are verbatim from the source.
- [ ] No sentence over about 25 words. No paragraph over about five sentences. This includes sentences carrying a bold definition: define the term in its own sentence instead.
- [ ] No sentence carries more than one new concept or more than two numbers.
- [ ] The opening states, in one line, the question the document answers. Each section's first sentence links to the previous section.
- [ ] Every term of art is bold-defined at first use, and only once.
- [ ] Every heading states a conclusion or a concrete topic.
- [ ] Every figure has a takeaway caption and is referenced in the text.
- [ ] Claims carry their confidence. Speculation is marked.
- [ ] Scope is stated near the top. Open problems close the document.
- [ ] Nothing was added that the source did not say, except definitions and examples that illustrate what the source said.

## Example

Source sentence:

> It's worth noting that in order to handle the case where the upstream service is unavailable, which we've seen happen fairly often in staging, the client will essentially retry with exponential backoff, and this is important because otherwise we'd hammer the service.

Rewrite:

> **Exponential backoff** is a retry policy that doubles the wait after each failure. The client uses it when the upstream service is down. This happens often in staging (observed). Without backoff, retries would flood the service while it recovers.

Four sentences, one idea each, the term defined once, the claim's basis marked.
