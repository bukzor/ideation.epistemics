---
label: GENERATOR_NOT_AGENT
standing: user
authority: chat.md#L501, the owner's request; chat.md#L576, the owner's ratification of the steelman
why:
  - ../imported-terms.kb/coverage.md
---

# The agent is replaced by a move generator, not modeled

The harness explores everything an agent could do under the rules; it
does not predict what an agent will do. Moves are tagged by actor, but
no actor has a policy. A random or adversarial generator is better than
a realistic one for the purpose, which is to find where the debt
function, the fields, and the rules are wrong.

> [!@bukzor] chat.md#L177
> well, my take is that I don't have a great handing on the dynamics of this system, that my instructions and/or the agent behavior is taking the kbs in a bad direction. As such my proposed way forward is a simulation of the agent/user/kb state transitions, such that we can build up a clearer picture of what's going wrong, how to set up dynamics that ensure constructive state transitions.

> [!@bukzor] chat.md#L501
> Design a minimal simulation that will help me develop insight/confidence into such things before they're committed to.

> [!DRAFT] chat.md#L177, chat.md#L501, chat.md#L576
> The steelmanned proposal: an executable model of the ledger's state
> space and the moves on it, so that design questions -- what fields,
> what rules, what counts as good -- can be explored rigorously and
> cheaply before real infrastructure is committed to. "Simulation" was
> doing the work of "executable model I can experiment on". The
> original named two goals; the harness serves "dynamics that ensure
> constructive transitions" fully, and "a clearer picture of what's
> going wrong" goes to the field (`SANDBOX_VS_FIELD`).

Declined: a simulation with a written agent policy. The unknown in the
system is the agent's behavior, and a model of it would be the owner's
assumptions about the agent, giving a rigorous-looking picture of
dynamics already half-believed with the real failure modes simulated
away.
