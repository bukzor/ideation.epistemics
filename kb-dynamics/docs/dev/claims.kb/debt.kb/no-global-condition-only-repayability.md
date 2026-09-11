---
label: SERVICE_RATE
standing: user
authority: f65fbdf3#L606 and #L815 entail it; f65fbdf3#L995 confirmed the entailment
why:
  - debt-is-wanted-unrepayable-debt-is-not.md
  - owner-review-is-a-queue-sorted-by-debt.md
  - ../imported-terms.kb/weekly-cost.md
---

# No global condition on debt: the queue runs when the owner chooses, and the only invariant is repayability

Health is not a level of debt and not a rate of servicing it. The queue
is run when the owner chooses, and the one invariant is that every item
stays repayable (`UNREPAYABLE`). This follows from two rulings already on
file: a hard-coded target is a broken design (`PAYOUT_TEST`), and debt
is wanted (`WANTED_DEBT`).

Declined: a rate condition, weight-bearing debt cleared per sitting at
least matching accrual, which presumes a review cadence the owner
declined to fix; and a bound on the weight-bearing part, which is the
singular target in another form.
