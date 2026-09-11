"""Property four: each rule has an effect -- without it, some sequence hides debt."""

import pytest

from kb_dynamics.agents.constant import constant_worst
from kb_dynamics.examples import load_bad_states, load_corners, load_good_states
from kb_dynamics.harness import run
from kb_dynamics.repayable import hidden
from kb_dynamics.rules import RULES, Rule

STATES = {
    example.path.stem: example.state
    for example in [*load_bad_states(), *load_good_states(), *load_corners()]
}


def witnesses(without: Rule) -> list[str]:
    """The recorded states from which the constant-worst agent hides debt once `without` is removed."""
    remaining = tuple(rule for rule in RULES if rule is not without)
    found: list[str] = []
    for name, initial in STATES.items():
        final, log = run(initial, constant_worst, remaining, steps=10)
        if any(hidden(initial, log, final).values()):
            found.append(name)
    return found


class DescribeEachRule:
    @pytest.mark.parametrize("rule", RULES, ids=[rule.name for rule in RULES])
    def it_has_a_sequence_that_hides_debt_without_it(self, rule: Rule):
        assert witnesses(rule), rule.name
