from app.discovery.strategies.base import DiscoveryStrategy
import random

class AdaptiveStrategy(DiscoveryStrategy):
    def select_next_experiment(self, state: dict) -> dict:
        # Placeholder heuristic
        expected_failure_probability = random.random()
        information_gain = random.random()
        novelty = random.random()
        uncertainty = random.random()
        
        score = (
            0.35 * expected_failure_probability +
            0.25 * information_gain +
            0.20 * novelty +
            0.20 * uncertainty
        )
        
        return {
            "perturbation_type": "adaptive_timeout",
            "severity": 0.5 + (0.1 * score),
            "score": score
        }
