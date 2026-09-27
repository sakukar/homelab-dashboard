# HomeLab Dashboard

HomeLab Dashboard is a fullscreen web dashboard for monitoring a home lab and displaying additional information such as weather.

## Product scope

- This repository is a target application. The agent orchestrator is a separate project.
- Current status: planning only. Do not write application or orchestrator code until the user explicitly authorizes implementation after the project backlog is planned.
- Dashboard planning is paused by the user's 2026-09-27 decision to begin separate orchestrator planning. The Dashboard plan remains incomplete; S1–S8 are not accepted as satisfied and implementation is not authorized. Follow the remaining-work and return conditions in `docs/WORKFLOW.md`.
- The overall workflow has two stages: plan Dashboard as fully as possible without code, then work on the orchestrator and workers in their separate project to practise agentic coding. Dashboard implementation remains subject to separate user authorization.
- Use the planning completion criteria S1–S8 in `docs/WORKFLOW.md`. Plan acceptance and implementation authorization are separate decisions; roadmap phases 0–7 are not the two overall work stages.
- During Dashboard planning, produce documentation and non-executable layout specifications, not application code, test code or runnable prototypes.
- Confirmed: accommodate later features, data sources and monitoring targets. Plan extension scenarios, contract evolution and display growth; do not assume a fixed target count or an unapproved plugin framework.
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
- PRs #4–#6 were closed without merging. Their branches retain unaccepted candidate code for possible later review.
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

## Communication

- Explain progress to the user in Finnish and distinguish the target application from the separate orchestrator project.
- Before an authorized work phase, state its purpose and effects.
- After it, report the current branch, local changes, commit/push state, PR/merge state, remaining work and the next step.
- Never describe pushed work as visible on the default branch unless it has actually been merged there.
