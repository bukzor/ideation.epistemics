---
label: NO_SILENT_RAISE
standing: bare
why:
  - debt-is-wanted-unrepayable-debt-is-not.md
  - what-voids-repayment.md
  - components.md
  - ../imported-terms.kb/permit.md
  - ../imported-terms.kb/oblige.md
---

# No agent move raises debt without a pathway to repay it

An agent move may raise debt. What it may not do is raise debt that
nothing will ever surface: every raise lands in the review queue with
what a later reader needs to rule on it, so the debt stays repayable
(`WANTED_DEBT`, `UNREPAYABLE`). Debt reductions are permitted under agent authority,
under the guards of `UNASKED_MOVES`.

The earlier form of this claim, "every agent move is non-increasing in
debt or carries a flag", read monotonicity into the owner's question and
is withdrawn on their word:

> [!@bukzor] chat.md#L261
> What are the minimal rules, behaviors we need to instill to ensure the kb trends toward a good state? And what even is a "good state"? Later, how do we "trend toward" the good state at maximum speed?

On speed: once debt is visible and every item of it is queued, rate is a
choice rather than a problem. What was wrong before was not how fast
ledgers drifted but that drift was invisible and unbounded.
