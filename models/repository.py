"""Repository model used to deserialize GitHub repository payloads."""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any
from utils import parse_github_datetime

@dataclass
class Repo:
    """Represents a public repository returned by the GitHub API."""

    name: str
    owner: str
    description: str
    stars: int
    created_at: datetime
    updated_at: datetime
    pushed_at: datetime


    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Repo:
        """Build a Repo instance from a GitHub API repository object."""
        return cls(
            name = data["name"],
            owner = data["owner"]["login"],
            description = data["description"],
            stars = data["stargazers_count"],
            created_at = parse_github_datetime(data["created_at"]),
            updated_at = parse_github_datetime(data["updated_at"]),
            pushed_at = parse_github_datetime(data["pushed_at"])
        )
