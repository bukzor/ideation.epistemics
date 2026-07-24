You are building the knot-theory plugin for the FP2 representation-synthesis
system (running on the ACS claim ledger). Deliverable: a plugin package —
signature, Lean4/Mathlib formalizations, certified rewrite rules, Class-R
rules with discharge routes, GPU benchmarks. Open your ledger first.

MOTIVATING WORKLOAD (operationalize; do not treat as vibes)
Brittenham–Hermiller 2025 (arXiv:2506.24088) proved unknotting number
non-additive: u(7₁#7̄₁) ≤ 5 < 6. Their pipeline: generate millions of braid
variants (crossing changes = sign flips in braid words — already GPU-shaped),
then IDENTIFY each resulting knot against a table of prime knots ≤15 crossings
via SnapPy's hyperbolic-geometry identification — sequential, requires prior
diagram simplification, and is the bottleneck. Target: replace identification;
success metric ≥ millions of braids fingerprinted per commodity-GPU-hour,
end-to-end, measured.

STRUCTURAL FACTS (formalize in Lean; import certificates into ACS)
- Objects: knot DIAGRAMS (PD/Gauss/DT codes, braid words) with proven
  interconversions. Knots = diagrams modulo Reidemeister (braids modulo
  Markov). Represent diagrams; prove move-soundness; NEVER attempt knot-level
  canonicalization — it subsumes knot equivalence (tower-of-exponentials).
- Gauss-code realizability is a nontrivial validity predicate — a real slice.
- Schubert: knots under # form a free commutative monoid, no inverses,
  infinitely many primes. Obstruction corollaries to formalize: no faithful
  group-valued code; no finite-width faithful code for unbounded knots
  (bounded fragments escape). These prune the search space at zero compute.

CLASS-R CORE (the exponential win — invariant fingerprinting)
Exact identify : Diagram → TableEntry, relaxed to a battery of algebraic
invariants computed as matrix products directly on UNSIMPLIFIED braid words:
- Burau representation → Alexander data at sampled points over finite fields:
  batched small-GEMM, ideal GPU shape.
- R-matrix / Jones evaluations at several q: sparse structured products on
  2^strands-dim space; feasibility depends on strand count — price it.
Lean obligations: each invariant is a braid-group homomorphism AND
Markov-invariant (hence a knot invariant). This is the certified half.
Budget obligation: the fingerprint is non-injective (mutants share most
invariants). Discharge by FINITE COLLISION AUDIT: precompute fingerprints over
the entire target table, enumerate collision classes once, route only
colliding hits to exact CPU resolution (SnapPy). Faithfulness is a measured
budget, never assumed. Key win to preserve: invariants need no simplification
step — a 119-crossing 14-strand braid fingerprints directly.

DESIGN LAWS INHERITED (one-line reasons; do not re-learn them)
- Price encode/decode/ops together: the prime-factorization encoding makes
  concatenation = multiplication and is useless — all cost hides in the codec.
- Lawrence–Krammer (faithful, entries grow) vs finite-field specializations
  (fixed-width, collisions) span the faithfulness/cost spectrum; the search
  walks it under budgets.

BENCHMARKS: batched-GEMM throughput, fingerprint pipeline end-to-end vs
SnapPy baseline on the paper's own verification braids (their Section 5 code
is the correctness oracle — run it).

EXITS
1. Hand-built: one certified invariant homomorphism + one discharged collision
   audit on a real knot table + measured throughput vs SnapPy.
2. FP2 search rediscovers fingerprinting over exact identification because
   priced obligations favor it.
3. Retraction drill: enlarge the table, invalidate the old audit, verify the
   dependency cone downgrades and re-discharges incrementally.
