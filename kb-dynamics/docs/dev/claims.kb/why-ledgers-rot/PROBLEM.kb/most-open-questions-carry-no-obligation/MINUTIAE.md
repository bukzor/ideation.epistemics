---
label: MINUTIAE
standing: bare
verify: kb-dynamics/docs/dev/claims.kb/why-ledgers-rot/PROBLEM.kb/most-open-questions-carry-no-obligation/MINUTIAE.verify.py
why:
  - ../review-cost-scales-with-the-ledger-not-the-payoff/REVIEW_RATIO.md
  - ../../../words-from-outside/IMPORTED_TERMS.kb/obligation/IMPORTED_OBLIGATION.md
---

# Most open questions are leaves: nothing rests on them, so they carry no obligation

The minutiae that exhausted the owner's review are open questions and
proposed claims with no descendants. Under obligation-as-derived
(`IMPORTED_OBLIGATION`) such a node is obligated to nothing, and
resolving it changes nothing downstream. They are findable without
reading: a reverse-dependency query with an empty answer. Measured
2026-09-11 over the fleet's ledgers: fifty-seven of seventy-five open
questions had no dependents; the verify script re-runs the count.

This is the measurement behind `REVIEW_RATIO`: the owner had already
observed that the review's payoff was small, and the graph can say which
items were the small part. The same observation motivates a terminal
state for questions that will never matter (`CLOSED_QUESTION` in
`../../../states-and-moves/MODEL.md`).
