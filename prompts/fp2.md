You are building FP2: a refinement methodology and generic representation-
synthesis engine, implemented as a client of the ACS claim-ledger kernel
(assume its API: claims with statuses described/stipulated/obligated/
certified(checker), dependency edges, versioned retraction propagation).

AXIOMS (the entire method reduces to these two; everything else is derived)
- TL: nothing enters the accepted set without explicit status + dependencies.
- RN: the set is revised under attack — refuted claims retract (propagating),
  open obligations are driven to discharge or explicit promotion-to-stipulation,
  last wins.
Degenerate failure modes to guard against: RN-without-TL = unaudited belief
drift (sycophancy); TL-without-RN = permanently hedged graveyard. Gödel
residue: the system cannot certify its own adoption; exactly one stipulated
claim ("we work this way") sits at the base forever — log it, don't hide it.

PURPOSE: synthesize efficient data representations WITH their operation sets
for a domain, from constraints, minimizing and auditing human judgment rather
than pretending to eliminate it. A "representation" is a triple
(datatype D, operations, interpretation ⟦·⟧) where ⟦·⟧ is a homomorphism for
the domain signature Σ.

ARCHITECTURE — the ledger is the spine; three discharge engines surround it:
1. PROOF engine (external prover; Lean4+Mathlib recommended for domain math;
   certificates imported via ACS's Dedukti-term payloads). Sovereign over
   correctness: semantics of Σ, homomorphism laws, per-rewrite soundness.
2. SEARCH engine (e-graph, egg/egglog-style) over representation terms.
   Two rule classes:
   - Class E (equivalences): ⟦lhs⟧=⟦rhs⟧, proof-certified before admission.
   - Class R (relaxations): ⟦rhs⟧ refines ⟦lhs⟧ with an explicit error budget
     ("sound if collision-audited on finite table T", "exact for size ≤ n",
     "correct w.p. ≥ 1−ε"). Directed, non-invertible; each application emits
     an obligation into the ledger, discharged outside the search.
   Nothing off-the-shelf does Class R with certificates — this is the research
   component. Extraction operates over (term, obligation-set) pairs.
3. EMPIRICAL engine (benchmarks on target hardware). Sovereign over cost:
   cost models are FITTED to measurements, enter the ledger as data claims,
   never as proof premises. Detect-and-refine loop: expect wrongness, measure,
   refit, let retraction propagation un-certify affected extractions.

DESIGN LAWS (each killed a failure mode; keep the one-line reasons)
- Value hierarchy: layout rewrites buy 2–10×; algorithmic rewrites buy
  polynomials; Class-R semantic relaxations buy exponentials. An equivalence-
  only system is structurally blind to the biggest wins.
- Price the whole triple: cost(encode)+cost(decode)+cost(ops). Otherwise
  extraction converges on beautiful algebra with uncomputable codecs.
- Faithfulness is a budget, not a boolean.
- Core/plugin split: core = combinator language (including collection
  combinators map/filter/dedup/reduce and a fixpoint for graph traversal),
  Class-E layout rules, search, cost-fitting, certificate formats. Plugin =
  Σ, semantics, domain Class-E laws, domain Class-R rules + discharge routes,
  finite structures. Generality is earned by porting plugins, measured by how
  much core survives.
- All arbitrary decisions (tie-breaks, cost-model choices, Σ itself) are
  stipulated-status ledger nodes — queryable, retractable.

PHASING WITH FALSIFIABLE EXITS
1. Ledger integration + Class-E engine. Exit: retraction drill through a
   rewrite chain.
2. One plugin end-to-end BY HAND including one discharged Class-R obligation.
3. Mechanized search must REDISCOVER the hand solution — including choosing
   the Class-R semantic win because priced obligations favor it; then revoke
   the enabling rule and verify retreat to best fully-certified alternative.
4. Second plugin, count core reuse.
First plugins arrive as separate specs (STTT-Search, Knot-Search).
