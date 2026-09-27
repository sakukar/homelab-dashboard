# HomeLab Dashboard

HomeLab Dashboard is a fullscreen web dashboard for monitoring a home lab and displaying additional information such as weather.

## Product scope

- This repository is a target application. The agent orchestrator is a separate project.
- Current status: planning only. Do not write application or orchestrator code until the user explicitly authorizes implementation after the project backlog is planned.
- Read `README.md`, `ROADMAP.md`, `docs/PROJECT_PLAN.md`, and `docs/ISSUES.md` before planning or implementing changes.
- The UI language is Finnish, including status, error and empty-state messages. API identifiers may remain English.
- The target display is a standard computer monitor; do not treat a particular resolution or browser as confirmed.
- Deployment method and integration device versions are deferred decisions. Discover them in their relevant tasks rather than blocking current planning or guessing them.
- Version 0.1 is Phase 1: a fullscreen kiosk dashboard using mock server and weather data.
- The initial UI includes server status cards, CPU/RAM/disk usage, UP/DOWN status, and a mock weather card.
- Real server monitoring, Proxmox, pfSense/WAN/VPN, MikroTik, live weather, cameras, alerts, and history follow in later roadmap phases.
- Treat roadmap items as planned work, not authorization to implement additional features beyond the assigned issue.
- An open issue, satisfied dependencies, an existing PR, or a planning label is not implementation authorization.
- Distinguish confirmed requirements from proposed defaults and unresolved decisions. Resolve the decisions that block an issue before implementing it.
- Existing PRs #4–#6 are unaccepted candidate work and must be reviewed against the agreed plan.
- Do not implement `orchestrator.py` or `worker.py` in this repository.

## Architecture

Backend:
- Python
- FastAPI
- pytest

Frontend:
- React
- TypeScript
- Vite

## Development rules

- Work on only one GitHub issue at a time.
- Do not implement unrelated features.
- Keep changes focused and small.
- Run relevant tests before finishing.
- Run frontend build when frontend code is changed.
- Do not merge pull requests.
- Do not modify another agent's worktree.

## Git

Branch naming:

agent/issue-<number>

Example:

agent/issue-12

## Pull requests

- One issue per pull request.
- Mention the issue number in the PR.
- Summarize what was changed.
- Include test/build results.
