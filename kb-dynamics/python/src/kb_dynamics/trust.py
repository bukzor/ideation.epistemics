"""Trust is per claim; a ledger's trust is an aggregation over its claims.

The owner's review conditions (`TRUST_TEST`) say when the queue is done or
doable; they are computed here as aggregations too, and none is an
attribute of the ledger. "Fits one sitting" is a field quantity the
sandbox cannot compute and is not stubbed.
"""

from collections.abc import Mapping
from typing import Literal

from .debt import effective_basis, queue
from .model import ClaimId, State

Condition = Literal[
    "queue-empty",
    "skeleton-right",
    "all-trusted",
]
CONDITIONS: tuple[Condition, ...] = (
    "queue-empty",
    "skeleton-right",
    "all-trusted",
)
Verdicts = Mapping[Condition, bool]


def trusted(state: State, claim_id: ClaimId) -> bool:
    """A claim is trusted when its fold reaches no proposed claim (`EFFECTIVE_BASIS`)."""
    return effective_basis(state, claim_id) != "proposed"


def all_trusted(state: State) -> bool:
    return all(trusted(state, claim_id) for claim_id in state)


def queue_empty(state: State) -> bool:
    return not queue(state)


def skeleton_right(state: State) -> bool:
    """The owner has read every user claim, and everything else is derivable and disposable.

    Read means settled wording. Derivable means the fold reaches no proposed
    claim. Disposable means no user claim rests on a non-user one.
    """
    return (
        all(
            claim.wording == "settled"
            for claim in state.values()
            if claim.basis == "user"
        )
        and all_trusted(state)
        and all(
            state[ground].basis == "user"
            for claim in state.values()
            if claim.basis == "user"
            for ground in claim.grounds
            if ground in state
        )
    )


def verdicts(state: State) -> Verdicts:
    return {
        "queue-empty": queue_empty(state),
        "skeleton-right": skeleton_right(state),
        "all-trusted": all_trusted(state),
    }
