You are building ACS (Agda Claim System): a verified claim-ledger kernel in
Agda. The central object is a claim store, not a proof. This kernel will later
host a refinement methodology and representation-synthesis engines; design for
generality, not any one domain.

CORE MODEL
- Claim: a proposition-like payload plus metadata. Payloads are terms of a deep
  embedding of the λΠ-calculus modulo rewriting (Dedukti's calculus) defined in
  Agda: syntax, typing relation, and a checker. Rationale: Dedukti terms are a
  universal, minimal claim-content language; foreign provers' certificates
  (Lean, Coq, HOL) become homogeneous imports.
- Status lattice per claim, per revision:
  described (held as object, no commitment)
  ⊑ stipulated (declared true by fiat; judgment/axiom — always queryable)
  ⊑ obligated (asserted with a named, pending discharge obligation)
  ⊑ certified(checker) — parameterized by which kernel checked it
  (dedukti-embedded, agda-native, external+export). Trust base per claim must
  be a graph query.
- Dependency edges: every non-described claim records what it rests on,
  including stipulations and tie-break decisions.
- Revisions: the store is versioned. Retraction of any claim invalidates
  (downgrades) exactly its dependency cone — "retraction propagation."
  Last revision wins. Prior states remain queryable.

ARCHITECTURAL LAW (load-bearing — do not violate)
Type theory is monotonic; revision is not. Therefore: the store, statuses,
edges, and transitions are OBJECT-LEVEL DATA (indexed families over revision
states; transitions are ordinary functions). Agda's typechecker operates at the
META level only: prove the transition rules sound (discharge only ascends the
lattice with a real certificate; retraction hits exactly the dependency cone;
last-wins holds). Never encode "claim = Agda type, revision = ???" — Agda
cannot un-inhabit a type, and you would silently lose all revision dynamics.

PRIOR ART & OBLIGATIONS (open a ledger about your own build immediately; log
these as obligated claims, statuses per above)
- Truth-maintenance systems (Doyle TMS, de Kleer ATMS) are 1980s implementations
  of this store. Reuse their propagation algorithms. Obligation: ATMS labels
  can blow up exponentially in assumption sets — evaluate full ATMS labels vs
  single-context TMS + checkpointing at ~10^6-node scale before committing.
- Obligation: survey existing verified λΠ-modulo checkers before writing one.
- Obligation: verify current Dedukti/Lambdapi ecosystem status, especially
  Lean 4 export coverage and anything univalence-adjacent (cubical transport
  likely cannot route through λΠ; that's why certified() is checker-
  parameterized).
- Uses of cubical Agda: transport of programs/proofs along equivalences between
  representations is a first-class intended operation — keep the kernel
  compatible with cubical mode.

DELIVERABLES, PHASED (expect your first pass to be wrong; revise under your
own ledger)
1. λΠ-modulo deep embedding + checker; store datatypes; status lattice.
2. Transition system + meta-level soundness proofs.
3. Retraction drill as acceptance test: retract a base claim, verify exact
   downstream invalidation and incremental re-discharge.
4. Query layer: trust-base-of(claim), rests-on-stipulation(s), obligation list.
Applications downstream: a methodology layer (FP2) and PL-design work will run
on this kernel. Keep the API claim-centric and domain-free.
