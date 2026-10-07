from app.perturbations.base import Perturbation
from app.perturbations.registry import PerturbationRegistry

@PerturbationRegistry.register
class PromptInjectionPerturbation(Perturbation):
    name = "prompt_injection"
    category = "adversarial"
    description = "Injects malicious prompt."

    def apply(self, context: dict):
        context['adversarial'] = True
