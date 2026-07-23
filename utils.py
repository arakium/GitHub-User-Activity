"""Shared helper functions used across GitHub API models and client code."""

from datetime import datetime

def parse_github_datetime(timestamp: str) -> datetime:
    """Convert a GitHub UTC timestamp string to a timezone-aware datetime."""
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))