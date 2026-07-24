# `depends:` may not run claim → claim

**Applied, partially.** The rule is written into
`claims.jsonschema.yaml`'s description and this realm's two offending
edges are gone. Enforcement is not built: a JSON schema cannot see
across files, so the check belongs in the warrant audit and is listed
as check #1 in `../../../repo-weight-derivation.md`.

**Why.** ADR-006 states deductions are the sole mechanism connecting
claims. The shipped schema then offers `depends:`, documented as
context "without implying support or refutation" — and it gets written
claim→claim as genuine support anyway. An invariant contradicted by the
schema that hosts it. The cost is not stylistic: a walker following
only the deduction spine misses real support, and one following
`depends:` too propagates retraction through mere context. Both
behaviours are wrong and there is no third option while the leak
exists.

**Scope, narrower than it first looked.** Of 9 `depends:`→claim edges
surveyed, only 4 were claim→claim. The other 5 run question→claim,
which is legitimate context and stays legal. The rule is specifically
claim→claim.

**Cost, paid here.** A support edge now costs a file. One edge in
`../../../claims.kb/incumbent-design-is-evidence-not-canon.md` was
demoted to a prose reference rather than promoted to a deduction,
because it records operator fiat rather than an inference.

**What to check.** That demotion — prose is unwalkable, so if the edge
was real support it should be a deduction and I took the cheap way. And
whether question→claim `depends:` really is context in your usage, or
whether questions cite claims as support too.
