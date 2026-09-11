"""The ladder's first rung: an agent that always makes the worst move it can find."""

from ..model import State
from ..moves import SettleWording, Step, Stipulate


def constant_worst(state: State) -> Step | None:
    """Settle a draft owner claim's wording, else stipulate a proposed claim, else nothing."""
    for claim_id, claim in sorted(state.items()):
        if claim.basis == "user" and claim.wording == "draft":
            return Step("agent", SettleWording(claim_id))
    for claim_id, claim in sorted(state.items()):
        if claim.basis == "proposed":
            return Step("agent", Stipulate(claim_id))
    return None
