from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_failures():
    return []

@router.get("/patterns")
def get_failure_patterns():
    return []

@router.get("/{id}")
def get_failure(id: str):
    return {"id": id}
