from typing import Dict, Type
from app.perturbations.base import Perturbation

class PerturbationRegistry:
    _registry: Dict[str, Type[Perturbation]] = {}

    @classmethod
    def register(cls, perturbation_cls: Type[Perturbation]):
        cls._registry[perturbation_cls.name] = perturbation_cls
        return perturbation_cls

    @classmethod
    def get(cls, name: str) -> Type[Perturbation]:
        return cls._registry.get(name)
