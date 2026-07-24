---
sources: [../sources.kb/claude.md]
depends:
  - ../definitions.kb/total-ledger.md
  - ../definitions.kb/repo-weight.md
date-observed: 2026-07-24
tags: [repo-weight, notation, proposal]
---

At repo weight, TL is represented by **field presence, not a status
enum**. Absence of any warrant field is the open-obligation cell — the
cheap default. `stipulated:` names the declaring source and is the
declared-axiom cell. `certified:` names a re-runnable check and is the
checked-certificate cell. Retraction is not a field at all — it is a
rename, per `./retraction-breaks-the-path.md`, because the path is what
the tooling tests.

Consequence: `status:` disappears from claims and deductions, and
`contested` with it. A contested claim is one with a live contradiction
deduction aimed at it — computed from the graph, with the attack itself
on the record, instead of declared in a field that can drift from it.

Proposed, not settled — asserted in this realm's own sense: warranted
only so far as it stays consistent with the admitted set. The full
derivation, its costs, and the two points awaiting fiat are in
`../repo-weight-derivation.md`; the side-by-side against the incumbent
is `../preservation-audit.md`.
