"""The corners of TRUST_TEST: pinned verdicts, so the conditions cannot drift unnoticed."""

import pytest

from kb_dynamics.examples import Corner, load_corners
from kb_dynamics.trust import verdicts

CORNERS = list(load_corners())


class DescribeTrustConditions:
    @pytest.mark.parametrize("corner", CORNERS, ids=[c.path.stem for c in CORNERS])
    def it_gives_the_recorded_verdict_on_every_corner(self, corner: Corner):
        assert dict(verdicts(corner.state)) == dict(corner.verdicts)
