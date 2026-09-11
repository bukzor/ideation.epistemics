"""The transition: total over (state, move); a cell that cannot apply is a Reject."""

from dataclasses import dataclass, replace
from typing import assert_never

from .model import Claim, ClaimId, State
from .moves import Add, Merge, Retract, SettleWording, Split, Step, Stipulate


@dataclass(frozen=True)
class Reject:
    reason: str


def reground(
    state: State, old: ClaimId, new: frozenset[ClaimId]
) -> dict[ClaimId, Claim]:
    """Every claim grounded on `old` grounds on `new` instead."""
    return {
        claim_id: (
            replace(claim, grounds=(claim.grounds - {old}) | new)
            if old in claim.grounds
            else claim
        )
        for claim_id, claim in state.items()
    }


def transition(state: State, step: Step) -> State | Reject:
    move = step.move
    match move:
        case Add(claim_id, claim):
            if claim_id in state:
                return Reject(f"{claim_id} exists")
            elif not claim.grounds <= state.keys():
                return Reject(f"{claim_id} grounds on a claim not in the state")
            else:
                return {**state, claim_id: claim}
        case Stipulate(claim_id):
            if claim_id not in state:
                return Reject(f"{claim_id} missing")
            else:
                return {**state, claim_id: replace(state[claim_id], basis="user")}
        case SettleWording(claim_id):
            if claim_id not in state:
                return Reject(f"{claim_id} missing")
            else:
                return {**state, claim_id: replace(state[claim_id], wording="settled")}
        case Split(claim_id, left, right, left_content):
            if claim_id not in state:
                return Reject(f"{claim_id} missing")
            elif left in state or right in state or left == right:
                return Reject(f"{left} or {right} exists")
            elif not (left_content and left_content < state[claim_id].content):
                return Reject(
                    f"{left_content} is not a proper nonempty part of {claim_id}"
                )
            else:
                whole = state[claim_id]
                rest = {
                    k: v
                    for k, v in reground(
                        state, claim_id, frozenset({left, right})
                    ).items()
                }
                del rest[claim_id]
                return {
                    **rest,
                    left: replace(whole, content=left_content),
                    right: replace(whole, content=whole.content - left_content),
                }
        case Merge(keep, drop):
            if keep not in state or drop not in state or keep == drop:
                return Reject(f"cannot merge {drop} into {keep}")
            else:
                rest = reground(state, drop, frozenset({keep}))
                del rest[drop]
                return rest
        case Retract(claim_id):
            if claim_id not in state:
                return Reject(f"{claim_id} missing")
            else:
                return {k: v for k, v in state.items() if k != claim_id}
        case _:
            assert_never(move)
