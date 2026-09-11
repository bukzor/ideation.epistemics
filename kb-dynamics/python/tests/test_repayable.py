"""Property one: agent-only sequences hide no debt from the owner's view."""

import pytest

from kb_dynamics.agents.constant import constant_worst
from kb_dynamics.examples import load_bad_states, load_corners, load_good_states
from kb_dynamics.harness import run
from kb_dynamics.repayable import hidden
from kb_dynamics.rules import RULES

STATES = {
    example.path.stem: example.state
    for example in [*load_bad_states(), *load_good_states(), *load_corners()]
}


class DescribeAgentOnlySequences:
    @pytest.mark.parametrize("name", STATES)
    def it_hides_no_debt_under_the_constant_worst_agent(self, name: str):
        initial = STATES[name]
        final, log = run(initial, constant_worst, RULES, steps=10)
        assert not any(hidden(initial, log, final).values()), (
            log,
            hidden(initial, log, final),
        )
