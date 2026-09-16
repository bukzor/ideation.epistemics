---
label: THREE_CONFUSIONS
standing: user
authority: chat.md#L185, the owner's own enumeration
why:
  - ../../../words-from-outside/IMPORTED_TERMS.kb/standing/IMPORTED_STANDING.md
---

# One standing field confuses three situations the owner meets in practice

The owner named three situations the incumbent standing field cannot
tell apart, and a fourth constraint on any repair:

> [!@bukzor] chat.md#L185
> 1. claims that are stipulated by me but authored by agent (perhaps with some problematic, unreviwed word choice)
> 2. claims that are stipulated by me in a problematic shorthand, that need steelmanning to be usable. under current procedures, agents are unwilling to touch the wording of such claims.
> 3. claims that are agent-drafted but so well-grounded they should properly be treated as factual

> [!@bukzor] chat.md#L190
> More generally, there seems to be a plethora of edge cases that are not well-representable in the current system. At the same time, I don't want a system that can represent *anything* -- that way lies madness.

These three are the first three test cases of any model of a claim's
state, written before the tooling. The diagnosis they support is that
one enum is encoding at least three orthogonal things -- who authored
the text, who endorses the content, how well the content is grounded --
and a single enum over a product space produces edge cases forever
(`BASIS_WORDING` in `../../../states-and-moves/MODEL.md`).
