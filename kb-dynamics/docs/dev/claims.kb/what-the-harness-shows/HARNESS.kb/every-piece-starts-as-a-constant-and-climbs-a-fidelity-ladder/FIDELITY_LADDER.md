---
label: FIDELITY_LADDER
standing: user
authority: chat.md#L576
why:
  - ../the-agent-is-replaced-by-a-generator-not-modeled/GENERATOR_NOT_AGENT.md
---

# Every piece starts as a constant and climbs a fidelity ladder on demand

Every piece of the harness starts as an obviously-wrong constant and is
replaced only when a property demands more of it.

> [!@bukzor] chat.md#L576
> Yes. For me, simulation can be of any fidelity, including an obviously-wrong constant. This is related to tdd methodology.

A constant agent is not a claim about the agent; it is a stub, replaced
exactly when a property cannot be exercised without something better.
Everything starts that way: the generator always emits one bad move,
debt is zero everywhere, the rule set is empty, the transition is the
identity. The first red test is a hand-written bad state with debt above
zero; debt grows to count it. The next red is the worst-case generator
driving debt up unboundedly; a rule enters and the test goes green. A
rule enters the set only because a test demanded it, which is stronger
provenance than a tally.

The ladder for the generator: constant-worst, uniform random,
adversarial search, biased toward observed behavior. Each rung is earned
by a property the previous rung could not exercise. This is consistent
with `GENERATOR_NOT_AGENT`: the rule is not "never model the agent" but
"never write the agent model before a property demands it", TDD's own
rule. Only the top rung is a model of the agent, and it is earned last.
