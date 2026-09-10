---
label: CORE_IS_IMPLEMENTATION
standing: agent
why:
  - the-sandbox-comes-before-the-substrate.md
---

# The harness's transition, debt, and rules are the implementation, not a prototype

The only thing swapped when the model meets real data is the state's
backing: in-memory maps for the on-disk ledger. The property suite stays
as the test suite. Meeting real data is a port, not a design.

Declined: a throwaway toy and a separate production implementation. Two
copies of the same table drift, and the properties would certify the
one that is not run.
