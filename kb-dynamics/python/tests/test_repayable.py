"""Property one: agent-only sequences hide no debt from the owner's view."""

import pytest
from hypothesis import given, settings

from kb_dynamics.agents.constant import constant_worst
from kb_dynamics.harness import run
from kb_dynamics.model import State
from kb_dynamics.moves import Step
from kb_dynamics.repayable import hidden
from kb_dynamics.rules import RULES
from strategies import STATES, agent_runs


class DescribeAgentOnlySequences:
    @pytest.mark.parametrize("name", STATES)
    def it_hides_no_debt_under_the_constant_worst_agent(self, name: str):
        initial = STATES[name]
        final, log = run(initial, constant_worst, RULES, steps=10)
        assert not any(hidden(initial, log, final).values()), (
            log,
            hidden(initial, log, final),
        )

    @settings(max_examples=300)
    @given(agent_runs(RULES))
    def it_hides_no_debt_under_a_random_agent(
        self, agent_run: tuple[str, State, tuple[Step, ...], State]
    ):
        name, initial, log, final = agent_run
        assert not any(hidden(initial, log, final).values()), (
            name,
            log,
            hidden(initial, log, final),
        )
