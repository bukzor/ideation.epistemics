"""The moves of the table (`MOVE_TABLE`), each tagged with its actor.

Not yet here: reword, close a question. Neither changes anything the model
represents until text or a closed state enters it.
"""

from dataclasses import dataclass
from typing import Literal

from .model import Claim, ClaimId

Actor = Literal["owner", "agent"]


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


Move = Add | Stipulate | SettleWording | Split | Merge | Retract


@dataclass(frozen=True)
class Step:
    actor: Actor
    move: Move
