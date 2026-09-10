---
label: MONOTONE
standing: agent
why:
  - debt-is-a-vector-and-leaves-are-not-in-it.md
  - ../imported-terms.kb/permit.md
  - ../imported-terms.kb/oblige.md
---

# No agent move raises debt silently

Every agent move is non-increasing in debt, or it increases debt and is
obliged to carry a flag that lands in the owner's queue. Moves that
strictly lower debt are permitted without asking. That is the entire
dynamics claim: a quantity that moves cannot raise silently and the
owner can lower. If the name helps, debt is a Lyapunov function of the
state.

> [!@bukzor] chat.md#L261
> This is where my proposal of modelling state transitions really comes from. What are the minimal rules, behaviors we need to instill to ensure the kb trends toward a good state? And what even is a "good state"? Later, how do we "trend toward" the good state at maximum speed?

On speed: once debt is visible and monotone, rate is a choice rather
than a problem. What was wrong before was not how fast ledgers drifted
but that drift was invisible and unbounded.
