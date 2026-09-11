"""Property five: from any reachable state, some owner-plus-agent sequence reaches debt zero."""

import pytest
from hypothesis import given, settings

from kb_dynamics.agents.repair import repair
from kb_dynamics.debt import debt
from kb_dynamics.harness import run
from kb_dynamics.model import State
from kb_dynamics.moves import Step
from kb_dynamics.rules import RULES
from strategies import STATES, agent_runs


def repaired(state: State) -> tuple[State, tuple[Step, ...]]:
    return run(state, repair, RULES, steps=60)


class DescribeRepair:
    @pytest.mark.parametrize("name", STATES)
    def it_reaches_debt_zero_from_every_recorded_state(self, name: str):
        final, log = repaired(STATES[name])
        assert not any(debt(final).values()), (debt(final), log)

    @settings(max_examples=200)
    @given(agent_runs(RULES))
    def it_reaches_debt_zero_from_every_state_a_random_agent_reaches(
        self, agent_run: tuple[str, State, tuple[Step, ...], State]
    ):
        name, _, agent_log, reached = agent_run
        final, log = repaired(reached)
        assert not any(debt(final).values()), (name, agent_log, debt(final), log)
