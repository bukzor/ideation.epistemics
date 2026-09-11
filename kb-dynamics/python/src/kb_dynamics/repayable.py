"""Hidden debt: rot the owner's view of the ledger has that the recorded ledger lacks.

The sanction table is the authority column of the move table
(`MOVE_TABLE`): what an unlicensed move means in the owner's eyes. An
unlicensed settling of wording or stipulation means nothing; an unlicensed
add means adding as proposed with draft wording; an unlicensed retraction
of a user claim means nothing (`PRUNE_GUARD`); an unlicensed merge means
nothing unless the two claims say one thing and neither is the owner's.
Replaying the log under the sanction table gives the owner's view, and any
debt it carries that the recorded ledger does not is hidden: the sandbox's
form of "no pathway" (`UNREPAYABLE`).
"""

from collections.abc import Sequence
from dataclasses import replace
from typing import assert_never

from .debt import COMPONENTS, Debt, debt
from .model import State
from .moves import Add, Merge, Retract, SettleWording, Split, Step, Stipulate, licensed
from .transition import Reject, transition


def as_owner_sees(state: State, step: Step) -> Step | None:
    """The move as sanctioned for its authority, or None when it means nothing."""
    if licensed(step):
        return step
    move = step.move
    match move:
        case Add(claim_id, claim):
            basis = "proposed" if claim.basis == "user" else claim.basis
            return replace(
                step, move=Add(claim_id, replace(claim, basis=basis, wording="draft"))
            )
        case Stipulate() | SettleWording():
            return None
        case Retract(claim_id):
            if claim_id in state and state[claim_id].basis == "user":
                return None
            else:
                return step
        case Merge(keep, drop):
            if keep not in state or drop not in state:
                return step
            elif state[drop].basis == "user":
                return None
            elif state[keep].content != state[drop].content:
                return None
            else:
                return step
        case Split():
            return step
        case _:
            assert_never(move)


def owner_view(initial: State, log: Sequence[Step]) -> State:
    state = initial
    for step in log:
        seen = as_owner_sees(state, step)
        if seen is not None:
            after = transition(state, seen)
            if not isinstance(after, Reject):
                state = after
    return state


def hidden(initial: State, log: Sequence[Step], recorded: State) -> Debt:
    """Componentwise, how much rot the owner's view has beyond the record."""
    owners = debt(owner_view(initial, log))
    records = debt(recorded)
    return {c: max(0, owners[c] - records[c]) for c in COMPONENTS}
