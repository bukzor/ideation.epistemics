---
label: CANDIDATE_RULES
standing: agent
why:
  - no-agent-move-raises-debt-silently.md
  - ../imported-terms.kb/rule.md
  - ../imported-terms.kb/permit.md
  - ../imported-terms.kb/oblige.md
---

# The candidate rule set, split by where each rule lives

Mechanical, in the validator over the state: references resolve; the
grounds are acyclic; every non-`user` claim has a ground or is
`proposed`; effective basis and debt are computed; exact duplicates and
graph-suspicious near-duplicates are flagged.

Judgment, at the move that creates the risk:

1. Before adding, search. If a near-match exists, ground on it or amend
   it; do not add.
2. One basis per claim. A claim that cannot be given one is split.
3. Ground it or mark it `proposed`. A blank basis is never admitted --
   this is what the add move is obliged to carry.
4. An agent may lower debt without asking: merge exact duplicates, split
   non-atomic claims, close leaf questions, propose rewording of drafts.

Rule 4 is what makes the ledger trend rather than merely not worsen;
without it agents only ever add. This set is a candidate: which rules
have any effect the harness shows (`FIVE_PROPERTIES` in
`../harness.md`), and which earn their cost is priced in
`../rule-pricing.md`.
