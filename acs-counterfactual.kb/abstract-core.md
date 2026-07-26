---
last-updated: "2026-07-26"
---

# ACS abstract core

Part 1 of the plan in `../acs-counterfactual.md`: the
representation-independent core — what every port (chat, kb, agda)
must realize. Produced by re-cutting the fifteen clean-room mechanisms
(`./derivation.md` §1) against the full kernel spec
(`../prompts/acs.md`). Each contains things the other lacks; this
document is the join. Parts 2–3 build on it.

## The core, stated

1. **Claim = payload + standing.** The payload language is a port
   parameter (Dedukti terms in ACS.agda, prose in ACS.chat, files in
   ACS.kb); the core requires only that payloads are held as objects,
   so anything can enter at `described`.

2. **Four-point status lattice.** `described ⊑ stipulated ⊑ obligated
   ⊑ certified(checker)`. The order tracks verification commitment,
   not resolvedness. `certified` is parameterized by a named,
   re-runnable checker (mech 1.3); `stipulated` must carry an
   attributable source (1.1).

3. **Warranted membership.** The accepted set is everything at
   `stipulated` or above; a non-described entry without a warrant is
   not in the store, it is un-ingested input (1.1). Mechanized as the
   intake check (1.15a).

4. **Dependency edges on every non-described claim**, including edges
   to the stipulations and tie-break decisions it rests on (1.5,
   1.11). Open kernel issue: `described` items carry no edges, yet
   most real mass enters as described — drift's re-entry door
   (stress finding 1 in `../acs-counterfactual.md`).

5. **Versioned store; last revision wins; prior states queryable.**
   Subsumes the derivation's bare total order (1.8) and strengthens
   it: history is part of the store, which is what makes the liveness
   view (1.15b) a query rather than bookkeeping.

6. **Retraction hits exactly the dependency cone — and the cone is
   definitional.** The invalidated set is computable from edges, so a
   port may materialize per-victim downgrades only under derived-cache
   discipline: regenerable, stamped with input revision, never read
   stale (1.6 joined with the spec's "downgrades exactly its
   dependency cone"). Spec gap found here: the downgrade's **target
   status** is unstated — `certified → obligated` reopens the
   obligation; `→ described` abandons it. The core makes the target a
   recorded transition rule each port fixes and logs as a stipulation.

7. **Two exits for an obligation; two laws.** Discharge ascends the
   lattice only with a real certificate (the spec's soundness law).
   Promotion-to-axiom (1.9) is a **descent** — `obligated →
   stipulated` — legitimate only as a recorded fiat with attributable
   source. The ascent law alone would forbid it, so the kernel needs
   the matching descent law: status descends only by recorded fiat
   (promotion) or by retraction propagation (the cone).

8. **Two strata.** Checkers are monotonic and live where revision
   never rewrites; the ledger revises freely above (1.4). In ACS.agda
   this is the architectural law (store as object-level data, Agda
   proving transitions sound at the meta level); in file ports it is
   two disk regions with different mutation disciplines. Same seam,
   port-specific enforcement.

9. **Attack intake.** Forced by RN + IN, absent from the spec text:
   any session must be able to record a challenge against any entry,
   or revision never fires and the store is a labeled graveyard
   (1.10). Spec amendment candidate.

10. **Degeneracy audit.** Also absent from the spec text: the intake
    check as a certificate, plus a liveness view over revision history
    — attacks and retractions occur, obligations age toward discharge
    (1.15). A store that only grows fails IN even if every entry is
    warranted.

11. **Self-application, with the residue logged.** The ledger is the
    system: the operating instructions a session boots from are
    entries under warrant (1.14 ≡ the spec's "open a ledger about your
    own build"). One base stipulation sits at the root,
    `stipulated(operator)` — the Gödel residue, logged rather than
    hidden (1.12).

12. **Query layer owed by every port:** `trust-base-of(claim)` (the
    transitive stipulations and checkers under it),
    `rests-on-stipulations`, the obligation list (a view, never a
    maintained sibling list — 1.7), the invalidation cone, and
    liveness.

13. **Domain freedom, measured.** Core membership is earned by porting
    survival, not asserted (1.13); the ports table in
    `../acs-counterfactual.md` is the measurement apparatus.

## The port parameter vector

The derivation's eight choice points (§2) plus the spec's
parameterization points are exactly what a port must assign:

payload language · checker set · entry granularity · ordering
primitive · edge representation · relevance/retrieval · check re-run
policy · retraction authority · attack representation · downgrade
target · core/plugin cut

A port = the core + one assignment of this vector, with each
assignment logged as a stipulation in the port's own ledger (1.11).
ACS.kb's assignment is part 2's content.

## Mechanism ↔ spec join

| mech | spec element | disposition |
|---|---|---|
| 1.1 warranted entry | lattice; stipulated-with-source | kept; `described` sits below the warrant line |
| 1.2 checks as re-runnable files | `certified(checker)` | kept; the *file* form is a fleet-port constraint, not core |
| 1.3 verdict stored with checker name | checker parameterization | identical |
| 1.4 two strata | architectural law | identical seam; enforcement is port-specific |
| 1.5 dependency edges | edges on non-described claims | kept; `described` gap open |
| 1.6 invalidation as query | retraction propagation | joined: cone definitional, materialization under cache discipline; downgrade target = spec gap |
| 1.7 obligation view | query layer: obligation list | identical; DV adds never-read-stale |
| 1.8 total order | versioned store, last-wins | subsumed and strengthened (prior states queryable) |
| 1.9 promotion-to-axiom | — | added; the descent law |
| 1.10 attack intake | — | added; spec amendment candidate |
| 1.11 stipulation records | edges include stipulations, tie-breaks | kept |
| 1.12 base stipulation | implicit in self-ledger | kept explicit |
| 1.13 core/plugin partition | "claim-centric and domain-free" | kept; porting survival is the measure |
| 1.14 boot from the ledger | "revise under your own ledger" | identical (SI) |
| 1.15 degeneracy audit | — | added |

What the spec had that the reduced-basis derivation lacked:
`described`; payload deep-embedding (port-specific); `trust-base-of`
as a named query; prior-states queryability.

## Open kernel questions (carried to part 3)

- Edges for `described` items, or procedures as claim bundles
  (stress 1).
- Multi-store scoping; prior art `../inquiry-scoped-layout.md`
  (stress 2).
- Loading economics — the view/retrieval layer the kernel never names
  (stress 3).
- Downgrade target status on retraction (found in this re-cut, §6).
