---
label: CANDIDATE_RULES
standing: agent
why:
  - ../no-agent-move-raises-debt-silently/NO_SILENT_RAISE.md
  - ../the-system-seeks-benefit-then-minimizes-cost-per-benefit/OBJECTIVE.md
  - ../../../words-from-outside/IMPORTED_TERMS.kb/rule/IMPORTED_RULE.md
  - ../../../words-from-outside/IMPORTED_TERMS.kb/permit/IMPORTED_PERMIT.md
  - ../../../words-from-outside/IMPORTED_TERMS.kb/oblige/IMPORTED_OBLIGE.md
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
4. An agent may reduce debt under agent authority: merge exact duplicates, split
   non-atomic claims, close leaf questions, propose rewording of drafts.

Rule 4 is what makes the ledger trend rather than merely not worsen;
without it agents only ever add. This set is a candidate. Rules 2 and 3 are structural in the model and
rule 4 is a permission; which rules have any effect the harness shows
(`PROPERTY_SET` in `../../../what-the-harness-shows/HARNESS.md`). Rule 1 prevents visible, repayable
debt, so no property demands it: it grounds on `OBJECTIVE`'s cost goal,
and its cost, like every rule's, is priced in `../../../weighing-a-candidate-rule/RULE_PRICING.md`.
