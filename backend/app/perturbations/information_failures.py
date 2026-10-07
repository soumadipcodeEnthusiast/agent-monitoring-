from app.perturbations.base import Perturbation
from app.perturbations.registry import PerturbationRegistry

@PerturbationRegistry.register
class StaleDataPerturbation(Perturbation):
    name = "stale_data"
    category = "information"
    description = "Provides outdated information."

    def apply(self, context: dict):
        context['data_status'] = 'stale'
