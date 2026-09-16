---
label: METHOD
standing: agent
why:
  - ../what-the-harness-shows/HARNESS.md
  - ../weighing-a-candidate-rule/RULE_PRICING.md
  - ../what-no-move-may-raise/DEBT.md
ontology:
  - substrate
  - payout
  - port
stale-when: a third built component with no ledger whose queue is shorter than before it
---

# method -- the order the work is built in, and when it has paid out

The sandbox comes before the substrate, because the owner expects to
find flaws and redo the design repeatedly and the sandbox is where a
redo is cheap. The harness's core is the implementation, kept pure and
total so the on-disk backing and a later Lean port are each a
translation. The line has paid out when a ledger the owner had stopped
reviewing meets any of `REVIEW_DONE`'s conditions -- its review done or
doable, no ledger singled out -- not when the framework is elegant.
