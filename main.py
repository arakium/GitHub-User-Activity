"""CLI entry point for viewing GitHub user profile, events, and repositories."""

import argparse
import os

import requests
from dotenv import load_dotenv

from client import GitHubClient

load_dotenv()


def get_username() -> str:
    """Parse the GitHub username from the command line."""
    parser = argparse.ArgumentParser(
        prog="GitHub User Activity",
        description="Fetch information about a GitHub user.",
    )
    parser.add_argument(
        "username",
        help="GitHub username.",
    )

    return parser.parse_args().username


def print_user_info(client: GitHubClient, username: str) -> None:
    """Print basic information about a GitHub user."""
    user = client.get_user_info(username)

    print(f"Username      : {user.username}")
    print(f"Name          : {user.name}")
    print(f"Company       : {user.company}")
    print(f"Location      : {user.location}")
    print(f"Public Repos  : {user.public_repos}")
    print(f"Followers     : {user.followers}")
    print(f"Following     : {user.following}")


def print_user_events(client: GitHubClient, username: str) -> None:
    """Print a user's recent public events."""
    events = client.get_user_events(username)

    if not events:
        print("No recent public events.")
        return

    for event in events:
        print(
            f"{event.created_at:%Y-%m-%d %H:%M} | "
            f"{event.type:<20} | "
            f"{event.repo}"
        )


def print_user_repos(client: GitHubClient, username: str) -> None:
    """Print a user's public repositories."""
    repos = client.get_user_repos(username)

    if not repos:
        print("No public repositories.")
        return

    for repo in repos:
        print(
            f"{repo.name:<35} "
            f"★ {repo.stars:<5} "
            f"Updated: {repo.updated_at:%Y-%m-%d}"
        )


def choose_action() -> str:
    """Display menu options and return the selected action key."""
    print(
        "\n"
        "1. User information\n"
        "2. Recent events\n"
        "3. Public repositories\n"
    )

    return input("Select an option: ").strip()


def main() -> None:
    """Application entry point."""
    token = os.getenv("GITHUB_KEY")
    if token is None:
        raise RuntimeError("GITHUB_KEY environment variable is not set.")

    username = get_username()
    client = GitHubClient(token)

    actions = {
        "1": print_user_info,
        "2": print_user_events,
        "3": print_user_repos,
    }

    choice = choose_action()
    action = actions.get(choice)

    if action is None:
        print("Invalid option.")
        return

    try:
        action(client, username)

    except requests.HTTPError as e:
        if e.response is not None and e.response.status_code == 404:
            print(f"User '{username}' was not found.")
        else:
            print(f"HTTP error: {e}")

    except requests.RequestException as e:
        print(f"Network error: {e}")


if __name__ == "__main__":
    main()