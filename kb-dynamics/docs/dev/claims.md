---
label: KB_DYNAMICS
standing: agent
ontology:
  - debt
  - good state
stale-when: a property that passes under a random agent while a real ledger still drifts under the same rules
---

# kb-dynamics, as a ledger

A claim ledger is a state, an agent's or owner's edit to it is a move, and
debt is a function of the state that no permitted move may raise: the
load-bearing claims resting on an unwarranted one, the claims that should
be split, the duplicate pairs, the draft wording on load-bearing claims.
Good state is debt zero. What the design commits to beyond that is a claim
in this ledger.

Formed 2026-09-10 from the chat captured under
`../../../docs/dev/chats/claude/Created=2026/09/09/14:14:39-05:00/`.

## Theories

    imported-terms   <- (outer projects, by outward `why:` links)

`imported-terms` alone may cite outside `kb-dynamics/`; every other theory
takes the outer words through it.

## Scans

    grep -rH '^standing:' claims.kb/ | sort -t: -k3
    grep -rl 'verdict:' claims.kb/
    claims.kb/imported-terms.verify.py
