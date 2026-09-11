"""Properties two and three: debt sees every recorded bad state, and only those."""

import pytest

from kb_dynamics.debt import debt
from kb_dynamics.examples import BadState, GoodState, load_bad_states, load_good_states

BAD = list(load_bad_states())
GOOD = list(load_good_states())


class DescribeDebt:
    @pytest.mark.parametrize("example", BAD, ids=[b.path.stem for b in BAD])
    def it_is_positive_in_the_named_component_of_every_bad_state(
        self, example: BadState
    ):
        assert debt(example.state)[example.rot] > 0, (example.rot, debt(example.state))

    @pytest.mark.parametrize("example", GOOD, ids=[g.path.stem for g in GOOD])
    def it_is_zero_on_every_good_state(self, example: GoodState):
        assert not any(debt(example.state).values()), debt(example.state)
