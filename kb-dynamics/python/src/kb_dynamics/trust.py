"""The three conditions of `TRUST_TEST`, each sufficient on its own.

Condition one is written two ways in the ledger, "queue empty" and "no
load-bearing claim rests on a proposed basis"; both are computed so the
corners where they part are visible.
"""

from collections.abc import Mapping
from typing import Literal

from .debt import load, proposed_roots, queue
from .model import State

Condition = Literal[
    "queue-empty",
    "no-load-bearing-on-proposed",
    "fits-one-sitting",
    "skeleton-right",
]
CONDITIONS: tuple[Condition, ...] = (
    "queue-empty",
    "no-load-bearing-on-proposed",
    "fits-one-sitting",
    "skeleton-right",
)
Verdicts = Mapping[Condition, bool]

# `QUEUE` pictures a sitting as "the seven proposed claims that, if wrong,
# break the most downstream work"; a constant until a property prices it.
SITTING = 7


def queue_empty(state: State) -> bool:
    return not queue(state)


def no_load_bearing_on_proposed(state: State) -> bool:
    return all(load(state, root) == 0 for root in proposed_roots(state))


def fits_one_sitting(state: State) -> bool:
    return len(queue(state)) <= SITTING


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
        and not any(proposed_roots(state))
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
        "no-load-bearing-on-proposed": no_load_bearing_on_proposed(state),
        "fits-one-sitting": fits_one_sitting(state),
        "skeleton-right": skeleton_right(state),
    }


def trusted(state: State) -> bool:
    """Any of the owner's three conditions, condition one taken by the letter."""
    return queue_empty(state) or fits_one_sitting(state) or skeleton_right(state)
