---
label: ATOMICITY
standing: user
authority: d3d3f372, the owner's ruling of 2026-09-11, on the restated draft
why:
  - standing-factors-into-basis-and-wording.md
  - an-arrow-carries-its-kind-and-sufficiency.md
---

# Claims and contents correspond one to one, and every claim has one basis

Two invariants, and the owner's three complaints are them failing:

> [!@bukzor] chat.md#L259
> Changing focus: another problem I have is that the claims are poorly grounded, poorly factored (should be split to have different grounding per piece, for example) or duplicate (or, worse, near-duplicate).

- One basis per claim: one kind of warrant, `user` or `derived` or
  `evidence`, never a stipulated half and a derived half. A claim with
  none is ungrounded, and is marked `proposed` or given grounds.
- One content per claim: for `Z <- A B C` the grounds are jointly
  sufficient for Z, usually each necessary, and no proper part of Z is
  already carried by a proper subset of them. Z is non-atomic when it
  is P and Q with A sufficing for P and B, C for Q -- two claims
  written as one, each wanting its own grounding. Lowered by the split
  move. A claim with several alternative sufficient ground sets is not
  non-atomic; it is overdetermined, and such claims are the surest.
- One claim per content: a duplicate is two claims that entail each
  other. Lowered by the merge move, which loses nothing, since a
  restatement for another theory's reader is a citation, not a claim.

Three senses are held apart in the third. Form: the text, which finds
exact duplicates by comparison. Denotation: the recorded grounds, which
two duplicates need not share and two different claims can share.
Semantics: entailment, which is read, not computed; identical recorded
ground sets are a candidate for reading, never a finding. The
correspondence has no scope boundary: two files with one content are a
duplicate pair whatever theories or ledgers they sit in.

> [!@bukzor] d3d3f372
> In general, we don't want two claim files with the same content regardless if they're cross-theory.

> [!@bukzor] d3d3f372
> ATOMICITY: looks good now. Perhaps a bit wordy? I'm not sure the last paragraph is necessary? But wordiness is okay in these docs as long as it conveys some value.
