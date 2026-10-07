from abc import ABC, abstractmethod

class DiscoveryStrategy(ABC):
    @abstractmethod
    def select_next_experiment(self, state: dict) -> dict:
        pass
