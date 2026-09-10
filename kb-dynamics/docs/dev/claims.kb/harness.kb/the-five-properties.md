---
label: FIVE_PROPERTIES
standing: agent
why:
  - the-agent-is-replaced-by-a-generator-not-modeled.md
  - ../debt.kb/no-agent-move-raises-debt-silently.md
  - ../imported-terms.kb/example.md
  - ../imported-terms.kb/flip.md
---

# The five properties, and what a failure of each means

1. Agent-only move sequences never raise debt under the current rules.
   Failure: a missing rule, or a component counting wrong. The generator
   hands back the shortest breaking sequence.
2. Every recorded bad state -- the three confusions, anything spotted in
   a real ledger -- has debt above zero. Failure: debt is blind to
   something the owner cares about.
3. Every debt-zero state satisfies every named goodness predicate. The
   converse of 2.
4. For each rule, some sequence exists where removing it lets debt rise.
   Failure: the rule is dead weight. This is the flip test
   (`IMPORTED_FLIP`) in miniature, and the minimality test as something
   the machine runs rather than an argument.
5. From any reachable state, some owner-plus-agent sequence reaches debt
   zero. Failure: a stuck state, a missing transition.

Sketch of the first:

```python
@given(move_sequences(actor="agent"))
def test_agent_moves_never_raise_debt(moves):
    state = empty()
    for move in moves:
        if all(rule(state, move) for rule in RULES):
            after = transition(state, move)
            assert debt(after) <= debt(state), (state, move)
            state = after
```

Each counterexample is a specific flaw found in seconds and fixed in a
few lines. When a property holds across thousands of sequences the
design is internally coherent, and building against real data stops
being a bet.
