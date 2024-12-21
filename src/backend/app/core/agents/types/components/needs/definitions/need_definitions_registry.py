from typing import Dict
from .need_definition import NeedDefinition
from ..enums.need_category import NeedCategory


class NeedDefinitionsRegistry:
    VALID_NEEDS: Dict[str, NeedDefinition] = {
        "hunger": NeedDefinition(
            category=NeedCategory.PHYSICAL,
            threshold=80,
            decay_rate=0.1,
            impact_on_mood=-0.2,
            recovery_rate=0.05,
            description="Niveau de faim de l'agent",
        ),
        # ... autres définitions ...
    }
