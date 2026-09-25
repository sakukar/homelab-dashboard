# HomeLab Dashboard

HomeLab Dashboard is a fullscreen information display for a home lab.

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

The application is intended to run continuously on a dedicated information display.

## Initial scope

Version 0.1 will use mock data and include:

- FastAPI backend
- React + TypeScript frontend
- server status cards
- CPU, RAM and disk usage
- UP/DOWN status
- weather card
- fullscreen kiosk layout

Real integrations such as Proxmox, pfSense and MikroTik will be added later.
