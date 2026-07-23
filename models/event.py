"""Event model used to deserialize GitHub user event payloads."""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from utils import parse_github_datetime

@dataclass
class Event:
    """Represents a single public event performed by a GitHub user."""

    actor: str
    type: str
    repo: str
    created_at: datetime

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Event:
        """Build an Event instance from a GitHub API event object."""
        return cls(
            actor=data["actor"]["login"],
            type=data["type"],
            repo=data["repo"]["name"],
            created_at=parse_github_datetime(data["created_at"])
        )