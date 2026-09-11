"""Property four: each rule has an effect -- without it, some sequence hides debt."""

import pytest
from hypothesis import find, settings
from hypothesis.errors import NoSuchExample

from kb_dynamics.agents.constant import constant_worst
from kb_dynamics.harness import run
from kb_dynamics.model import State
from kb_dynamics.moves import Step
from kb_dynamics.repayable import hidden
from kb_dynamics.rules import RULES, Rule
from strategies import STATES, agent_runs


def without(rule: Rule) -> tuple[Rule, ...]:
    return tuple(other for other in RULES if other is not rule)


def constant_witnesses(rule: Rule) -> list[str]:
    """The recorded states from which the constant-worst agent hides debt without `rule`."""
    found: list[str] = []
    for name, initial in STATES.items():
        final, log = run(initial, constant_worst, without(rule), steps=10)
        if any(hidden(initial, log, final).values()):
            found.append(name)
    return found


def random_witness(rule: Rule) -> tuple[str, State, tuple[Step, ...], State] | None:
    """The smallest random run that hides debt without `rule`, or None if none is found."""

    def hides(agent_run: tuple[str, State, tuple[Step, ...], State]) -> bool:
        _, initial, log, final = agent_run
        return any(hidden(initial, log, final).values())

    try:
        return find(
            agent_runs(without(rule)), hides, settings=settings(max_examples=500)
        )
    except NoSuchExample:
        return None


class DescribeEachRule:
    @pytest.mark.parametrize("rule", RULES, ids=[rule.name for rule in RULES])
    def it_has_a_sequence_that_hides_debt_without_it(self, rule: Rule):
        assert constant_witnesses(rule) or random_witness(rule), rule.name
