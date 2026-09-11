"""The moves of the table (`MOVE_TABLE`), each tagged with the authority it carries.

Authority, not hands (`AUTHORITY_NOT_HANDS`): a move made by an agent on
the owner's word carries the owner's authority and cites its license, the
address of the ruling or of the standing rule. A move with no license is
the agent's own.

Not yet here: reword, which changes nothing the model represents until
text enters it.
"""

from dataclasses import dataclass

from .model import Claim, ClaimId


@dataclass(frozen=True)
class Owner:
    """The owner's authority, with the address that licenses the move."""

    license: str


@dataclass(frozen=True)
class Agent:
    """The agent's own authority: no license."""


Authority = Owner | Agent
AGENT = Agent()


@dataclass(frozen=True)
class Add:
    claim_id: ClaimId
    claim: Claim


@dataclass(frozen=True)
class Stipulate:
    claim_id: ClaimId


@dataclass(frozen=True)
class SettleWording:
    claim_id: ClaimId


@dataclass(frozen=True)
class Split:
    """Replace one claim by two that partition its content; dependents ground on both."""

    claim_id: ClaimId
    left: ClaimId
    right: ClaimId
    left_content: frozenset[int]


@dataclass(frozen=True)
class Merge:
    """Drop one claim; its dependents ground on the kept one instead."""

    keep: ClaimId
    drop: ClaimId


@dataclass(frozen=True)
class Retract:
    """Remove a claim; dependents keep the dangling ground, which the fold reads as proposed."""

    claim_id: ClaimId


@dataclass(frozen=True)
class Close:
    """A question's terminal state besides answered (`CLOSED_QUESTION`): removed, once a leaf."""

    claim_id: ClaimId


Move = Add | Stipulate | SettleWording | Split | Merge | Retract | Close


@dataclass(frozen=True)
class Step:
    authority: Authority
    move: Move


def licensed(step: Step) -> bool:
    return isinstance(step.authority, Owner)
