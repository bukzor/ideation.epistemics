You are building the ultimate-tic-tac-toe (STTT) plugin for the FP2
representation-synthesis system (which runs on the ACS claim ledger). Your
deliverable is a plugin package, not a standalone program: signature, Lean
semantics + proofs, rewrite rules with certificates, Class-R rules with
discharge routes, benchmarks. Open your ledger first; log everything below
with proper statuses.

DOMAIN & GOAL
STTT: 9 local 3×3 boards forming a meta-board; a move in cell c of a local
board sends the opponent to local board c (unless won/full → free choice).
Goal: synthesize efficient GPU/CPU representations of game states WITH their
operation set, optimized for (a) identifying and iterating symmetric orbits,
(b) traversing the state graph (BFS/retrograde/solver workloads).

SIGNATURE Σ (minimum; extend as needed, log extensions as stipulations)
apply-move, legal-moves, local-win/meta-win predicates, successor-set,
the 8 symmetry generators, canonical-form, orbit-iterate.

KEY FACTS TO FORMALIZE (verify, don't inherit — derive bounds yourself)
- The state fits in a small fixed number of machine words: derive the exact
  bit budget (81 cells × 2 bits + forced-board + local-board win/full status;
  note some fields are derivable — decide what's stored vs recomputed and log
  the decision). Faithful fixed-width codes trivially exist; the search space
  is WHICH packing. This is the layout stratum working at full strength.
- Symmetry group: D₄ (order 8) acting simultaneously on the arrangement of
  local boards and within each local board. Equivariance ⟦g·s⟧ = ĝ(⟦s⟧) is an
  ordinary Class-E homomorphism law over Σ — no special machinery. Proofs are
  finite case analysis; expect `decide`-grade. ĝ must be cheap in-encoding:
  bit-permutation networks / PEXT-PDEP / GPU shuffles — make cheapness a
  constraint the cost model prices, not an assumption.
- Exact canonicalization = min over the 8 images. Cheap and exact — unlike
  most domains, the quotient here is trivial; exploit that.

CLASS-R RULE (the semantic-relaxation stratum)
Frontier dedup via symmetry-INVARIANT hash instead of canonicalize-then-hash:
cheaper, non-injective. Obligation schema: collision behavior discharged by
enumeration over the reachable state space (or a bounded region) — a finite,
mechanical audit. This mirrors the fingerprint pattern in Knot-Search; the
recurrence is expected and is evidence the abstraction is right.

TRAVERSAL (exercises FP2's collection combinators — you are the first
serious client; report gaps upstream rather than working around them)
Successor generation, frontier compaction, dedup-by-key against a visited
set, layered BFS, reachability as least fixpoint. Lean semantics: lfp of the
successor relation.

BENCHMARKS (empirical engine; memory-bound regime)
GPU hash tables, atomics, frontier compaction, warp-level orbit iteration.
Fit the cost model to measurements; log coefficients as data claims.

EXITS
1. Hand-built: one packed representation, proven equivariant ops, one
   discharged collision audit, measured traversal throughput vs a naive
   baseline.
2. FP2 search rediscovers or beats the hand packing from constraints alone.
3. Retraction drill: revoke the hash rule's audit; verify the system retreats
   to exact canonicalization and downstream claims downgrade correctly.
