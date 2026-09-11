"""Loader for the language-neutral examples beside the implementations."""

from collections.abc import Iterator, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import cast

import yaml

from .debt import Component
from .model import Basis, Claim, State, Sufficiency, Wording
from .trust import Condition, Verdicts

EXAMPLES = Path(__file__).resolve().parents[3] / "examples"


@dataclass(frozen=True)
class BadState:
    path: Path
    rot: Component
    state: State


@dataclass(frozen=True)
class GoodState:
    path: Path
    state: State


@dataclass(frozen=True)
class Corner:
    path: Path
    verdicts: Verdicts
    state: State


def parse_front_matter(text: str) -> Mapping[str, object]:
    """The YAML between the leading `---` fences, as a mapping."""
    _, front, _ = text.split("---\n", 2)
    return cast(Mapping[str, object], yaml.safe_load(front))


def parse_state(claims: object) -> State:
    """Lift a `claims:` mapping into the model; values are trusted to match the schema."""
    claims = cast(Mapping[str, Mapping[str, object]], claims)
    return {
        claim_id: Claim(
            basis=cast(Basis, fields["basis"]),
            wording=cast(Wording, fields["wording"]),
            grounds=frozenset(cast(list[str], fields["grounds"])),
            content=frozenset(cast(list[int], fields["content"])),
            sufficiency=cast(Sufficiency, fields.get("sufficiency", "entails")),
        )
        for claim_id, fields in claims.items()
    }


def load_bad_states(root: Path = EXAMPLES) -> Iterator[BadState]:
    for path in sorted((root / "bad-states").glob("*.md")):
        front = parse_front_matter(path.read_text())
        yield BadState(
            path, cast(Component, front["rot"]), parse_state(front["claims"])
        )


def load_good_states(root: Path = EXAMPLES) -> Iterator[GoodState]:
    for path in sorted((root / "good-states").glob("*.md")):
        front = parse_front_matter(path.read_text())
        yield GoodState(path, parse_state(front["claims"]))


def load_corners(root: Path = EXAMPLES) -> Iterator[Corner]:
    for path in sorted((root / "corners").glob("*.md")):
        front = parse_front_matter(path.read_text())
        verdicts = cast(Mapping[Condition, bool], front["verdicts"])
        yield Corner(path, verdicts, parse_state(front["claims"]))
