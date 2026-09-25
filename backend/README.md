# Backend

Requires Python 3.12 or newer and [uv](https://docs.astral.sh/uv/).
Run these commands from `backend/`:

```sh
uv sync --extra dev --locked
uv run --extra dev uvicorn app.main:app --reload
```

The API listens on `http://127.0.0.1:8000`. `GET /health` returns
`{"status":"ok"}`. Interactive API documentation is at `/docs`.
The health endpoint checks process availability only.

Run tests:

```sh
uv run --extra dev pytest
```

## Server model

`app.models.Server` is a validated snapshot for future collectors and API routes.
It does not collect metrics or persist records yet.

| Field | Meaning |
| --- | --- |
| `name`, `hostname` | Required nonblank strings; surrounding whitespace is removed |
| `status` | `online`, `offline`, or `unknown` (default) |
| `cpu_usage` | Overall CPU utilization, 0–100 percent |
| `load` | Instantaneous runnable task count, a nonnegative integer |
| `load_average` | Object with `one_minute`, `five_minutes`, `fifteen_minutes` |
| `memory_usage` | Used memory, 0–100 percent |
| `disk_usage` | Used disk space, 0–100 percent |

All measurements default to `None` (JSON `null`) when unavailable. Load averages
must be finite and nonnegative; they are not percentages and may exceed 100.
All three averaging windows are required when `load_average` is supplied.
Memory and disk usage represent one server-level summary; per-disk details,
byte totals, and collector-specific aggregation are outside this initial model.
