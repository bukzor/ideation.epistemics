---
label: METHOD
standing: agent
why:
  - harness.md
  - rule-pricing.md
  - debt.md
ontology:
  - substrate
  - payout
  - target ledger
  - port
stale-when: a third built component with the target ledger still untrusted
---

# method -- the order the work is built in, and when it has paid out

The sandbox comes before the substrate, because the owner expects to
find flaws and redo the design repeatedly and the sandbox is where a
redo is cheap. The harness's core is the implementation, kept pure and
total so the on-disk backing and a later Lean port are each a
translation. The line has paid out when one chosen ledger is trusted
again, not when the framework is elegant.
