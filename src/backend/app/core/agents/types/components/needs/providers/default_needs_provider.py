from dataclasses import dataclass
from typing import Dict
from ..interfaces.i_need_provider import INeedProvider
from ..definitions.need_definition import NeedDefinition
from ..enums.need_category import NeedCategory


@dataclass
class DefaultNeedsProvider(INeedProvider):
    def get_needs(self) -> Dict[str, NeedDefinition]:
        return {
            "hunger": NeedDefinition(
                category=NeedCategory.PHYSICAL,
                threshold=80,
                decay_rate=0.1,
                impact_on_mood=-0.2,
                recovery_rate=0.05,
                description="Niveau de faim de l'agent",
                priority=1,
            ),
            "thirst": NeedDefinition(
                category=NeedCategory.PHYSICAL,
                threshold=85,
                decay_rate=0.15,
                impact_on_mood=-0.3,
                recovery_rate=0.08,
                description="Niveau de soif de l'agent",
                priority=2,
            ),
            "rest": NeedDefinition(
                category=NeedCategory.PHYSICAL,
                threshold=75,
                decay_rate=0.05,
                impact_on_mood=-0.15,
                recovery_rate=0.03,
                description="Niveau de fatigue de l'agent",
                priority=3,
            ),
            "mental_stimulation": NeedDefinition(
                category=NeedCategory.MENTAL,
                threshold=60,
                decay_rate=0.06,
                impact_on_mood=-0.2,
                recovery_rate=0.04,
                description="Besoin de stimulation mentale",
                priority=4,
            ),
            "social_interaction": NeedDefinition(
                category=NeedCategory.SOCIAL,
                threshold=70,
                decay_rate=0.08,
                impact_on_mood=-0.25,
                recovery_rate=0.04,
                description="Besoin d'interactions sociales",
                priority=5,
            ),
            "safety": NeedDefinition(
                category=NeedCategory.ENVIRONMENTAL,
                threshold=90,
                decay_rate=0.03,
                impact_on_mood=-0.4,
                recovery_rate=0.02,
                description="Besoin de sécurité",
                priority=6,
            ),
            "hygiene": NeedDefinition(
                category=NeedCategory.ENVIRONMENTAL,
                threshold=65,
                decay_rate=0.07,
                impact_on_mood=-0.1,
                recovery_rate=0.06,
                description="Niveau d'hygiène",
                priority=7,
            ),
            "comfort": NeedDefinition(
                category=NeedCategory.ENVIRONMENTAL,
                threshold=50,
                decay_rate=0.04,
                impact_on_mood=-0.1,
                recovery_rate=0.05,
                description="Niveau de confort",
                priority=8,
            ),
        }
