"""Trust per claim against the queue: the owner's conjecture and its converse."""

import pytest

from kb_dynamics.examples import Corner, load_bad_states, load_corners, load_good_states
from kb_dynamics.trust import all_trusted, queue_empty, verdicts

CORNERS = list(load_corners())
STATES = {
    example.path.stem: example.state
    for example in [*load_bad_states(), *load_good_states(), *CORNERS]
}


class DescribeTrustAndTheQueue:
    @pytest.mark.parametrize("name", STATES)
    def it_trusts_every_claim_when_the_queue_is_empty(self, name: str):
        state = STATES[name]
        assert not queue_empty(state) or all_trusted(state), verdicts(state)

    def it_can_trust_every_claim_with_a_non_empty_queue(self):
        witnesses = [
            n for n, s in STATES.items() if all_trusted(s) and not queue_empty(s)
        ]
        assert "rot-among-user-claims-only" in witnesses, witnesses

    @pytest.mark.parametrize("corner", CORNERS, ids=[c.path.stem for c in CORNERS])
    def it_gives_the_recorded_verdict_on_every_corner(self, corner: Corner):
        assert dict(verdicts(corner.state)) == dict(corner.verdicts)
