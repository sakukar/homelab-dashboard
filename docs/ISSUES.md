# Planned issue catalog

**Planning only; application implementation is not authorized.**

This catalog covers the HomeLab Dashboard target application, not its separate agent orchestrator. See [the project plan](PROJECT_PLAN.md) for confirmed requirements, proposed defaults, unresolved decisions and release gates.

Total: **39 issues** (36 new planning items and the three existing issues refined). Every issue is open/planned; existing PRs are unaccepted candidate work.

Dependencies mean accepted prerequisite outputs, not merely a closed ticket. An explicitly dropped optional feature requires a documented scope decision and dependency update. Phase order and implementation authorization remain separate constraints.

Confirmed: **Finnish UI on a standard computer monitor**. Exact display specifications remain open. Deployment method and integration device versions are intentionally deferred to their relevant tasks; they do not block current planning or mock-data design.

## Overview

| Plan ID | GitHub | Task | Depends on |
| --- | --- | --- | --- |
| P0-01 | [#7](https://github.com/sakukar/homelab-dashboard/issues/7) | Confirm scope, deployment assumptions and implementation gate | — |
| P0-02 | [#8](https://github.com/sakukar/homelab-dashboard/issues/8) | Specify the dashboard API and data semantics | P0-01 |
| P0-03 | [#9](https://github.com/sakukar/homelab-dashboard/issues/9) | Specify kiosk layout, screen states and visual acceptance | P0-01, P0-02 |
| P1-01 | [#1](https://github.com/sakukar/homelab-dashboard/issues/1) | Initialize FastAPI backend | P0-01 |
| P1-02 | [#2](https://github.com/sakukar/homelab-dashboard/issues/2) | Initialize React frontend | P0-01 |
| P1-03 | [#3](https://github.com/sakukar/homelab-dashboard/issues/3) | Define the validated Server model | P0-02, P1-01 |
| P1-04 | [#10](https://github.com/sakukar/homelab-dashboard/issues/10) | Provide deterministic mock dashboard scenarios | P0-02, P1-03 |
| P1-05 | [#11](https://github.com/sakukar/homelab-dashboard/issues/11) | Expose the mock dashboard snapshot API | P1-01, P1-04 |
| P1-06 | [#12](https://github.com/sakukar/homelab-dashboard/issues/12) | Render server cards and resource overview | P1-02, P1-03, P0-03 |
| P1-07 | [#13](https://github.com/sakukar/homelab-dashboard/issues/13) | Connect dashboard refresh and failure recovery | P1-05, P1-06 |
| P1-08 | [#14](https://github.com/sakukar/homelab-dashboard/issues/14) | Render the mock weather card | P1-07, P0-03 |
| P1-09 | [#15](https://github.com/sakukar/homelab-dashboard/issues/15) | Complete the fullscreen kiosk layout | P1-06, P1-08, P0-03 |
| P1-10 | [#16](https://github.com/sakukar/homelab-dashboard/issues/16) | Establish reproducible CI and test commands | P1-01, P1-02 |
| P1-11 | [#17](https://github.com/sakukar/homelab-dashboard/issues/17) | Document and package the selected deployment | P1-05, P1-09, P0-01 |
| P1-12 | [#18](https://github.com/sakukar/homelab-dashboard/issues/18) | Accept the version 0.1 mock dashboard | P1-03, P1-04, P1-07, P1-08, P1-09, P1-10, P1-11 |
| P2-01 | [#19](https://github.com/sakukar/homelab-dashboard/issues/19) | Inventory real servers and choose monitoring access | P1-12 |
| P2-02 | [#20](https://github.com/sakukar/homelab-dashboard/issues/20) | Implement the selected real server collector | P2-01, P1-03 |
| P2-03 | [#21](https://github.com/sakukar/homelab-dashboard/issues/21) | Schedule bounded collection and retain latest snapshots | P2-02, P1-05 |
| P2-04 | [#22](https://github.com/sakukar/homelab-dashboard/issues/22) | Monitor explicitly configured important services | P2-01, P2-03 |
| P2-05 | [#23](https://github.com/sakukar/homelab-dashboard/issues/23) | Display and accept real server and service monitoring | P2-03, P2-04, P1-12 |
| P3-01 | [#24](https://github.com/sakukar/homelab-dashboard/issues/24) | Specify Proxmox compatibility and identity mapping | P2-05 |
| P3-02 | [#25](https://github.com/sakukar/homelab-dashboard/issues/25) | Collect Proxmox node and guest observations | P3-01, P2-03 |
| P3-03 | [#26](https://github.com/sakukar/homelab-dashboard/issues/26) | Display and accept Proxmox host and guest status | P3-02, P2-05 |
| P4-01 | [#27](https://github.com/sakukar/homelab-dashboard/issues/27) | Specify pfSense, WAN, backup WAN and VPN sources | P2-05 |
| P4-02 | [#28](https://github.com/sakukar/homelab-dashboard/issues/28) | Collect pfSense gateway and VPN status | P4-01, P2-03 |
| P4-03 | [#29](https://github.com/sakukar/homelab-dashboard/issues/29) | Render and accept WAN, backup WAN and VPN overview | P4-02, P2-05 |
| P5-01 | [#30](https://github.com/sakukar/homelab-dashboard/issues/30) | Specify MikroTik devices and interface measurements | P2-05 |
| P5-02 | [#31](https://github.com/sakukar/homelab-dashboard/issues/31) | Collect MikroTik device and interface status | P5-01, P2-03 |
| P5-03 | [#32](https://github.com/sakukar/homelab-dashboard/issues/32) | Render and accept MikroTik network status | P5-02, P4-03 |
| P6-01 | [#33](https://github.com/sakukar/homelab-dashboard/issues/33) | Select weather, camera and household information sources | P1-12 |
| P6-02 | [#34](https://github.com/sakukar/homelab-dashboard/issues/34) | Replace mock weather with the selected live provider | P6-01, P1-08, P2-03 |
| P6-03 | [#35](https://github.com/sakukar/homelab-dashboard/issues/35) | Add the approved camera view | P6-01, P1-09, P1-11 |
| P6-04 | [#36](https://github.com/sakukar/homelab-dashboard/issues/36) | Implement the first explicitly selected household widget | P6-01, P1-09 |
| P7-01 | [#37](https://github.com/sakukar/homelab-dashboard/issues/37) | Specify history retention and alert semantics | P2-05 |
| P7-02 | [#38](https://github.com/sakukar/homelab-dashboard/issues/38) | Persist observations with bounded retention | P7-01, P2-03 |
| P7-03 | [#39](https://github.com/sakukar/homelab-dashboard/issues/39) | Expose and display bounded historical views | P7-02, P1-09 |
| P7-04 | [#40](https://github.com/sakukar/homelab-dashboard/issues/40) | Evaluate and persist deduplicated alert transitions | P7-01, P7-02 |
| P7-05 | [#41](https://github.com/sakukar/homelab-dashboard/issues/41) | Render active and recovered alerts | P7-03, P7-04 |
| P7-06 | [#42](https://github.com/sakukar/homelab-dashboard/issues/42) | Complete cross-source and operational acceptance | P7-05, P3-03, P4-03, P5-03, P6-02, P6-03, P6-04 |

## Detailed work items

### P0-01 — Confirm scope, deployment assumptions and implementation gate

[GitHub issue #7](https://github.com/sakukar/homelab-dashboard/issues/7)

Dependencies: None

Decision blockers: record D01–D05 and D13 with confirmed/proposed/deferred status; deferred deployment details are resolved in P1-11

Document the target-project/orchestrator boundary, version 0.1 requirements, display inventory, language, deployment and access decisions. Audit the premature PRs without merging them.

**Acceptance criteria**

- [ ] User decisions are recorded with proposed defaults clearly distinguished from confirmed requirements.
- [ ] All roadmap phases have linked issues with dependencies and acceptance criteria; no unassigned roadmap feature is implicitly authorized.
- [ ] PRs #4–#6 are recorded as unaccepted candidate work; discrepancies and their disposition are documented.
- [ ] The separate implementation-authorization requirement is documented; closing this planning issue does not grant authorization.

**Verification:** Review the complete issue catalog for missing requirements, dependency cycles and contradictory scope. Record the planning decision and explicit implementation authorization when they occur.

**Out of scope:** Application code, orchestrator implementation, PR merging and infrastructure changes.

**Confirmed requirements and deferred decisions:** Confirmed: the UI language is Finnish and the display is a standard computer monitor. Exact resolution, size, orientation and browser remain open. The user cannot choose deployment or provide integration device versions yet. Record these as deferred decisions, not prerequisites for completing current planning. Deployment is assessed in P1-11; source versions are discovered in P2-01/P3-01/P4-01/P5-01 before their live adapters.


### P0-02 — Specify the dashboard API and data semantics

[GitHub issue #8](https://github.com/sakukar/homelab-dashboard/issues/8)

Dependencies: P0-01

Decision blockers: Load meaning, memory/disk aggregation, refresh and freshness policy

Write a versioned contract for GET /api/v1/dashboard, including server identity, availability, observation times, mock/live mode, weather and source health. Reconcile PR #6 with the chosen contract before further model work.

**Acceptance criteria**

- [ ] Document stable IDs, nullable values, UTC timestamps, load semantics, percentage units and online/offline/unknown mapping.
- [ ] Supply complete healthy, empty, partial, missing, stale and failed-source JSON examples plus API-wide error responses.
- [ ] Confirm proposed 10-second refresh, 5-second request timeout and 30-second freshness threshold or replace them explicitly.
- [ ] Define backwards-compatible extension rules and distinguish process liveness from monitored-source health.

**Verification:** Review example payloads against a field-by-field schema and a status/freshness truth table; verify that host down, permission error and old observations remain distinct.

**Out of scope:** Endpoint implementation, live collectors and database selection.

**Confirmed requirements and deferred decisions:** The UI language is confirmed as Finnish. API field names and machine status codes may stay English; specify their Finnish presentation consistently with P0-03. Deployment choice and actual integration versions are not required for the mock-data contract.


### P0-03 — Specify kiosk layout, screen states and visual acceptance

[GitHub issue #9](https://github.com/sakukar/homelab-dashboard/issues/9)

Dependencies: P0-01, P0-02

Decision blockers: D01–D03

Create a reviewable layout specification for the target display, server cards, mock weather, freshness and source errors, including agreed copy and overflow behavior.

**Acceptance criteria**

- [ ] Define layouts for empty, one, six/proposed maximum and overflow inventories, with long names and unavailable fields.
- [ ] Specify labeled UP/DOWN/UNKNOWN and stale/error presentation using text as well as color.
- [ ] Record agreed resolutions, language, time format, readable typography and the difference between browser kiosk mode and optional in-app fullscreen.
- [ ] Document first load, recovery, partial data and unavailable weather states.

**Verification:** Walk through every contract scenario against the layout specification and record user decisions on display count and overflow.

**Out of scope:** React implementation, image generation requirements, administration controls and real monitoring.

**Confirmed requirements and deferred decisions:** Design for a standard computer monitor with Finnish user-visible text, including status, loading, empty and error states. Exact resolution, size, orientation and browser are not confirmed. 1920×1080 and 1280×720 are proposed test viewports only. Agree the final display acceptance later; do not present these proposals as known hardware.


### P1-01 — Initialize FastAPI backend

[GitHub issue #1](https://github.com/sakukar/homelab-dashboard/issues/1)

Dependencies: P0-01

Decision blockers: Review existing PR #4

Review and adapt the existing backend scaffold: installable Python package, FastAPI app, GET /health, isolated development environment and pytest setup. Document the repository boundary; do not build the legacy orchestrator placeholders.

**Acceptance criteria**

- [ ] A clean checkout installs reproducibly using the documented dependency lock and supported Python version.
- [ ] GET /health returns HTTP 200 and the documented JSON liveness response.
- [ ] Tests run from documented commands without requiring real devices, credentials or a running external service.
- [ ] Setup and shutdown instructions are accurate; existing PR #4 is reviewed against this scope.

**Verification:** Run a clean dependency installation, the health endpoint test and an HTTP startup smoke check. Record dependency warnings with their impact.

**Out of scope:** Dashboard snapshot endpoint, collectors, persistence and orchestrator code.

### P1-02 — Initialize React frontend

[GitHub issue #2](https://github.com/sakukar/homelab-dashboard/issues/2)

Dependencies: P0-01

Decision blockers: Review existing PR #5

Review and adapt the existing React + TypeScript + Vite scaffold, including dependency lock, development commands, lint and production build.

**Acceptance criteria**

- [ ] A clean checkout installs with npm ci using a documented supported Node.js version.
- [ ] The application mounts successfully with the HomeLab Dashboard title and a clear initial empty state.
- [ ] Lint, TypeScript checking and production build pass; generated output and dependencies stay out of Git.
- [ ] Documentation describes the scaffold accurately and does not claim working live monitoring.

**Verification:** Run npm ci, npm run lint and npm run build; open the application and check for startup console errors.

**Out of scope:** Live integration, full dashboard behavior and orchestrator UI.

**Confirmed requirements and deferred decisions:** The UI language is confirmed as Finnish, including the initial empty state and later status/error text. The target is a standard computer monitor; no specific resolution or browser is confirmed. Review the existing English scaffold when implementation is separately authorized.


### P1-03 — Define the validated Server model

[GitHub issue #3](https://github.com/sakukar/homelab-dashboard/issues/3)

Dependencies: P0-02, P1-01

Decision blockers: Contract from P0-02; review existing PR #6

Review and adapt the initial Server model to the accepted contract, including stable identity, observation time, status, CPU, memory, disk, load and load averages.

**Acceptance criteria**

- [ ] All required contract fields and documented units serialize consistently; unknown measurements remain null rather than zero.
- [ ] Finite bounds, required identity, timestamps and supported status values are validated.
- [ ] Load meaning and disk/memory semantics match the approved contract rather than inheriting provisional PR #6 assumptions.
- [ ] Existing PR #6 is reviewed and its base dependency on PR #4 is handled before acceptance.

**Verification:** Model tests cover valid snapshots, JSON round trips, null/zero distinction, invalid ranges and timestamps, stable IDs and unknown status.

**Out of scope:** Data collection, database tables and unapproved model fields.

### P1-04 — Provide deterministic mock dashboard scenarios

[GitHub issue #10](https://github.com/sakukar/homelab-dashboard/issues/10)

Dependencies: P0-02, P1-03

Decision blockers: Accepted API contract

Create a mock source for server and weather snapshots with deterministic scenario selection and injectable time.

**Acceptance criteria**

- [ ] Include healthy, down, unknown, missing measurements, empty inventory, stale, high-usage and partial-source scenarios.
- [ ] Repeated runs with the same scenario and clock give the same identities and values.
- [ ] Mock mode is included in the snapshot and needs no network access or secrets.
- [ ] Fixture selection is documented; malformed fixture/configuration fails clearly.

**Verification:** Validate every fixture against the contract and assert the expected status, freshness and null semantics with a controlled clock.

**Out of scope:** Real devices, random data generation and production failure-control endpoints.

### P1-05 — Expose the mock dashboard snapshot API

[GitHub issue #11](https://github.com/sakukar/homelab-dashboard/issues/11)

Dependencies: P1-01, P1-04

Decision blockers: Accepted API routes and error contract

Implement GET /api/v1/dashboard using the deterministic mock source and the agreed response model.

**Acceptance criteria**

- [ ] Healthy, empty and partial snapshots conform to the documented schema.
- [ ] Source-level failures return usable partial data; application-wide errors have the documented HTTP/error shape.
- [ ] Observation times and mock/live identity are preserved rather than refreshed merely by serving a request.
- [ ] API documentation and local access instructions describe the endpoint and supported scenarios.

**Verification:** HTTP tests cover each scenario, schema shape, content type, observation-time stability and application failure handling.

**Out of scope:** Live collectors, edit endpoints and browser rendering.

### P1-06 — Render server cards and resource overview

[GitHub issue #12](https://github.com/sakukar/homelab-dashboard/issues/12)

Dependencies: P1-02, P1-03, P0-03

Decision blockers: Accepted layout and contract

Build the dashboard shell and server/resource components using contract fixtures before connecting the refresh loop.

**Acceptance criteria**

- [ ] Show stable server identity, labeled availability and CPU/RAM/disk with correct units.
- [ ] Missing values render as unavailable and stale values are distinguishable from current values.
- [ ] Empty, one, maximum-count and overflow layouts match the agreed specification; long names do not break the screen.
- [ ] Any aggregate shown has a documented calculation; do not invent meaningless averages.

**Verification:** Component checks cover labels, units, null versus zero, all availability states and long/overflow inventory; run lint and production build.

**Out of scope:** Network refresh logic, editable infrastructure controls and live metrics.

### P1-07 — Connect dashboard refresh and failure recovery

[GitHub issue #13](https://github.com/sakukar/homelab-dashboard/issues/13)

Dependencies: P1-05, P1-06

Decision blockers: Confirmed refresh, timeout and stale policy

Connect the frontend to the snapshot endpoint with a bounded refresh loop and explicit loading, ready, empty, partial, error and recovery states.

**Acceptance criteria**

- [ ] Only one active refresh request exists per mounted view and requests/timers are cleaned up when it unmounts.
- [ ] Failed refreshes retain the last good data with visible failure/freshness indicators.
- [ ] Timeouts, invalid responses and stale observations cannot masquerade as fresh UP status.
- [ ] Recovery clears transient errors and late responses cannot overwrite newer state.

**Verification:** Use controlled clocks and mocked HTTP responses for first load, overlapping/late response prevention, timeout, failure, stale transition and recovery; run frontend lint/build.

**Out of scope:** WebSockets, server-sent events, live collectors and unlimited retries.

### P1-08 — Render the mock weather card

[GitHub issue #14](https://github.com/sakukar/homelab-dashboard/issues/14)

Dependencies: P1-07, P0-03

Decision blockers: D02; location-independent mock weather contract

Add the version 0.1 weather card using weather data from the same mock snapshot API.

**Acceptance criteria**

- [ ] Show the fixture location, temperature/unit, condition and observation age using agreed localization.
- [ ] Missing or stale weather has a defined presentation without hiding server cards.
- [ ] The dashboard visibly identifies mock data.
- [ ] No external weather request or API key is required.

**Verification:** Component/browser checks cover normal, missing and stale weather plus locale/units; run lint and production build.

**Out of scope:** Weather-provider selection, real forecasts and live credentials.

### P1-09 — Complete the fullscreen kiosk layout

[GitHub issue #15](https://github.com/sakukar/homelab-dashboard/issues/15)

Dependencies: P1-06, P1-08, P0-03

Decision blockers: D01–D03 confirmed

Apply the accepted screen layout and overflow behavior across the agreed target and fallback resolutions.

**Acceptance criteria**

- [ ] The agreed card count and weather fit the target screen without accidental clipping or scrolling.
- [ ] Fallback resolutions, long labels and partial/error states remain usable.
- [ ] Reload/recovery does not need keyboard input; optional fullscreen behavior handles rejection and exiting correctly.
- [ ] Document browser kiosk startup separately from application fullscreen behavior.

**Verification:** Run browser layout checks at agreed resolutions and manually review the actual display for readability, labels and overflow; run lint/build.

**Out of scope:** Operating-system kiosk provisioning beyond the selected runbook, animation-heavy redesign and arbitrary extra widgets.

### P1-10 — Establish reproducible CI and test commands

[GitHub issue #16](https://github.com/sakukar/homelab-dashboard/issues/16)

Dependencies: P1-01, P1-02

Decision blockers: Selected supported runtime versions

Add focused CI checks for backend tests and frontend lint/typecheck/build, with an established command for later component/browser checks.

**Acceptance criteria**

- [ ] Checks run from a clean checkout with locked dependencies and documented runtime versions.
- [ ] Backend and frontend failures fail their corresponding jobs and expose actionable output.
- [ ] Routine CI uses fixtures only and requires no home-lab credentials or live devices.
- [ ] Verification commands and local equivalents are documented; branch rules are proposed rather than changed silently.

**Verification:** Run the exact CI commands locally and verify an actual workflow run when the workflow PR is created; record command/job results.

**Out of scope:** Orchestrator automation, automatic merging/deployment and broad repository permission changes.

### P1-11 — Document and package the selected deployment

[GitHub issue #17](https://github.com/sakukar/homelab-dashboard/issues/17)

Dependencies: P1-05, P1-09, P0-01

Decision blockers: D04–D05 must be resolved

Provide one supported deployment path, configuration example and operations runbook for the mock dashboard on the chosen host.

**Acceptance criteria**

- [ ] A clean target can start the backend/frontend using documented commands and a mock-only default.
- [ ] Browser-to-API routing works with the selected origin/proxy configuration; required bindings and access controls are explicit.
- [ ] Start, stop, restart/reboot, logs, configuration errors and recovery are covered.
- [ ] No secret values are committed; production and local-development settings are distinguished.

**Verification:** Exercise the runbook on the chosen target or matching clean environment, including reboot/restart and browser API access.

**Out of scope:** Supporting multiple competing deployment stacks, cloud deployment and automatic installation on unrelated hosts.

**Confirmed requirements and deferred decisions:** The installation method is intentionally undecided because the user cannot choose it at this stage. Begin this task by assessing the eventual host, comparing suitable deployment options and recording one selected path before packaging. Do not assume Docker, systemd, a host OS or architecture. This decision does not block current planning or the mock-data design.


### P1-12 — Accept the version 0.1 mock dashboard

[GitHub issue #18](https://github.com/sakukar/homelab-dashboard/issues/18)

Dependencies: P1-03, P1-04, P1-07, P1-08, P1-09, P1-10, P1-11

Decision blockers: D01–D05 and P0 decisions resolved

Run and record the complete version 0.1 acceptance matrix and confirm that the target project is ready for later live-source phases.

**Acceptance criteria**

- [ ] Healthy, down, unknown, empty, partial, stale, timeout and recovery scenarios pass end to end.
- [ ] Clean install, CI, production build and the documented deployment work with no external services.
- [ ] An agreed soak test (proposed eight hours) on the target display records no crash or steadily increasing requests/memory.
- [ ] README accurately lists delivered behavior and remaining phases; acceptance evidence and remaining defects are linked.

**Verification:** Record commands, browser/device/resolution, scenario results and soak observations. Resolve release-blocking defects before marking accepted.

**Out of scope:** Live-source implementation, automatic PR merging and orchestrator validation.

### P2-01 — Inventory real servers and choose monitoring access

[GitHub issue #19](https://github.com/sakukar/homelab-dashboard/issues/19)

Dependencies: P1-12

Decision blockers: D06 and relevant D04–D05

Record supported server OS/versions, physical/VM identity, required metrics, filesystem choices and available read-only monitoring interfaces. Select the smallest viable collector approach.

**Acceptance criteria**

- [ ] Every initial target has an alias, kind, OS/version and intended measurement source.
- [ ] An approved access method, metric definitions, permissions and configuration shape are documented.
- [ ] Unsupported metrics remain explicitly unavailable and disk/memory aggregation is defined.
- [ ] Representative sanitized source fixtures and a compatibility/test matrix are specified.

**Verification:** Review the selected interface against primary documentation for installed versions and confirm read-only availability on an explicitly configured test target.

**Out of scope:** Unrequested agent installation, broad network scanning and supporting every operating system.

**Confirmed requirements and deferred decisions:** The user does not know the target server versions at this stage. This discovery task owns collecting the actual OS/interface inventory later; dependent live collector work remains blocked until it is known. Unknown versions do not block current planning or mock-data work.


### P2-02 — Implement the selected real server collector

[GitHub issue #20](https://github.com/sakukar/homelab-dashboard/issues/20)

Dependencies: P2-01, P1-03

Decision blockers: Approved collector interface and targets

Map one selected server monitoring interface into the normalized Server snapshot, keeping mock mode usable.

**Acceptance criteria**

- [ ] CPU/memory/disk/load/time/identity map to the approved definitions and units.
- [ ] Missing/unsupported metrics, unreachable hosts, authentication failures and invalid responses are handled distinctly.
- [ ] Connections have bounded timeouts and output/logs exclude credentials.
- [ ] Compatibility is documented for the actual supported OS/interface versions.

**Verification:** Use sanitized fixtures for successful and failing responses, unit conversions and null handling, followed by a read-only smoke test against the configured target.

**Out of scope:** Polling scheduler, automatic source discovery and unrelated operating-system support.

### P2-03 — Schedule bounded collection and retain latest snapshots

[GitHub issue #21](https://github.com/sakukar/homelab-dashboard/issues/21)

Dependencies: P2-02, P1-05

Decision blockers: Poll cadence, stale thresholds and concurrency limits

Introduce source scheduling and in-memory latest-value ownership so HTTP requests consume snapshots instead of blocking on infrastructure calls.

**Acceptance criteria**

- [ ] One slow/failed source does not stop others or delay the dashboard request path.
- [ ] Per-source polling does not overlap; concurrency, timeouts and retry/backoff are bounded.
- [ ] Startup/shutdown, disabled sources and last-success/stale transitions have defined behavior.
- [ ] Restart behavior is documented and mock mode still runs without live configuration.

**Verification:** Controlled-clock tests cover independent sources, failure/backoff/recovery, shutdown cancellation and stale transitions; exercise concurrent API requests during a slow collection.

**Out of scope:** Persistent history, distributed scheduling, message brokers and orchestrator execution.

### P2-04 — Monitor explicitly configured important services

[GitHub issue #22](https://github.com/sakukar/homelab-dashboard/issues/22)

Dependencies: P2-01, P2-03

Decision blockers: Service inventory and approved probe types

Add bounded read-only service checks for the agreed initial services, with checks separate from host availability.

**Acceptance criteria**

- [ ] Each service has a stable ID, display name, configured target and documented success criteria.
- [ ] Service UP/DOWN/UNKNOWN and observation time do not overwrite the parent host state.
- [ ] Timeout, rejected response and disabled/not-yet-observed states are distinguishable.
- [ ] Only explicitly configured destinations are checked; no browser-supplied arbitrary probe target.

**Verification:** Use local test servers/fixtures for success, error, timeout and recovery and verify scheduling isolation and sanitized diagnostics.

**Out of scope:** Port scanning, arbitrary network administration and external alert delivery.

### P2-05 — Display and accept real server and service monitoring

[GitHub issue #23](https://github.com/sakukar/homelab-dashboard/issues/23)

Dependencies: P2-03, P2-04, P1-12

Decision blockers: Approved live targets and freshness policy

Expose and render real server/service observations through the existing dashboard contract and verify live-mode behavior.

**Acceptance criteria**

- [ ] Mock/live mode is explicit and server/service failures are individually visible.
- [ ] Disconnecting one configured test source produces correct error/stale behavior while others keep updating.
- [ ] Recovery updates observation age and labels correctly without a page reload.
- [ ] Configuration and operational instructions cover supported targets and limitations.

**Verification:** Run fixture-based API/component/browser checks plus the agreed read-only real-target disconnect/reconnect acceptance; run backend tests and frontend lint/build.

**Out of scope:** Proxmox-specific guest discovery, network-device integrations and history.

### P3-01 — Specify Proxmox compatibility and identity mapping

[GitHub issue #24](https://github.com/sakukar/homelab-dashboard/issues/24)

Dependencies: P2-05

Decision blockers: D07

Discover installed Proxmox versions, nodes, clusters and guest types; select required read-only endpoints and map host/VM/container identity.

**Acceptance criteria**

- [ ] Installed versions and required endpoint permissions are recorded from primary documentation.
- [ ] Node and guest IDs cannot collide with existing server IDs; parent relationships and duplicate-source ownership are defined.
- [ ] Stopped guests, unavailable nodes and missing metrics have explicit mappings.
- [ ] Sanitized response fixtures and a minimal acceptance target are available.

**Verification:** Review endpoint permission requirements and confirm chosen test access without issuing infrastructure-control operations.

**Out of scope:** VM power control, cluster configuration and unsupported-version promises.

**Confirmed requirements and deferred decisions:** The installed Proxmox version is intentionally unknown at this stage. Discover and verify it in this task before selecting endpoints and implementing the adapter; no version compatibility is promised in advance.


### P3-02 — Collect Proxmox node and guest observations

[GitHub issue #25](https://github.com/sakukar/homelab-dashboard/issues/25)

Dependencies: P3-01, P2-03

Decision blockers: Approved Proxmox contract

Implement the version-compatible Proxmox source adapter and register it with the existing scheduler.

**Acceptance criteria**

- [ ] Selected node and VM/container metrics map to stable IDs, parent identity, units and observation times.
- [ ] Partial node failure, permission errors, stopped guests and malformed responses do not destroy healthy observations.
- [ ] Pagination/filtering where required and bounded timeouts follow the selected API contract.
- [ ] Mock and generic server sources remain usable; overlapping observations have deterministic ownership.

**Verification:** Fixture contract/error tests and a read-only smoke test against the approved Proxmox target.

**Out of scope:** VM creation/start/stop, host administration and new scheduling infrastructure.

### P3-03 — Display and accept Proxmox host and guest status

[GitHub issue #26](https://github.com/sakukar/homelab-dashboard/issues/26)

Dependencies: P3-02, P2-05

Decision blockers: Agreed grouping/overflow behavior

Extend the display to distinguish Proxmox hosts and guests and make parent relationships understandable.

**Acceptance criteria**

- [ ] Host, VM and container identities/types are clear without duplicating the same entity.
- [ ] Stopped guest versus unreachable source is distinguishable.
- [ ] Large guest inventories use the agreed overflow/grouping behavior.
- [ ] Partial failure and recovery preserve unrelated dashboard sections.

**Verification:** Component/browser checks for mixed inventory, stopped guests, long names and source failure; read-only real-target acceptance; frontend lint/build.

**Out of scope:** Interactive VM administration and unplanned guest-control actions.

### P4-01 — Specify pfSense, WAN, backup WAN and VPN sources

[GitHub issue #27](https://github.com/sakukar/homelab-dashboard/issues/27)

Dependencies: P2-05

Decision blockers: D08

Record installed pfSense edition/version and select supported read-only status access; define primary/backup gateway and VPN session semantics.

**Acceptance criteria**

- [ ] The access method is verified for the installed version; no assumed REST package dependency.
- [ ] Interface link, gateway reachability, active WAN route and VPN tunnel status are modeled separately.
- [ ] Primary outage, backup active, both unavailable and unknown-source cases have example snapshots.
- [ ] Required permissions, source cadence and sanitized fixtures are documented.

**Verification:** Review installed-version Netgate/interface documentation and confirm the selected fields on an approved read-only test target.

**Out of scope:** Firewall package installation, failover changes and routing/VPN configuration.

**Confirmed requirements and deferred decisions:** The installed pfSense edition/version is intentionally unknown at this stage. Discover and verify it in this task before selecting access and implementing the adapter; do not assume a REST package or particular edition.


### P4-02 — Collect pfSense gateway and VPN status

[GitHub issue #28](https://github.com/sakukar/homelab-dashboard/issues/28)

Dependencies: P4-01, P2-03

Decision blockers: Approved pfSense access method

Implement the selected read-only source for configured WAN, backup WAN and VPN observations.

**Acceptance criteria**

- [ ] All agreed network status dimensions map to the approved schema and observation times.
- [ ] Source failure yields unknown/stale data instead of an invented WAN-down conclusion.
- [ ] Partial responses and malformed/missing fields preserve usable observations.
- [ ] Timeout, credentials and scheduler isolation follow the existing collector rules.

**Verification:** Fixture tests for primary, backup, both-down, unknown, VPN failure and recovery; read-only target smoke check.

**Out of scope:** Triggering WAN failover, firewall/routing writes and VPN management.

### P4-03 — Render and accept WAN, backup WAN and VPN overview

[GitHub issue #29](https://github.com/sakukar/homelab-dashboard/issues/29)

Dependencies: P4-02, P2-05

Decision blockers: Network layout and status mappings

Add a concise network overview for the agreed WAN/backup/VPN entities without hiding server health.

**Acceptance criteria**

- [ ] Primary and backup availability and active-route selection are clearly labeled.
- [ ] Unknown/stale source data is not displayed as confirmed loss of internet.
- [ ] VPN states and last observation are readable at the target display size.
- [ ] Added cards preserve the agreed kiosk overflow and recovery behavior.

**Verification:** Fixture-driven browser checks cover the network scenario matrix and target resolution; run lint/build and read-only acceptance.

**Out of scope:** Failover buttons, network topology editor and configuration controls.

### P5-01 — Specify MikroTik devices and interface measurements

[GitHub issue #30](https://github.com/sakukar/homelab-dashboard/issues/30)

Dependencies: P2-05

Decision blockers: D09

Inventory RouterOS versions and important interfaces; select a supported read-only interface and normalize device/port metrics.

**Acceptance criteria**

- [ ] Device models, versions, source access and required permissions are recorded.
- [ ] Link state, throughput units, counters, sampling interval and counter-reset behavior are defined.
- [ ] Chosen interfaces and source identities are explicit; unknown values stay unavailable.
- [ ] Sanitized source fixtures and a supported-version matrix are documented.

**Verification:** Verify decisions against installed-version MikroTik documentation and approved read-only target observations.

**Out of scope:** RouterOS upgrades, automatic network discovery and device configuration changes.

**Confirmed requirements and deferred decisions:** The installed RouterOS versions and device models are intentionally unknown at this stage. Discover them in this task before choosing access and implementing the adapter; no version compatibility is promised in advance.


### P5-02 — Collect MikroTik device and interface status

[GitHub issue #31](https://github.com/sakukar/homelab-dashboard/issues/31)

Dependencies: P5-01, P2-03

Decision blockers: Approved RouterOS contract

Implement the selected MikroTik adapter using the established source scheduling and configuration conventions.

**Acceptance criteria**

- [ ] Configured devices and ports map to stable identities and observation times.
- [ ] Counter-derived rates handle reset, first sample and elapsed time correctly where throughput is in scope.
- [ ] Permission errors, malformed values, unavailable interfaces and source timeouts are explicit.
- [ ] No write operation is used and secrets are excluded from logs and browser data.

**Verification:** Fixture tests for status, units, counter reset/first sample/time gaps, failures and recovery plus approved read-only smoke test.

**Out of scope:** Router configuration, traffic shaping and packet capture.

### P5-03 — Render and accept MikroTik network status

[GitHub issue #32](https://github.com/sakukar/homelab-dashboard/issues/32)

Dependencies: P5-02, P4-03

Decision blockers: Agreed interface display and layout budget

Extend the network display with the selected MikroTik device/interface states and any approved throughput measurements.

**Acceptance criteria**

- [ ] Device/port identity, link state and units are clear and do not conflate WAN reachability with local link status.
- [ ] Unavailable/stale values are explicit and unrelated source sections remain usable.
- [ ] The agreed interface count fits the kiosk layout or uses its documented overflow behavior.
- [ ] Operations documentation lists supported devices and selected interfaces.

**Verification:** Component/browser fixtures for link up/down, rate reset, unknown and source recovery; target display review and frontend lint/build.

**Out of scope:** Topology editing, device control and unbounded interface lists.

### P6-01 — Select weather, camera and household information sources

[GitHub issue #33](https://github.com/sakukar/homelab-dashboard/issues/33)

Dependencies: P1-12

Decision blockers: D10–D11 and access boundary D05

Choose weather location/provider and camera mode/protocol; define which household widgets are actually wanted before implementation.

**Acceptance criteria**

- [ ] Weather fields, provider terms/attribution, cadence and location are documented.
- [ ] Camera source/count, snapshot-vs-video, browser compatibility and proxy requirements are decided.
- [ ] Each household widget has a bounded purpose, source, display budget and failure behavior; split additional widgets into separate issues before work.
- [ ] Provider credentials and private camera addresses have a configuration plan that does not expose secrets to the browser.

**Verification:** Check selected providers against their primary documentation and record supported source samples and decision outcomes.

**Out of scope:** Guessing household features, installing camera infrastructure and live adapter code.

### P6-02 — Replace mock weather with the selected live provider

[GitHub issue #34](https://github.com/sakukar/homelab-dashboard/issues/34)

Dependencies: P6-01, P1-08, P2-03

Decision blockers: Approved weather provider and location

Add the selected backend weather adapter and map it to the existing weather card contract while retaining mock mode.

**Acceptance criteria**

- [ ] Location, values, condition codes and observation times map correctly with agreed units/timezone.
- [ ] Provider attribution and refresh/cache behavior comply with the selected source requirements.
- [ ] Rate limiting, timeout, invalid response and stale last-good data are handled independently of server monitoring.
- [ ] Credentials stay server-side and mock mode remains deterministic.

**Verification:** Provider fixture tests, rate-limit/timeout recovery tests, weather component checks and one approved live read; frontend lint/build when changed.

**Out of scope:** Multiple providers, extra forecast features and replacing the server dashboard layout.

### P6-03 — Add the approved camera view

[GitHub issue #35](https://github.com/sakukar/homelab-dashboard/issues/35)

Dependencies: P6-01, P1-09, P1-11

Decision blockers: Approved camera mode/protocol/count

Implement only the agreed snapshot or video display path, including a bounded backend proxy if the chosen source requires one.

**Acceptance criteria**

- [ ] The selected format renders on the target browser and fits the agreed display budget.
- [ ] Unavailable/expired camera data is labeled and cannot block other widgets.
- [ ] Refresh/stream connections and cleanup are bounded; credentials do not appear in client URLs, markup or logs.
- [ ] Only configured cameras can be requested and deployment access restrictions cover camera content.

**Verification:** Test with a controlled fixture/media source for load, disconnect, reconnect and cleanup; verify the approved real camera and target browser.

**Out of scope:** Recording, facial recognition, camera movement/control and arbitrary URL proxying.

### P6-04 — Implement the first explicitly selected household widget

[GitHub issue #36](https://github.com/sakukar/homelab-dashboard/issues/36)

Dependencies: P6-01, P1-09

Decision blockers: Widget choice required; otherwise this issue remains blocked or is dropped

Implement one bounded household-information widget only after its purpose, data source, fields, update policy and layout are agreed in P6-01.

**Acceptance criteria**

- [ ] The selected widget and its exact fields replace this provisional scope before implementation starts.
- [ ] Loading/empty/stale/error behavior and any provider access/attribution are documented.
- [ ] The widget fits the existing display budget and has deterministic fixture coverage.
- [ ] If no widget is requested, record that decision and close as not planned instead of inventing a feature.

**Verification:** Add source/formatting and browser checks appropriate to the selected widget; run relevant backend tests and frontend lint/build.

**Out of scope:** Unspecified widgets, a generic widget marketplace and broad plugin systems.

### P7-01 — Specify history retention and alert semantics

[GitHub issue #37](https://github.com/sakukar/homelab-dashboard/issues/37)

Dependencies: P2-05

Decision blockers: D12

Decide which measurements/events are stored, retention and storage budgets, alert thresholds, hold times, clearing rules and display/delivery requirements.

**Acceptance criteria**

- [ ] Estimate storage from agreed entity counts, sample cadence and retention; select the smallest suitable store explicitly.
- [ ] Define UTC time windows, gaps, aggregation/downsampling, deletion and backup/recovery behavior.
- [ ] Define sustained threshold, DOWN, UNKNOWN, stale-source and recovery behavior to avoid alert flapping.
- [ ] Decide acknowledgement, severity and external notification destination; no destination means no external delivery.

**Verification:** Review worked examples for threshold crossings, missing data, restart and source recovery plus a capacity calculation.

**Out of scope:** Database implementation, arbitrary long-term retention and selecting notification channels without a decision.

### P7-02 — Persist observations with bounded retention

[GitHub issue #38](https://github.com/sakukar/homelab-dashboard/issues/38)

Dependencies: P7-01, P2-03

Decision blockers: Approved storage choice and data volume

Implement the selected history store, schema/migration path, bounded writes and retention cleanup without slowing snapshot serving.

**Acceptance criteria**

- [ ] Required metrics/events are stored with stable identity and observation time.
- [ ] Retention, cleanup and disk/storage failure behavior match the approved budget.
- [ ] Restart and duplicate observations have defined outcomes; collection/API paths remain responsive under storage failure.
- [ ] Backup/restore and any migration procedures are documented and reproducible.

**Verification:** Use an isolated test store for writes, duplicates, cleanup boundaries, restart/migration and failure injection; verify expected query performance at agreed scale.

**Out of scope:** Unlimited raw-data retention, unrelated analytics and distributed storage.

### P7-03 — Expose and display bounded historical views

[GitHub issue #39](https://github.com/sakukar/homelab-dashboard/issues/39)

Dependencies: P7-02, P1-09

Decision blockers: Agreed history ranges and kiosk interaction

Add bounded history queries and a focused historical view for the approved measurements and time ranges.

**Acceptance criteria**

- [ ] Queries validate entity, range and resolution and enforce limits on returned data.
- [ ] UTC storage and localized display agree at timezone/daylight-saving boundaries.
- [ ] Missing intervals are visible gaps rather than fabricated zero measurements.
- [ ] Chart/view layout remains readable and does not displace critical current status.

**Verification:** API tests for invalid/empty/bounded ranges and time boundaries; component/browser tests for gaps, units and large approved ranges; lint/build.

**Out of scope:** Ad-hoc query builders, unlimited exports and predictive analytics.

### P7-04 — Evaluate and persist deduplicated alert transitions

[GitHub issue #40](https://github.com/sakukar/homelab-dashboard/issues/40)

Dependencies: P7-01, P7-02

Decision blockers: Approved thresholds, hold times and recovery policy

Implement the agreed alert state machine over normalized observations with stable alert identity and persisted transitions.

**Acceptance criteria**

- [ ] Sustained threshold and source-availability rules use the approved hold and clearing semantics.
- [ ] Repeated observations do not create duplicate active alerts; flapping and unknown/stale input behave as specified.
- [ ] Restart restores active state consistently and recovery emits a single matching transition.
- [ ] Alert evaluation failures do not stop collection or dashboard snapshot serving.

**Verification:** Controlled-time sequences cover brief/sustained violations, repeated samples, gaps, stale data, recovery and restart deduplication.

**Out of scope:** Infrastructure remediation, changing monitored devices and notification delivery.

### P7-05 — Render active and recovered alerts

[GitHub issue #41](https://github.com/sakukar/homelab-dashboard/issues/41)

Dependencies: P7-03, P7-04

Decision blockers: Approved alert layout and acknowledgement policy

Render the agreed active/recovered alert states and their relationship to history. External notification delivery is a separate, unconfirmed scope decision.

**Acceptance criteria**

- [ ] Severity, affected entity, onset/recovery and any approved acknowledgement have clear behavior.
- [ ] Active alert counts and event/history views agree after restart and source recovery.
- [ ] Unknown, stale and recovering sources follow the approved alert semantics in the UI.
- [ ] An empty alert set, multiple alerts and long entity names fit the agreed kiosk layout.

**Verification:** Fixture-based component/browser tests cover active, cleared, empty, stale-source and restart/recovery cases; run frontend lint/build and relevant API tests.

**Out of scope:** External notification delivery, automatic remediation and unapproved acknowledgement actions.

### P7-06 — Complete cross-source and operational acceptance

[GitHub issue #42](https://github.com/sakukar/homelab-dashboard/issues/42)

Dependencies: P7-05, P3-03, P4-03, P5-03, P6-02, P6-03, P6-04

Decision blockers: Optional features explicitly selected or dropped; agreed target environment

Perform final cross-source acceptance and reconcile delivered behavior with the full roadmap and operations documentation.

**Acceptance criteria**

- [ ] Every roadmap feature is accepted or explicitly marked not planned; optional blocked work is never silently treated as delivered.
- [ ] Cross-source failure and recovery, bounded refresh, clean deployment and restart behavior pass on the supported environment.
- [ ] Retention, history, active alerts, source configuration and recovery runbooks agree with actual behavior.
- [ ] The agreed target-display soak, full verification suite and final limitations are recorded with linked evidence.

**Verification:** Run all relevant CI/build commands, the full source/failure matrix, retention/restart checks, deployment runbook and target-display soak. Link accepted or explicitly waived prerequisite outcomes.

**Out of scope:** New features, automatic PR merging, external messaging and orchestrator implementation.
