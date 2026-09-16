---
label: BASIS_WORDING
standing: user
authority: d3d3f372, the owner's ruling of 2026-09-11
why:
  - ../../../why-ledgers-rot/PROBLEM.kb/one-standing-field-confuses-three-situations/THREE_CONFUSIONS.md
  - ../../../words-from-outside/IMPORTED_TERMS.kb/standing/IMPORTED_STANDING.md
  - ../../../words-from-outside/IMPORTED_TERMS.kb/stipulated/IMPORTED_STIPULATED.md
  - ../../../words-from-outside/IMPORTED_TERMS.kb/certified/IMPORTED_CERTIFIED.md
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

> [!@bukzor] d3d3f372
> Yes, accepted. And yes: round-tripping is a work item.

Declined: keeping one enum and adding values for each case. A single
enum over a product space produces edge cases forever.
