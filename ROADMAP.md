# Roadmap

**Planning only.** This is the HomeLab Dashboard target-project roadmap.
The agent orchestrator is a separate project. Implementation starts only after
the backlog has been planned and the user separately authorizes execution.

See [the detailed plan](docs/PROJECT_PLAN.md) for decisions and acceptance rules,
and [the issue catalog](docs/ISSUES.md) for dependencies and GitHub links.
Phase numbers describe rollout order; they do not authorize work automatically.

| Phase | Scope | Work items | Exit criteria |
| --- | --- | --- | --- |
| 0 | Requirements, contract and display specification | P0-01–P0-03 | Version 0.1 decisions, contract examples and layout are agreed; full backlog exists; separate implementation authorization recorded before code starts |
| 1 / v0.1 | Mock-data dashboard | P1-01–P1-12 | Server cards, CPU/RAM/disk, UP/DOWN/UNKNOWN, mock weather, refresh/recovery and kiosk layout pass documented acceptance and deployment checks |
| 2 | Real server and important-service monitoring | P2-01–P2-05 | Approved server/service sources work with correct units, source isolation, stale states and recovery; mock mode remains usable |
| 3 | Proxmox | P3-01–P3-03 | Supported hosts and guests have stable identity and read-only observations; partial failures and stopped guests are displayed correctly |
| 4 | pfSense / WAN / backup WAN / VPN | P4-01–P4-03 | Approved source distinguishes link, gateway, active route and VPN states; no configuration writes |
| 5 | MikroTik | P5-01–P5-03 | Selected devices/interfaces display validated state and approved measurements with reset/failure handling |
| 6 | Live weather, camera and selected household information | P6-01–P6-04 | Selected sources meet their display/access/failure criteria; unspecified household widgets remain blocked or are explicitly dropped |
| 7 | Alerts, historical data and final acceptance | P7-01–P7-06 | Bounded retention, usable history and deterministic alert transitions pass restart/recovery and full-system acceptance |

Version 0.1 uses **mock data for both servers and weather**. It requires no real
monitoring source or weather credentials. The existing PRs are preliminary
scaffolds and do not mean that Phase 1 is complete.

Before each live integration, confirm the actual installed version, source access,
permissions and field mappings. External notification delivery is not yet a
confirmed requirement; if selected, plan it as a separate issue before coding.
No device control, remediation or infrastructure administration is implied.

The detailed issue graph determines technical prerequisites. A task can remain
blocked by an unresolved decision even if its prerequisite issues are closed.
Later-phase dependencies may be independent technically, but any change to the
rollout order or one-issue-at-a-time workflow must be explicitly agreed.

Confirmed: Finnish user interface on a standard computer monitor. Exact display
specifications remain open. Installation method and integration device versions
are deferred to the relevant deployment/discovery tasks; they do not block the
current planning work.
