from fastapi import APIRouter
from app.api.schemas import MetricOverview

router = APIRouter()

@router.get("/overview", response_model=MetricOverview)
def get_metrics_overview():
    return MetricOverview(
        total_experiments=100,
        failures_discovered=35,
        unique_failure_patterns=8,
        average_failure_boundary=0.65,
        recovery_rate=0.37,
        adaptive_advantage=1.8
    )

@router.get("/discovery")
def get_discovery_metrics():
    return {"random": [], "fixed": [], "adaptive": []}

@router.get("/boundaries")
def get_boundary_metrics():
    return {"boundaries": []}
