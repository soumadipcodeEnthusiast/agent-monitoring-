from fastapi import APIRouter
from typing import List, Dict

router = APIRouter()

@router.get("/")
def get_agents():
    return [{"id": "1", "name": "Research Assistant Mock"}]

@router.post("/")
def create_agent(agent: dict):
    return agent

@router.get("/{id}")
def get_agent(id: str):
    return {"id": id, "name": "Research Assistant Mock"}
