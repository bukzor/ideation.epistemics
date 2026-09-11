---
label: PAYOUT_TEST
standing: user
verdict: rejected
authority: f65fbdf3#L606, the owner's ruling of 2026-09-11
why:
  - ../debt.kb/owner-review-is-a-queue-sorted-by-debt.md
---

# Paid out means one target ledger can be opened, queued, reviewed in a session, and trusted

Rejected: a singular target hard-codes what the design must not.

> [!@bukzor] f65fbdf3#L606
> i don't see any need to decide this now. or ever, really. Why would "the target" be a singular? A system that hard-codes the target is a broken design.

The criterion, restated for every ledger, is asked again as
`TRUST_TEST`; the two guards below are re-posed there.

Pick one durable ledger the owner has lost confidence in and make it the
target for the whole line. The work has paid out when the owner can
open it, run the queue, spend one session, and trust it. Not when the
framework is elegant, not when a rules collection is complete. If three
components are built and that ledger is still not trusted, the recursion
has the work, and the test says so.

Two guards:

- every artifact is usable alone, and each next one is justified by what
  the previous revealed, never by the design;
- the tooling runs on itself: this ledger is a claims ledger, and debt
  runs on it. A system unusable for its own maintenance is unusable.

The budget that matters is not build time, which agents spend, but the
owner's attention for design and validation.
