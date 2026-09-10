---
label: PAYOUT_TEST
standing: agent
why:
  - ../debt.kb/owner-review-is-a-queue-sorted-by-debt.md
---

# Paid out means one target ledger can be opened, queued, reviewed in a session, and trusted

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
