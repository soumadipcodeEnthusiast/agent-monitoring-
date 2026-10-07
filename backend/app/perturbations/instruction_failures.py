from app.perturbations.base import Perturbation
from app.perturbations.registry import PerturbationRegistry

@PerturbationRegistry.register
class AmbiguousInstructionPerturbation(Perturbation):
    name = "ambiguous_instruction"
    category = "instruction"
    description = "Makes instruction unclear."

    def apply(self, context: dict):
        context['instruction_quality'] = 'ambiguous'
