---
sources: [../sources.kb/claim-ledger-notation-session.md]
depends: [../definitions.kb/acs.md, ../claims.kb/two-base-statuses-not-four.md]
tags: [acs, notation, inconsistency]
---

`definitions.kb/acs.md` lists ACS's statuses as
`described/stipulated/certified` (no `asserted`, no `retracted`); the
settled chat-weight design (`Skill(llm-claim-ledger)` SKILL.md) has
four — `asserted` (the common, unmarked case), `stipulated`,
`certified(CHECK)`, `retracted` — with `described` being unlabeled
prose, not a status at all. Is ACS's set deliberately narrower (a real
design choice not yet written down), or is `acs.md` stale relative to
`two-base-statuses-not-four.md`? Settles by operator decision, then a
one-line `acs.md` correction either way.

Candidate answer (2026-07-24, awaiting fiat): stale, and stale in both
directions. Applying the two settled claims uniformly — obligation is
derived, statuses collapse to two base ones — gives stored
`{asserted, stipulated, retracted}` with `{certified, obligated}` as
derived views. `acs.md` diverges by promoting `described` (unlabeled
prose) to a status *and* by storing `certified`, which
`two-base-statuses-not-four.md` says is read off a premise chain or a
named check at point of use. That is the same stored-vs-derived error
the obligation refactor already corrected once.

Same answer as `how-should-repo-weight-absorb-tl-rn.md` reaches for the
rung below; deciding either should decide both.
