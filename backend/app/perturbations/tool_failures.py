from app.perturbations.base import Perturbation
from app.perturbations.registry import PerturbationRegistry

@PerturbationRegistry.register
class TimeoutPerturbation(Perturbation):
    name = "timeout"
    category = "tool"
    description = "Simulates a tool timeout."

    def apply(self, context: dict):
        context['error'] = 'TimeoutError'
