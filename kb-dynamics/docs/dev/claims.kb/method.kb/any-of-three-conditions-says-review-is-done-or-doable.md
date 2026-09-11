---
label: TRUST_TEST
standing: user
authority: f65fbdf3#L815 on the three conditions; 9b6f24ad on what they are conditions of
why:
  - paid-out-means-one-target-ledger-is-trusted-again.md
  - ../debt.kb/owner-review-is-a-queue-sorted-by-debt.md
  - ../model.kb/effective-basis-is-computed-from-grounds-not-stored.md
---

# Any of three conditions says the owner's review of a ledger is done or doable, and the harness is to stress their corners

For any ledger, each of these is sufficient:

- its queue is empty
- its queue fits one sitting
- its skeleton is right: the owner has read every `user` claim, and
  everything else is derivable and disposable

> [!@bukzor] f65fbdf3#L815
> All three seem sufficient, from here. I'd like to see the kb-dynamics exploration to stress the corner cases of this question.

Each condition is an aggregation over the queue: a fact about what the
owner has left to rule on. None is trust. A claim is trusted by its own
fold (`EFFECTIVE_BASIS`), a ledger carries no trust of its own, and a
non-empty queue says nothing about any particular claim:

> [!@bukzor] 9b6f24ad
> a non-empty queue has no (direct) bearing on the state of any particular claim.

The earlier title, "restores trust in a ledger", was the agent's framing
of the question and is withdrawn on that ruling; the first condition's
gloss, "no load-bearing claim rests on a proposed basis", named one rot
kind where the queue counts every kind (`COMPONENTS`) and goes with it.
What an empty queue and per-claim trust entail about each other is
`EMPTY_QUEUE_TRUST`. "Fits one sitting" is a field quantity the sandbox
does not compute.

The fleet-wide report is the progress instrument, re-run at will; there
is no target ledger (`PAYOUT_TEST` is rejected on that point). Two
guards carried over: every artifact is usable alone and justified by
what the previous revealed, and the tooling runs on this ledger too.
