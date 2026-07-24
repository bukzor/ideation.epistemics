---
last-updated: "2026-07-24"
---

# The Ladder — rungs of the {TL, RN} basis

`Skill(llm-claim-ledger)` is the conversational realization of the
{TL, RN} basis that ACS/FP2 mechanize (see
`sources.kb/knot-theory-chat.md`). The chat's own reduction: "'LC: we
Label our Claims' is TL; 'strive to ensure all claims are sound or
else retracted' is RN, verbatim — your prompt was already the minimal
basis." The skill states the axioms; ACS/FP2 are their derived
machinery at the mechanized rung (`prompts/`).

| chat weight (the skill) | mechanized (ACS/FP2) |
|---|---|
| LC — label claims | TL, total ledger: nothing enters unlabeled |
| sound/open/retracted; last wins; retraction propagates | RN, refinement norm: the set is revised under attack |
| ledger as conversation spine | SI, spine inversion: the claim store *is* the system |
| `XY <- AB CD` premise lists | dependency edges; RP, mechanical retraction propagation |
| bare / `?` / `stipulated` / `!` | asserted / described-or-open / declared axiom / certified(checker) |
| `claim certify` — name and run an executable check | discharge engines: Lean proof, e-graph, benchmark |
| `claim accept` — operator fiat | promotion-to-axiom, TL's third status |
| flush — obligation manifests addressed to fresh contexts | Dedukti-port transport; certificate asymmetry |
| warrant-mix at point of use, eyeballed | ATMS-style label propagation, computed |

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
stored — see `claims.kb/obligation-is-derived-not-stored.md`. Executors
of `prompts/` inherit this revision, per RN: last wins.
