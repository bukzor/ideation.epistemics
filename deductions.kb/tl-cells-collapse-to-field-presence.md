---
status: asserted
kind: entailment
conclusion: ../claims.kb/warrant-by-field-presence.md
premises:
  - ../claims.kb/two-base-statuses-not-four.md
  - ../claims.kb/obligation-is-derived-not-stored.md
  - ../claims.kb/retraction-is-revision-to-tombstone.md
sources: [../sources.kb/claude.md]
tags: [repo-weight, notation]
---

TL names three justification cells. Three premises already settled in
this realm remove the need for any of them to be a stored status.

`two-base-statuses-not-four.md` collapses the enum: an asserted claim
is "effectively a question," so the open cell is the *absence* of
warrant rather than a value, and `certified` is read off a premise
chain or a named check at point of use rather than declared.
`obligation-is-derived-not-stored.md` gives the general form — standing
that can be computed must not be stored, or the two can disagree.
`retraction-is-revision-to-tombstone.md` removes the last candidate:
retraction is revision under last-wins, not a distinct primitive, so it
needs a tombstone marker and not an enum cell.

What is left to store is the warrant itself where it exists, and
nothing where it does not. That is field presence.

The incumbent supplies the mechanism unprompted: its questions already
derive state from which fields are present, carrying no status field at
all. So this is its own convention generalized from one collection to
the rest, which is why the conclusion is an improvement on the shipped
design rather than a replacement for it
(`../claims.kb/incumbent-design-is-evidence-not-canon.md`).

Not entailed: that five collections are right, or that `likelihood`
must go. Those turn on judgments the axioms do not make — see
`../repo-weight-derivation.md`.
