"""What a claim and a state are made of.

A state is a whole ledger: a map from claim id to claim. Trust is never
stored on the claim; it is computed from the grounds (`EFFECTIVE_BASIS`).
"""

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Literal

ClaimId = str
Basis = Literal["user", "derived", "evidence", "proposed", "question"]
Wording = Literal["settled", "draft"]


@dataclass(frozen=True)
class Claim:
    basis: Basis
    wording: Wording
    grounds: frozenset[ClaimId]
    content: frozenset[int]


State = Mapping[ClaimId, Claim]
