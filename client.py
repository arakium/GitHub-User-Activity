"""HTTP client utilities for retrieving GitHub user activity data."""

from __future__ import annotations
from typing import Any, cast
import requests
from requests import status_codes

from models.event import Event
from models.repository import Repo
from models.user import User

JSON = dict[str, Any]
JSONArray = list[JSON]

class GitHubAPIError(Exception):
    """Exception handler"""
    def __init__(self, message: str, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code

class GitHubClient:
    """Wrapper around the GitHub REST API endpoints used by this CLI."""

    _BASE_URL = "https://api.github.com"
    _API_VERSION = "2022-11-28"

    def __init__(self, token) -> None:
        """Create a client session configured with authentication headers."""
        self.token: str = token
        self._session = requests.Session()
        self._session.headers.update({
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": self._API_VERSION
        })

    def _request(self, path: str) -> requests.Response:
        """Send a GET request to a GitHub API path and return the response."""
        url = f"{self._BASE_URL}{path}"

        try:
            response = self._session.get(url=url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as err:
            raise GitHubAPIError(f"GitHub API request to {path} failed: {err}",
            status_code=err.response.status_code if err.response else None) from err
        except requests.exceptions.RequestException as err:
            raise GitHubAPIError(f"Network error requesting: {path}: {err}") from err


    def get_user_events(self, username: str) -> list[Event]:
        """Fetch recent public events for a GitHub user."""
        events = cast(JSONArray, self._request(f"/users/{username}/events").json())
        return [Event.from_dict(event) for event in events]

    def get_user_info(self, username: str) -> User:
        """Fetch profile metadata for a GitHub user."""
        user_info = cast(JSON, self._request(f"/users/{username}").json())
        return User.from_dict(user_info)

    def get_user_repos(self, username: str) -> list[Repo]:
        """Fetch public repositories owned by a GitHub user."""
        repos = cast(JSONArray, self._request(f"/users/{username}/repos").json())
        return [Repo.from_dict(repo) for repo in repos]
