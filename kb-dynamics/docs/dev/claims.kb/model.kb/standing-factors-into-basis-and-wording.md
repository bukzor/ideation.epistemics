---
label: BASIS_WORDING
standing: agent
why:
  - ../problem.kb/one-standing-field-confuses-three-situations.md
  - ../imported-terms.kb/standing.md
  - ../imported-terms.kb/stipulated.md
---

# Standing factors into two fields: basis and wording

A claim carries two orthogonal fields in place of one standing:

- `basis` -- why we believe it: `user` (the owner asserts it; stipulated,
  the ground), `derived` (follows from its grounds; inherits trust from
  them), `evidence` (externally checkable; certified), `proposed` (agent
  filler with no ground yet), `question`.
- `wording` -- whether the text renders the content faithfully:
  `settled` or `draft`.

The three confusions run through it as: agent-authored and owner-endorsed
with unvetted text is `basis: user, wording: draft`; owner shorthand
needing a steelman is `basis: user, wording: draft`; a well-grounded
agent draft is `basis: derived` with grounds reaching `basis: user`
claims. Cases one and two collapse into one state, which is the sign the
factoring is right: what differed between them, who typed the draft,
does not change what should happen next (`NEXT_ACTION_TEST`). Case three
stops needing a status of its own because trust is computed
(`EFFECTIVE_BASIS`).

Declined: keeping one enum and adding values for each case. A single
enum over a product space produces edge cases forever.
