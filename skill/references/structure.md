# Structure reference

The output's sections depend on what the source is. Classify first, then use the matching template. Merge templates for mixed documents. Drop a section only when the source has nothing for it, and do not write "Not applicable" placeholders.

## Contents

1. Classifying the source
2. Shared opening and closing
3. Template: explanation
4. Template: plan
5. Template: spec
6. Three-layer mechanism explanations
7. Tables and progressions
8. Appendix rules

## 1. Classifying the source

| Type | Signs | Reader's question |
|---|---|---|
| Explanation | "how", "why", mechanisms, trade-offs, comparisons | How does this work and why? |
| Plan | steps, phases, order, owners, "first / then", risks | What will happen and in what order? |
| Spec | requirements, interfaces, inputs and outputs, "must", constraints | What exactly is being built? |
| Mixed | a plan with a design rationale, a spec with a background section | Both |

A Claude Code plan-mode output is usually plan plus a short explanation. A design doc is usually spec plus explanation.

## 2. Shared opening and closing

Every output starts the same way, regardless of type:

1. **Frame** (one to three sentences): the larger setting. What system, what goal, who cares.
2. **Problem** (one to three sentences): the specific gap or question inside that frame.
3. **Scope** (one to three lines): what this document covers and what it leaves out. Bullets are fine here.
4. **Core idea** (a table or a short progression): the whole document compressed. See section 7.

Every output ends the same way:

- **Open problems**: what is unknown, undecided, or untested. Bullets. If the source names none, list the ones the rewrite exposed. If there are truly none, one sentence saying so.
- **Appendix** (optional): tangents moved out of the main text. See section 8.

## 3. Template: explanation

```
# [Title that states the conclusion]

[Frame → problem → scope]

## The idea in one table
[Table or progression]

## [Mechanism 1: heading states what it does]
### Intuition
### Formal
### Operational

## [Mechanism 2 ...]

## Trade-offs
[Table: option, gain, cost, when to pick]

## Open problems
```

Use the three-layer split (section 6) for each mechanism the source explains. Two or three mechanisms is typical. If the source has one mechanism, drop the numbered mechanism headings and use the three layers as top-level sections.

## 4. Template: plan

```
# [Title: what the plan delivers]

[Frame → problem → scope]

## Plan at a glance
[Table: step, what changes, why, risk]

## Step 1: [what the step achieves]
[Operational layer: files, commands, checks. Intuition layer only if the step is non-obvious.]

## Step 2: ...

## Risks and mitigations
[Table]

## Open problems
```

Plans rarely need the formal layer. They do need, for each step, the concrete artifact it produces and how to know it worked. Keep file paths and commands verbatim from the source.

## 5. Template: spec

```
# [Title: the thing being specified]

[Frame → problem → scope]

## Overview
[Table: component, responsibility, interface]
[Optional Mermaid diagram of components and data flow]

## Requirements
[Numbered list. One requirement per line. "Must", "should", "may" used consistently.]

## Interfaces
[Per interface: inputs, outputs, errors. Tables or code blocks verbatim.]

## Behavior
[Three-layer explanation for each non-trivial rule]

## Constraints and non-goals

## Open problems
```

## 6. Three-layer mechanism explanations

A mechanism is anything with a "why" behind it: an algorithm, a protocol, a design choice, an invariant. Explain each in three layers, in this order, because a reader who has the intuition can skim the formal part and a reader who has both can jump to the operational part.

**Intuition.** One or two sentences of the picture, then a concrete example small enough to trace by hand. Textbooks do this: "Suppose three clients each send one request per second..." If a figure is worth having, it goes here.

**Formal.** The precise rule. An equation, an invariant, a state machine, a definition with all its conditions. Short. This is the part the reader will quote later.

**Operational.** What to do with it. The command to run, the config to set, the check that confirms it holds, the failure mode to watch for.

Example, for a rate limiter:

> ### Intuition
> A token bucket is a jar that fills at a fixed rate. Each request takes one token. When the jar is empty, requests wait. If the jar holds 10 tokens and fills at 2 per second, a burst of 10 goes through at once, then the rate settles at 2 per second.
>
> ### Formal
> Bucket capacity B, fill rate r tokens per second. A request at time t is admitted if tokens(t) ≥ 1, where tokens(t) = min(B, tokens(t_prev) + r·(t − t_prev)). Long-run throughput is at most r. Maximum burst is B.
>
> ### Operational
> Set B to the largest burst the downstream can absorb, and r to its sustained capacity. Check: under a constant load above r, the admitted rate should flatten at r. If it does not, the clock source is wrong.

## 7. Tables and progressions

The "core idea" section compresses the document into one artifact the reader can hold in mind. Two shapes work:

**Table**, when the content is a set of things with shared attributes. Options vs criteria, steps vs outcomes, components vs responsibilities.

**Progression**, when the content is a sequence of states or a chain of reasoning. Write it as a numbered list of short lines, each a state or a step, or as a Mermaid flowchart if there are branches.

Example progression for a caching change:

1. Every request hits the database.
2. Add a read-through cache in front of it.
3. Reads that hit the cache skip the database.
4. Writes invalidate the cache key.
5. Stale reads can happen between a write and its invalidation. This is the open problem.

## 8. Appendix rules

A tangent is content that does not change what the reader will do or believe about the main topic. Examples: history of how the design was chosen, an alternative that was rejected early, a side note about tooling.

In preserve mode, move tangents to an appendix headed by what they are about. Reference the appendix from the main text in one line: "The rejected alternatives are in Appendix A." Nothing is deleted.

In compress mode, tangents may be dropped. List what was dropped in the chat message, not in the document.
