from app.perturbations.base import Perturbation
from app.perturbations.registry import PerturbationRegistry

@PerturbationRegistry.register
class PermissionDeniedPerturbation(Perturbation):
    name = "permission_denied"
    category = "environment"
    description = "Simulates lack of access."

    def apply(self, context: dict):
        context['error'] = 'PermissionDenied'
