# HomeLab Dashboard

HomeLab Dashboard is a fullscreen information display for a home lab.

## Project status: planning

This is the target application for a **separate agent-orchestrator project**.
The orchestrator itself is not developed in this repository.

The entire project is being planned and divided into issues before implementation
is authorized. An open issue or existing PR is not permission to begin coding.

- [Detailed project plan](docs/PROJECT_PLAN.md): requirements, proposed defaults,
  open decisions, architecture, contracts and acceptance gates.
- [Issue catalog](docs/ISSUES.md): task scope, dependencies and GitHub links.
- [Roadmap](ROADMAP.md): phase order and completion criteria.
- [Git-työnkulku ja eteneminen](docs/WORKFLOW.md): suomenkielinen ohje haaroista, PR:istä ja projektien etenemisestä.

## Goals

The dashboard should provide an at-a-glance view of:

- home network status
- servers and virtual machines
- CPU, memory and disk usage
- WAN and backup WAN status
- important services
- alerts and failures
- weather information
- other useful household information

The application is intended to run continuously on a standard computer monitor.
The user interface language is Finnish. Exact display specifications, deployment
method and integration device versions will be determined later.

## Initial scope

Version 0.1 targets Phase 1 of [the roadmap](ROADMAP.md). It will use mock
data for both server measurements and weather, and include:

- FastAPI backend
- React + TypeScript frontend
- server status cards
- CPU, RAM and disk usage
- UP/DOWN status
- weather card with mock data
- fullscreen kiosk layout

Real integrations such as Proxmox, pfSense and MikroTik will be added later.
Live weather data is also deferred to a later phase.

## Current implementation

PRs #4–#6 contain a FastAPI scaffold, React scaffold and provisional Server model
created before the planning scope was clarified. They were closed without merging
on 2026-09-27. Their code remains on `agent/issue-1`, `agent/issue-2` and
`agent/issue-3` for possible later review; it is not accepted implementation.
Planning documents are published separately from the `agent/issue-7` branch.

Mock server data, populated server cards, UP/DOWN display, failure/recovery
behavior and the mock weather card are planned work. The empty `orchestrator.py`
and `worker.py` files are legacy placeholders, not targets for implementation.
