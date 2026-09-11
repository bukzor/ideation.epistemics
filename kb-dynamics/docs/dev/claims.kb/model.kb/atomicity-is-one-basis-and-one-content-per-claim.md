---
label: ATOMICITY
standing: agent
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
two duplicates need not share and two different claims can share (G
entails both X and X-and-Y). Semantics: entailment, which is read, not
computed. Identical recorded ground sets are a candidate for reading,
never a finding, even were sufficiency certified on every arrow -- and
on disk it is not, until a process makes it so (`GROUND_RECORD`). The
sandbox makes content equality the semantic test by fiat
(`ATOM_CONTENT`); in the field that test is a judgment check, priced as
one (`CANDIDATE_RULES`).
