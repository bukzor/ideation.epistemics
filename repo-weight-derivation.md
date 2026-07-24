---
last-updated: "2026-07-24"
---

# Repo weight, derived from {TL, RN}

A proposal, not a decision. Answers
`questions.kb/how-should-repo-weight-absorb-tl-rn.md` by deriving the
schema from the axioms and only then comparing against the incumbent
(`preservation-audit.md`, which carries the verdicts). Two points need
operator fiat and are marked.

## What TL implies

> No item enters the accepted set without an explicit justification
> status ∈ {checked certificate, open obligation, declared axiom}.

Three cells, and `claims.kb/two-base-statuses-not-four.md` already
collapsed them once: `open obligation` is the unmarked default (an
asserted claim is "effectively a question"), while `declared axiom` and
`checked certificate` differ not in standing but in *how* the standing
was obtained — fiat versus a discharged check.

So the stored thing is not a status. It is **the warrant, or its
absence**. And the incumbent already knows how to represent that: its
questions carry no status field, deriving state from field presence
(`resolved` / `candidate-resolutions` / neither). Apply that same move
to claims and TL falls out with no enum at all:

| Frontmatter | TL cell | Reading |
|---|---|---|
| *(nothing)* | open obligation | Asserted, warranted only by consistency with the admitted set |
| `stipulated: <source path>` | declared axiom | Warrant by fiat; the source says whose |
| `certified: <check>` | checked certificate | Warrant by a named, re-runnable check |
| `retracted: <tombstone>` | — | Withdrawn; body says why, path survives |

Absence is the cheap default, which is `good-smells`' CE (cheap entry,
expensive promotion) and BF (bare form stays legal). Nothing is
demanded at entry — UO. And a `certified:` claim is visibly different
from one nobody checked, which is the gap
`claims.kb/repo-weight-rung-is-unbuilt.md` opens with.

`status: asserted | contested | retracted` goes away, and takes two
problems with it. `contested` had no resolution procedure; under this
scheme a contested claim is one with a live contradiction deduction
aimed at it, which is *computed*, not declared. And `status` on
deductions — added so a disputed inference could be marked — is the
same fact, already expressible as an undercut. Two stored fields that
could disagree with the graph, replaced by one query that cannot.

## What RN implies

> The accepted set is revised under attack; refuted claims are
> retracted, propagating; open obligations are driven toward discharge
> or promotion-to-axiom; last revision wins.

**Propagation needs exactly one walkable edge, and it exists.**
`premises` → `conclusion` on deductions is typed, directed and
polarized. Retracting a claim undermines every deduction holding it as
a premise, and any conclusion whose support was only that deduction
falls back to open. This is a derived recomputation over the spine, not
a status to hand-edit — which is why warrant-by-field-presence is the
right representation: `certified:` on a node whose premise just died
must go stale, and a walker can say so.

**The leak has to close.** `depends:` is documented as context and
written as support. The fix is a schema rule, not advice: **`depends:`
may not point from a claim to a claim.** Support between claims goes
through a deduction, which is the design's own stated invariant
(ADR-006) finally enforced. This costs a file per support edge — real
friction, and exactly the CE trade: context is free, support is
promoted deliberately. It is also WC (writing the deduction forces the
judgment it records). This realm's own graph, 11 claims and zero
deductions, is the first thing the rule would reject.

**Obligation is a view.** Per
`claims.kb/obligation-is-derived-not-stored.md`: a claim is obligated
to the extent conclusions rest on it — an importance-weighted
reverse-dependency query over the spine. A command, never a field.

**Tombstones, not deletions.** Per
`claims.kb/retraction-is-revision-to-tombstone.md`, retraction is
revision under last-wins: the body becomes the tombstone, the path
stays. Names outlive contents, so every existing reference keeps
resolving and the walker can still see what died.

**The seam holds.** `certified:` names a check that runs below the
ledger and is monotonic; the certification record lives above and is
dynamic. Storing a check's *verdict* without its name would violate
the seam — hence a check reference, not a boolean.

## What the axioms do not imply

Stated rather than smuggled, per the audit's own rule.

- **`questions.kb/` is not derivable.** Worse, the realm's own
  `two-base-statuses-not-four.md` says an open claim *is* effectively a
  question, so the axioms arguably merge them. Keeping questions is an
  ergonomic decision: at repo weight files are cheap, and "how should X
  absorb Y" does not restate as a proposition without distortion.
  Legitimate — but a decision, not a derivation. **Needs fiat.**
- **`definitions.kb/` is not derivable.** A definition is not truth-apt.
  Keep on independent grounds; the axioms simply do not reach it.
- **`sources.kb/` is half-derivable.** TL's `declared axiom` cell needs
  an attributable declarer, so `stipulated:` requires provenance —
  which is precisely why ADR-2026-07-03-001's `user`/`assistant` kinds
  matter more under this design than they did under the old one.

So {TL, RN} implies three collections. Five is the right answer anyway,
for reasons outside the axioms — and that is the honest thing to write
down.

## The mechanism

Everything above is inert without checks. `llm.kb-validate` is the
existing surface; `2026-07-24-000-warrant-audit.prototype/` is a
working sketch of the hard one.

1. **No claim→claim `depends:`.** Schema-level. Closes the leak.
2. **No live node points at a retracted node.** Already implemented and
   already catching a real defect.
3. **Stale certificates.** A `certified:` node with a retracted
   ancestor on its premise chain is flagged: re-run or fall back to
   open.
4. **Obligation view.** `llm.kb-obligations` — reverse-dependency
   query, ranked. Read, not enforced.

Checks 1–3 fail the build. Check 4 is a report. That split is the
seam again: mechanical facts are enforced, judgment is surfaced.

## Open for fiat

- **`likelihood`.** Under this design it has no cell. "How sure" is not
  a warrant, and TL's whole point is that warrant is what gets
  recorded; a hand-written scalar that is never recomputed cannot be
  the derived warrant-mix. The argument for keeping it: it records a
  partial judgment cheaply, which is UO, and SV wants standing visible
  at a glance. **Recommendation: obviate.** Genuine probabilistic
  content belongs in the claim's text, where "X holds with p≈0.9" is a
  different and checkable claim rather than a hedge on X. This is the
  entry most likely to draw disagreement, so it is flagged rather than
  assumed.
- **Questions as a collection**, above.

## Cost

Migration is real: every graph in the fleet drops `status:` and
`likelihood:`, and every claim→claim `depends:` becomes a deduction or
loses its support reading. This realm migrates first — the only honest
test. The rule that rejects our own graph is the evidence it bites.
