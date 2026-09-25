# Frontend

Minimal React + TypeScript dashboard, built with Vite. Requires Node.js 24 LTS
and npm. From `frontend/`:

```sh
npm ci
npm run dev
```

Open the local URL printed by Vite (normally `http://localhost:5173`).
The initial dashboard shows an empty state; it does not fetch server data yet.
Resource measurements remain unavailable until a future API integration.

```sh
npm run lint
npm run build
npm run preview
```

`build` checks TypeScript and writes the production bundle to `dist/`.
`preview` serves that bundle locally for verification.
