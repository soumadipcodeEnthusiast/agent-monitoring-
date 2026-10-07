from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_hypotheses():
    return []

@router.get("/{id}")
def get_hypothesis(id: str):
    return {"id": id, "status": "TESTING"}
