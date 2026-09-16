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
  - LABEL  # the layout rule's placeholder, `<slug>/LABEL.md`
  - CLAUDE  # `CLAUDE.md`, in the scans
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

    words-from-outside/IMPORTED_TERMS       <- (outer projects, by outward `why:` links)
    why-ledgers-rot/PROBLEM                 <- IMPORTED_TERMS
    states-and-moves/MODEL                  <- IMPORTED_TERMS, PROBLEM
    what-no-move-may-raise/DEBT             <- MODEL, IMPORTED_TERMS
      the-kinds-of-rot/COMPONENTS           <- DEBT (nested: one claim per kind of rot)
    what-the-harness-shows/HARNESS          <- DEBT, MODEL, IMPORTED_TERMS
    weighing-a-candidate-rule/RULE_PRICING  <- DEBT, HARNESS, IMPORTED_TERMS
    the-order-of-work/METHOD                <- HARNESS, RULE_PRICING, DEBT

`IMPORTED_TERMS` alone may cite outside `kb-dynamics/`; every other theory
takes the outer words through it. Read top-down: `PROBLEM` says why the
model exists, `MODEL` and `DEBT` say what it is, `HARNESS` says what is
shown about it and how, `RULE_PRICING` is the field-side vocabulary for
weighing a rule, `METHOD` is the order of work and the payout test.

Every claim is `<slug>/LABEL.md`, the slug naming its locus and the stem
its label; a theory is that beside `<slug>/LABEL.kb/`. So a path is a
citation, and `find` is the label index.

## Scans

    find claims.kb -name '*.md' -not -name CLAUDE.md | sort   # every claim, slug and label
    grep -rH '^standing:' claims.kb/ | sort -t: -k3
    grep -rl 'verdict:' claims.kb/
    grep -rl 'standing: open' claims.kb/      # what no one has ruled
    grep -rl 'todo: true' claims.kb/          # decided, not built
    claims.kb/words-from-outside/IMPORTED_TERMS.verify.py
