from app.discovery.strategies.base import DiscoveryStrategy
import random

class RandomStrategy(DiscoveryStrategy):
    def select_next_experiment(self, state: dict) -> dict:
        return {
            "perturbation_type": "timeout",
            "severity": random.random()
        }
