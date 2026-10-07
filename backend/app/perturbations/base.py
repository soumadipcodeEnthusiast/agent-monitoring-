from abc import ABC, abstractmethod

class Perturbation(ABC):
    name: str
    category: str
    severity: float
    description: str

    def __init__(self, severity: float = 0.5):
        self.severity = severity

    @abstractmethod
    def apply(self, context: dict):
        pass
