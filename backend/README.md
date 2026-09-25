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
