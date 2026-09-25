from fastapi import FastAPI

app = FastAPI(title="HomeLab Dashboard")


@app.get("/health")
def health() -> dict[str, str]:
    """Report that the API process is responding."""
    return {"status": "ok"}
