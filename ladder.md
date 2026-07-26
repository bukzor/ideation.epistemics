---
last-updated: "2026-07-26"
---

# The Ladder — rungs of the {TL, RN} basis

`Skill(llm-claim-ledger)` is the conversational realization of the
{TL, RN} basis that ACS/FP2 mechanize (see
`./sources.kb/knot-theory-chat.md`). The chat's own reduction: "'LC: we
Label our Claims' is TL; 'strive to ensure all claims are sound or
else retracted' is RN, verbatim — your prompt was already the minimal
basis." The skill states the axioms; ACS/FP2 are their derived
machinery at the mechanized rung (`prompts/`).

Between them sits **repo weight** (`./definitions.kb/repo-weight.md`):
claims as files in a `.kb/` tree, on `Skill(llm-discourse-graph)`.
Distinguished by medium and by persistence — it is where sessions
accumulate, and so the rung the operator's productivity actually rests
on (`mission.md`).

| chat weight (the skill) | repo weight (the `.kb/` graphs) | mechanized (ACS/FP2) |
|---|---|---|
| LC — label claims | one node per claim, addressable by path | TL, total ledger: nothing enters unlabeled |
| sound/open/retracted; last wins; retraction propagates | `status:` field; supersession by edit | RN, refinement norm: the set is revised under attack |
| ledger as conversation spine | the `.kb/` tree *is* the knowledge | SI, spine inversion: the claim store *is* the system |
| `XY <- AB CD` premise lists | `premises:`/`conclusion:` — typed, polarized, resolved but never walked for support; `depends:` leaks around them | dependency edges; RP, mechanical retraction propagation |
| bare / `?` / `stipulated` / `!` | `asserted` / `contested` / `retracted`, plus `likelihood` | asserted / described-or-open / declared axiom / certified(checker) |
| `claim certify` — name and run an executable check | — no certificate status | discharge engines: Lean proof, e-graph, benchmark |
| `claim accept` — operator fiat | — no fiat status | promotion-to-axiom, TL's third status |
| flush — obligation manifests addressed to fresh contexts | `claim flush` lands nodes here; todo checkboxes carry the rest | Dedukti-port transport; certificate asymmetry |
| warrant-mix at point of use, eyeballed | — no propagation, no view | ATMS-style label propagation, computed |

The dashes are the finding: the middle rung is the least built, and it
is the one that runs every day (`./claims.kb/repo-weight-rung-is-unbuilt.md`).
The realm reached the hardest rung before the nearest one.

`claim certify` and `claim accept` are exactly RN's two resolution
routes for open debt: "open obligations are actively driven toward
discharge or promotion-to-axiom."

The monotonic/dynamic seam (the chat's MT) holds at every rung:
checkers are monotonic and live below the ledger (Lean, tests, fetches;
Dedukti at the certified port), while the ledger above is dynamic
(last wins). The twin degenerate modes (IN) are failure modes at every
rung too: RN-without-TL is sycophancy; TL-without-RN is a perfectly
labeled graveyard.

Revision flowing up-ladder (2026-07-24): obligation is derived, not
stored — see `./claims.kb/obligation-is-derived-not-stored.md`. Executors
of `prompts/` inherit this revision, per RN: last wins.

**The middle column is the incumbent, and it now has a proposal against
it** (`./repo-weight-derivation.md`, held against the incumbent in
`./preservation-audit.md`). Under it the dashes fill: no status field
at all, warrant by field presence, `certified:`/`stipulated:` for the
two cells that were missing. And RP turns out to be nearly free —
retraction is a rename, so `llm.kb-validate-links` surfaces every
dependent (`./claims.kb/link-checker-is-the-propagator.md`). That is
the row most worth re-reading: the middle rung looked like the one
needing the most machinery, and it needed a naming convention.

The three columns are *ports* of one representation-independent ACS
core (`./claims.kb/acs-rungs-are-ports-of-one-core.md`): ACS.chat,
ACS.kb, ACS.agda. What survives every port is the kernel, and porting
survival is the kernel's validation metric. Worked through in
`./acs-counterfactual.md`.
