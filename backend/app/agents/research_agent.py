from app.agents.base_agent import BaseAgent
from app.api.schemas import AgentRunResult
import uuid
from datetime import datetime

class ResearchAgent(BaseAgent):
    async def run(self, task: str) -> AgentRunResult:
        return AgentRunResult(
            success=True,
            final_answer="Research completed.",
            trace_id=str(uuid.uuid4())
        )
