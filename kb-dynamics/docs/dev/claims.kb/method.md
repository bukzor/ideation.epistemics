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
  - port
stale-when: a third built component with no ledger the owner trusts more than before it
---

# method -- the order the work is built in, and when it has paid out

The sandbox comes before the substrate, because the owner expects to
find flaws and redo the design repeatedly and the sandbox is where a
redo is cheap. The harness's core is the implementation, kept pure and
total so the on-disk backing and a later Lean port are each a
translation. The line has paid out when a ledger the owner distrusted
is trusted again by any of `TRUST_TEST`'s conditions -- no ledger is
singled out -- not when the framework is elegant.
