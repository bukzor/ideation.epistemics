---
label: TRUST_TEST
standing: user
authority: f65fbdf3#L815
why:
  - paid-out-means-one-target-ledger-is-trusted-again.md
  - ../debt.kb/owner-review-is-a-queue-sorted-by-debt.md
---

# Any of three conditions restores trust in a ledger, and the harness is to stress their corners

For any ledger, each of these is sufficient:

- its queue is empty: no load-bearing claim rests on a proposed basis
- its queue fits one sitting
- its skeleton is right: the owner has read every `user` claim, and
  everything else is derivable and disposable

> [!@bukzor] f65fbdf3#L815
> All three seem sufficient, from here. I'd like to see the kb-dynamics exploration to stress the corner cases of this question.

The fleet-wide report is the progress instrument, re-run at will; there
is no target ledger (`PAYOUT_TEST` is rejected on that point). Two
guards carried over: every artifact is usable alone and justified by
what the previous revealed, and the tooling runs on this ledger too.
