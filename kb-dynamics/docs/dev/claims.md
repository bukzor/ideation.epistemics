---
label: KB_DYNAMICS
standing: agent
ontology:
  - debt
  - good state
  - basis
  - wording
  - grounds
  - load-bearing
non-claim-tokens:
  - RULES
  - DRAFT
  - README
  # `chat.md#L<n>` quote addresses: label-shaped, a known scanner collision
  - L103
  - L105
  - L107
  - L177
  - L185
  - L190
  - L230
  - L259
  - L261
  - L320
  - L392
  - L422

  - L498
  - L501
  - L576
  - L632
  # `f65fbdf3#L<n>`: the 2026-09-11 grounding sitting, same collision
  - L606
  - L815
  - L995
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
`../../../docs/dev/chats/claude/Created=2026/09/09/14:14:39-05:00/`; the
ledger replaces that chat as the entry point, and a `chat.md#L<n>`
address anywhere in it points into the `chat.md` one titled directory below it.

## Theories

    imported-terms   <- (outer projects, by outward `why:` links)
    problem          <- imported-terms
    model            <- imported-terms, problem
    debt             <- model, imported-terms
      components     <- debt (nested: one claim per kind of rot)
    harness          <- debt, model, imported-terms
    rule-pricing     <- debt, harness, imported-terms
    method           <- harness, rule-pricing, debt

`imported-terms` alone may cite outside `kb-dynamics/`; every other theory
takes the outer words through it. Read top-down: `problem` says why the
model exists, `model` and `debt` say what it is, `harness` says what is
shown about it and how, `rule-pricing` is the field-side vocabulary for
weighing a rule, `method` is the order of work and the payout test.

## Scans

    grep -rH '^standing:' claims.kb/ | sort -t: -k3
    grep -rl 'verdict:' claims.kb/
    grep -rl 'standing: open' claims.kb/      # what no one has ruled
    grep -rl 'todo: true' claims.kb/          # decided, not built
    claims.kb/imported-terms.verify.py
