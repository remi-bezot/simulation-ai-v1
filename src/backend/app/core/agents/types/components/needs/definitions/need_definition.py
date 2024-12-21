from dataclasses import dataclass
from ..enums.need_category import NeedCategory


@dataclass
class NeedDefinition:
    category: NeedCategory
    threshold: float
    decay_rate: float
    impact_on_mood: float
    recovery_rate: float
    description: str
    priority: int = 0

    def __post_init__(self):
        if not 0 <= self.threshold <= 100:
            raise ValueError("Le seuil doit être entre 0 et 100")
        if not 0 <= self.decay_rate <= 1:
            raise ValueError("Le taux de décroissance doit être entre 0 et 1")
