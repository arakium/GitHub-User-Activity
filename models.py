"""Legacy Event model definition for GitHub event payloads."""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    """Represents a single public GitHub event."""

    actor: str
    type: str
    repo: str
    created_at: datetime

    @classmethod
    def from_dict(cls, data: dict) -> Event:
        """Build an Event instance from a GitHub API event object."""
        return cls(
            actor=data["actor"]["login"],
            type=data["type"],
            repo=data["repo"]["name"],
            created_at=data["created_at"]
        )