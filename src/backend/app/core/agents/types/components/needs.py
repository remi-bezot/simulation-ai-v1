from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from statistics import mean


class NeedCategory(Enum):
    PHYSICAL = "physical"
    MENTAL = "mental"
    SOCIAL = "social"
    ENVIRONMENTAL = "environmental"


class NeedUrgency(Enum):
    NORMAL = "normal"
    WARNING = "warning"
    CRITICAL = "critical"
    EMERGENCY = "emergency"


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


@dataclass
class Need:
    name: str
    category: NeedCategory
    urgency: NeedUrgency
    value: float = 0.0
    history: List[Tuple[datetime, float]] = field(default_factory=list)

    def update_value(self, new_value: float):
        self.value = new_value
        self.history.append((datetime.now(), new_value))

    def get_average_value(self) -> float:
        return mean([value for _, value in self.history])


@dataclass
class Needs:
    """Système avancé de gestion des besoins pour agents intelligents"""

    VALID_NEEDS: Dict[str, NeedDefinition] = {
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
        "social": NeedDefinition(
            category=NeedCategory.SOCIAL,
            threshold=70,
            decay_rate=0.08,
            impact_on_mood=-0.25,
            recovery_rate=0.04,
            description="Besoin d'interactions sociales",
        ),
        "hygiene": NeedDefinition(
            category=NeedCategory.ENVIRONMENTAL,
            threshold=65,
            decay_rate=0.07,
            impact_on_mood=-0.1,
            recovery_rate=0.06,
            description="Niveau d'hygiène de l'agent",
        ),
        "mental_stimulation": NeedDefinition(
            category=NeedCategory.MENTAL,
            threshold=60,
            decay_rate=0.06,
            impact_on_mood=-0.2,
            recovery_rate=0.04,
            description="Besoin de stimulation mentale",
        ),
    }

    URGENCY_THRESHOLDS = {
        NeedUrgency.NORMAL: 0.3,
        NeedUrgency.WARNING: 0.5,
        NeedUrgency.CRITICAL: 0.8,
        NeedUrgency.EMERGENCY: 0.9,
    }

    current_needs: Dict[str, float] = field(
        default_factory=lambda: {need: 0.0 for need in Needs.VALID_NEEDS.keys()}
    )
    needs_history: List[Dict] = field(default_factory=list)
    need_satisfaction_stats: Dict[str, List[float]] = field(
        default_factory=lambda: {need: [] for need in Needs.VALID_NEEDS.keys()}
    )

    def satisfy_need(self, need: str, amount: float) -> Optional[float]:
        """
        Satisfait un besoin spécifique.

        :param need: Le besoin à satisfaire
        :param amount: La quantité de satisfaction
        :return: La nouvelle valeur du besoin ou None si invalide
        """
        if not self._validate_need(need, amount):
            return None

        self.current_needs[need] = max(0.0, self.current_needs[need] - amount)
        self._record_need(need)
        return self.current_needs[need]

    def update(self, delta_time: float = 1.0) -> List[Tuple[str, NeedUrgency]]:
        """
        Met à jour tous les besoins et retourne les changements d'urgence.

        :return: Liste des besoins ayant changé d'état d'urgence
        """
        urgency_changes = []
        for need, config in self.VALID_NEEDS.items():
            old_urgency = self.get_need_urgency(need)
            self._update_need(need, delta_time)
            new_urgency = self.get_need_urgency(need)

            if old_urgency != new_urgency:
                urgency_changes.append((need, new_urgency))

        self._record_needs()
        return urgency_changes

    def _update_need(self, need: str, delta_time: float) -> None:
        """Met à jour un besoin spécifique"""
        config = self.VALID_NEEDS[need]
        decay = config.decay_rate * delta_time
        recovery = config.recovery_rate * delta_time

        if self.current_needs[need] > config.threshold:
            self.current_needs[need] = max(0.0, self.current_needs[need] - recovery)
        else:
            self.current_needs[need] = min(100.0, self.current_needs[need] + decay)

    def get_need_urgency(self, need: str) -> NeedUrgency:
        """Détermine le niveau d'urgence d'un besoin"""
        value = self.current_needs[need]
        for urgency, threshold in sorted(
            self.URGENCY_THRESHOLDS.items(), key=lambda x: x[1], reverse=True
        ):
            if value >= threshold * 100:
                return urgency
        return NeedUrgency.NORMAL

    def get_critical_needs(self) -> Dict[str, float]:
        """
        Retourne les besoins critiques.

        :return: Dictionnaire des besoins dépassant leur seuil
        """
        return {
            need: value
            for need, value in self.current_needs.items()
            if value >= self.VALID_NEEDS[need].threshold
        }

    def get_priority_need(self) -> Optional[str]:
        """
        Retourne le besoin le plus urgent.

        :return: Le nom du besoin le plus urgent ou None
        """
        critical_needs = self.get_critical_needs()
        return (
            max(critical_needs.items(), key=lambda x: x[1])[0]
            if critical_needs
            else None
        )

    def get_need_value(self, need: str) -> Optional[float]:
        """
        Retourne la valeur actuelle d'un besoin.

        :param need: Le besoin à vérifier
        :return: La valeur du besoin ou None si invalide
        """
        return self.current_needs.get(need)

    def is_critical(self) -> bool:
        """
        Vérifie si des besoins sont critiques.

        :return: True si au moins un besoin est critique
        """
        return bool(self.get_critical_needs())

    def get_mood_impact(self) -> float:
        """Calcule l'impact total des besoins sur l'humeur"""
        total_impact = 0.0
        for need, value in self.current_needs.items():
            config = self.VALID_NEEDS[need]
            if value >= config.threshold:
                total_impact += config.impact_on_mood * (value / 100.0)
        return max(-1.0, min(1.0, total_impact))

    def get_needs_by_category(self) -> Dict[NeedCategory, Dict[str, float]]:
        """Regroupe les besoins par catégorie"""
        categorized = {category: {} for category in NeedCategory}
        for need, value in self.current_needs.items():
            category = self.VALID_NEEDS[need].category
            categorized[category][need] = value
        return categorized

    def get_category_satisfaction(self, category: NeedCategory) -> float:
        """Calcule le niveau de satisfaction moyen pour une catégorie"""
        needs = {
            need: value
            for need, value in self.current_needs.items()
            if self.VALID_NEEDS[need].category == category
        }
        return mean(needs.values()) if needs else 0.0

    def get_need_stats(self, need: str) -> Dict:
        """Retourne les statistiques détaillées d'un besoin"""
        history = [h for h in self.needs_history if h["need"] == need]
        values = [h["value"] for h in history]

        return {
            "current": self.current_needs[need],
            "average": mean(values) if values else 0,
            "min": min(values) if values else 0,
            "max": max(values) if values else 0,
            "urgency": self.get_need_urgency(need),
            "category": self.VALID_NEEDS[need].category,
            "description": self.VALID_NEEDS[need].description,
        }

    def _validate_need(self, need: str, amount: float) -> bool:
        """Valide un besoin et sa valeur"""
        if need not in self.VALID_NEEDS:
            return False
        if not 0 <= amount <= 100:
            return False
        return True

    def _record_need(self, need: str) -> None:
        """Enregistre un besoin dans l'historique"""
        self.needs_history.append(
            {
                "need": need,
                "value": self.current_needs[need],
                "timestamp": datetime.now(),
            }
        )

    def _record_needs(self) -> None:
        """Enregistre tous les besoins dans l'historique"""
        for need in self.VALID_NEEDS:
            self._record_need(need)
