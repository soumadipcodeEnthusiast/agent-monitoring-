from abc import ABC, abstractmethod
from app.api.schemas import AgentRunResult

class AgentInterface(ABC):
    @abstractmethod
    async def run(self, task: str) -> AgentRunResult:
        pass
