---
stipulated: ../sources.kb/bukzor.md
sources: [../sources.kb/bukzor.md]
depends:
  - ../definitions.kb/repo-weight.md
date-observed: 2026-07-24
tags: [repo-weight, strategy, method]
---

The incumbent design at repo weight — `Skill(llm-discourse-graph)` as
it ships — is admissible as prior art and as evidence of past intent.
It is not admissible as canon. Operator fiat, 2026-07-24, made against
the gap analysis in `./repo-weight-rung-is-unbuilt.md`.

**The retired frame.** This was first posed as patch vs. rewrite. That
dichotomy is malformed: both branches take the incumbent as the
baseline and differ only in edit distance from it, which smuggles in
the authority the question was meant to test. The design question is
what {TL, RN} implies a claim store must represent. Edit distance is an
output of that answer, not an input to it.

**What the incumbent is good for.** Two things. As prior art it holds
design moves worth taking on their merits — the operator values more
than a few of them. As evidence it records intent and policy: which
problems were felt worth solving, in what order. Both are real
evidence. Neither is authority, and intent in particular is defeasible
— a policy can be wrong, and an old policy can be wrong about a
situation that has since changed.

**What is inadmissible.** Incumbency itself, and adoption statistics.
How often a feature is used today is caused in part by how good the
design is, so reading usage as a signal of what to build is circular —
rarity cannot distinguish "not needed" from "too much friction to
record." A survey of how much {TL, RN} is live across existing graphs
(run 2026-07-24) was discarded on those grounds.

**The obligation this creates.** Discarding canon does not discharge
the incumbent's virtues; it converts them into debt. The new design
owes a side-by-side: for each aspect of the incumbent worth keeping, a
verdict of **improves**, **preserves**, or **obviates**, argued.
"Obviates" is a legitimate verdict — an aspect can stop being needed
once the axioms are applied — but it must be stated and defended.
Silence is not a verdict, and an aspect lost without one is a
regression, not a simplification.
