---
label: MINUTIAE
standing: agent
why:
  - review-cost-scales-with-the-ledger-not-the-payoff.md
  - ../imported-terms.kb/obligation.md
---

# Most open questions are leaves: nothing rests on them, so they carry no obligation

The minutiae that exhausted the owner's review are open questions and
proposed claims with no descendants. Under obligation-as-derived
(`IMPORTED_OBLIGATION`) such a node is obligated to nothing, and
resolving it changes nothing downstream. They are findable without
reading: a reverse-dependency query with an empty answer.

This is the measurement behind `REVIEW_RATIO`: the owner had already
observed that the review's payoff was small, and the graph can say which
items were the small part. The same observation motivates a terminal
state for questions that will never matter (`CLOSED_QUESTION` in
`../model.md`).
