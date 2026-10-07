from pydantic import BaseModel

class EvaluationResult(BaseModel):
    success: bool
    failure_class: str

class AgentEvaluator:
    def evaluate(self, task: str, result: dict) -> EvaluationResult:
        return EvaluationResult(success=result.get("success", True), failure_class="NONE")
