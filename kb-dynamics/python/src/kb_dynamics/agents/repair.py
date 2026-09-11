"""Property five's witness: an owner who rules yes on everything, and the agent's unasked moves.

Existence is all the property asks, so the constructive witness is the
cheapest owner: every queue item is repaid by the ruling that clears it,
and the unasked moves (`UNASKED_MOVES`) go first, since they need no
ruling at all.
"""

from ..debt import duplicates, proposed_roots
from ..model import ClaimId, State
from ..moves import AGENT, Close, Merge, Owner, SettleWording, Split, Step, Stipulate

YES = Owner("the repair witness: the owner rules yes on every item")


def fresh(state: State, stem: ClaimId) -> ClaimId:
    candidate = stem
    while candidate in state:
        candidate += "'"
    return candidate


def repair(state: State) -> Step | None:
    """The next move that lowers debt, or None at debt zero."""
    for drop in duplicates(state):
        keep = next(k for k, c in state.items() if c.content == state[drop].content)
        authority = YES if state[drop].basis == "user" else AGENT
        return Step(authority, Merge(keep, drop))
    for claim_id, claim in state.items():
        if len(claim.content) > 1:
            left = fresh(state, f"{claim_id}-a")
            right = fresh({**state, left: claim}, f"{claim_id}-b")
            return Step(
                AGENT, Split(claim_id, left, right, frozenset({min(claim.content)}))
            )
    for claim_id, claim in state.items():
        if claim.basis == "question" and not any(
            claim_id in other.grounds for other in state.values()
        ):
            return Step(AGENT, Close(claim_id))
    for root in proposed_roots(state):
        return Step(YES, Stipulate(root))
    for claim_id, claim in state.items():
        if claim.wording == "draft":
            return Step(YES, SettleWording(claim_id))
    return None
