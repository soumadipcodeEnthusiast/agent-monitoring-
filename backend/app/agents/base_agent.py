from app.agents.agent_interface import AgentInterface
from app.api.schemas import AgentRunResult
import uuid

class BaseAgent(AgentInterface):
    async def run(self, task: str) -> AgentRunResult:
        return AgentRunResult(success=True, final_answer="Mock answer", trace_id=str(uuid.uuid4()))
