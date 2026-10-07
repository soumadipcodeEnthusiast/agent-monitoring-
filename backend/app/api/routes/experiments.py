from fastapi import APIRouter
from app.api.schemas import ExperimentCreate
from typing import List

router = APIRouter()

@router.get("/")
def get_experiments():
    return []

@router.post("/")
def create_experiment(exp: ExperimentCreate):
    return {"id": "test_exp_1", **exp.model_dump()}

@router.get("/{id}")
def get_experiment(id: str):
    return {"id": id, "status": "COMPLETED"}

@router.post("/{id}/run")
def run_experiment(id: str):
    return {"id": id, "status": "RUNNING"}
