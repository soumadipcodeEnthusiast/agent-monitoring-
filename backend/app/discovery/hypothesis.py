from pydantic import BaseModel
from typing import List

class Hypothesis(BaseModel):
    id: str
    description: str
    category: str
    confidence: float
    supporting_experiments: List[str] = []
    contradicting_experiments: List[str] = []
    status: str = "PROPOSED"
