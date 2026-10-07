from fastapi import FastAPI
from app.api.routes import agents, experiments, failures, hypotheses, metrics

app = FastAPI(
    title="Adaptive Failure Discovery Engine",
    description="Research-oriented system for discovering failure conditions in AI agents."
)

app.include_router(agents.router, prefix="/api/agents", tags=["agents"])
app.include_router(experiments.router, prefix="/api/experiments", tags=["experiments"])
app.include_router(failures.router, prefix="/api/failures", tags=["failures"])
app.include_router(hypotheses.router, prefix="/api/hypotheses", tags=["hypotheses"])
app.include_router(metrics.router, prefix="/api/metrics", tags=["metrics"])

@app.get("/")
def root():
    return {"message": "Adaptive Failure Discovery Engine API"}
