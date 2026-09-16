---
label: OBJECTIVE
standing: user
authority:
  address: dfc18e9d
  words: My initial guess is that, in general we seek benefit _and then_ minimize cost/benefit.
  about: the incoherence between rules the harness can never motivate and WANTED_DEBT
why:
  - debt-is-wanted-unrepayable-debt-is-not.md
  - ../problem.kb/review-cost-scales-with-the-ledger-not-the-payoff.md
---

# The system seeks benefit, and then minimizes cost per benefit

Two goals, ordered. First the ledger seeks benefit: claims admitted,
work allowed to proceed before a ruling, which is why debt is wanted
(`WANTED_DEBT`). Then, among the ways of getting that benefit, it
minimizes cost per unit of benefit. The two conflict, with a highly
sensitive exchange rate between them (`EXCHANGE_RATE` in
`../rule-pricing.md`), and the order is the owner's initial guess, not
a closure.

> [!@bukzor] dfc18e9d
> 1. the system seeks low cost/benefit
>    - in this framing, WANTED_DEBT could be seen as "the system seeks benefit"
>    - the two goals conflict, with a highly sensitive exchange rate. My initial guess is that, in general we seek benefit _and then_ minimize cost/benefit.

This is what a rule may ground on when no harness property demands it.
The properties check the first goal only: debt stays repayable, so
benefit is never lost. A rule that prevents visible, repayable debt
serves the second goal, cost, which the sandbox does not model; its
ground is this claim and its price is the field's
(`ATTRIBUTION`, `REPLAY`). `SURFACE_BEFORE_GROUNDING` and the
search-before-adding rule of `CANDIDATE_RULES` are the first two.
