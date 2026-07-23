"""User model used to deserialize GitHub user profile payloads."""

from __future__ import annotations
from utils import parse_github_datetime
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class User:
    """Represents profile information for a GitHub user account."""

    username: str
    id: int
    node_id: str
    avatar_url: str
    html_url: str
    repos_url: str
    events_url: str
    type: str
    user_view_type: str
    name: str | None
    company: str | None
    blog: str
    location: str | None
    email: str | None
    hireable: bool | None
    bio: str | None
    twitter_username: str | None
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> User:
        """Build a User instance from a GitHub API user object."""
        return cls(
            username=data["login"],
            id=data["id"],
            node_id=data["node_id"],
            avatar_url=data["avatar_url"],
            html_url=data["html_url"],
            repos_url=data["repos_url"],
            events_url=data["events_url"],
            type=data["type"],
            user_view_type=data["user_view_type"],
            name=data["name"],
            company=data["company"],
            blog=data["blog"],
            location=data["location"],
            email=data["email"],
            hireable=data["hireable"],
            bio=data["bio"],
            twitter_username=data["twitter_username"],
            public_repos=data["public_repos"],
            public_gists=data["public_gists"],
            followers=data["followers"],
            following=data["following"],
            created_at=parse_github_datetime(data["created_at"]),
            updated_at=parse_github_datetime(data["updated_at"]),
        )