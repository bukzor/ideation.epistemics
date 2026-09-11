---
label: SESSION_MODEL
standing: agent
ontology:
  - session
  - owner
  - agent
non-claim-tokens:
  - CLAUDE
stale-when: a ruling that the model is to be fitted to the corpus rather than tested by generated scenarios
---

# The session model, as a ledger

The framework half of a family of models of one thing: a session in which an
agent acts under rules, asks the owner for decisions, and reads its rules
through carriers that may or may not arrive. Its three priors live where their
subjects already had a ledger: `commitment` and `ask` beside the design claims
in `bukzor-agent-skills/docs/dev/claims.kb/design.claims.kb/`, `carriage` in
`strata.claims.kb/` beside `protocol`. What is here is the part no fleet ledger
held: rules as things that run, and three simulations at increasing detail.

Formed in session `f9bdf6f0-d5fd-48a2-b065-da485f78241c` on 2026-09-09 from the
2026-09-03 review of the session corpus and its follow-up sittings
(`claude-code-holistics/review.kb/`).

## Theories

    law         <- commitment (design.claims.kb)
    budget      <- carriage (strata.claims.kb)
    trace-sim   <- carriage, budget
    session-sim <- trace-sim, law, ask, commitment

`budget` runs today from file sizes. `trace-sim` is the first simulated
interaction and has no owner in it. `session-sim` is the full game.

## Scans

    grep -rH '^standing:' session-model.claims.kb/ | sort -t: -k3
    grep -rl 'verdict:' session-model.claims.kb/
