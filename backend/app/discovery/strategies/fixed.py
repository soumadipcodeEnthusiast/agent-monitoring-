from app.discovery.strategies.base import DiscoveryStrategy

class FixedStrategy(DiscoveryStrategy):
    def select_next_experiment(self, state: dict) -> dict:
        return {
            "perturbation_type": "timeout",
            "severity": 0.5
        }
