# GitHub User Activity

A Python CLI application that interacts with the GitHub REST API to retrieve public information about GitHub users.

## Features

- View user profile information
- View recent public events
- View public repositories
- Automatic JSON deserialization into Python dataclasses
- Pagination support for list endpoints
- Reusable `GitHubClient` for interacting with the GitHub API

## Requirements

- Python 3.11+
- A GitHub Personal Access Token

Create a `.env` file in the project root:

```env
GITHUB_KEY=your_github_personal_access_token
```

## Installation

```bash
git clone https://github.com/<your-username>/GitHub-User-Activity.git
cd GitHub-User-Activity

pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py <github-username>
```

Example:

```bash
python main.py torvalds
```

You'll then be prompted to choose one of the available actions:

```
1. User information
2. Recent events
3. Public repositories
```

## Project Structure

```
.
├── client.py
├── main.py
├── models/
│   ├── event.py
│   ├── repository.py
│   └── user.py
└── .env
```

## Project

This project is based on the roadmap.sh **GitHub User Activity** project:

https://roadmap.sh/projects/github-user-activity
