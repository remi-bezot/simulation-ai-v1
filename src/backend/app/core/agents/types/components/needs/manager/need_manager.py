from dataclasses import dataclass, field
from typing import Dict, List, Optional
from ..enums.need_category import NeedCategory
from ..enums.need_urgency import NeedUrgency
from ..definitions.need_definition import NeedDefinition
from ..interfaces.i_need_manager import INeedManager
from ..interfaces.i_need_provider import INeedProvider
from ..validators.need_validator import NeedValidator


@dataclass
class NeedManager(INeedManager):
    """Système avancé de gestion des besoins pour agents intelligents"""

    need_provider: INeedProvider
    validator: NeedValidator
    current_needs: Dict[str, float] = field(init=False)
    recorder: INeedRecorder
    priority_calculator: IPriorityCalculator
    observers: List[INeedObserver] = field(default_factory=list)

    def __post_init__(self):
        self.current_needs = {
            need: 0.0 for need in self.need_provider.get_needs().keys()
        }
        self.need_history: List[Dict] = []
        self.current_priorities: Dict[str, int] = {}
        self.last_update_time: Optional[float] = None

    def update_need(self, need: str, amount: float) -> None:
        """Met à jour un besoin spécifique"""
        self.validator.validate_need(need, amount)
        self._update_need_value(need, amount)
        self._notify_change(need)
        self._record_need_change(need)
        self._update_priorities()

    def _update_need_value(self, need: str, amount: float) -> None:
        self.current_needs[need] = max(
            0.0, min(100.0, self.current_needs[need] + amount)
        )

    def get_need_status(self, need: str) -> Dict:
        """Retourne le statut détaillé d'un besoin"""
        if need not in self.VALID_NEEDS:
            raise ValueError(f"Besoin invalide: {need}")

        return {
            "current": self.current_needs[need],
            "threshold": self.VALID_NEEDS[need].threshold,
            "priority": self.current_priorities.get(need, 0),
            "category": self.VALID_NEEDS[need].category.value,
            "urgency": self._calculate_urgency(need),
        }

    def get_critical_needs(self) -> Dict[str, float]:
        """Retourne les besoins critiques"""
        return {
            need: value
            for need, value in self.current_needs.items()
            if value >= self.VALID_NEEDS[need].threshold
        }

    def _calculate_urgency(self, need: str) -> NeedUrgency:
        """Calcule l'urgence d'un besoin"""
        value = self.current_needs[need]
        for urgency in reversed(NeedUrgency):
            if value >= self.VALID_NEEDS[need].threshold * urgency.value:
                return urgency
        return NeedUrgency.NORMAL

    def _record_need_change(self, need: str) -> None:
        """Enregistre un changement de besoin"""
        self.recorder.record_change(
            need=need, value=self.current_needs[need], timestamp=datetime.now()
        )
        self._notify_observers(need)

    def _notify_observers(self, need: str) -> None:
        for observer in self.observers:
            observer.on_need_change(need, self.current_needs[need])

    def _update_priorities(self) -> None:
        """Met à jour les priorités des besoins"""
        self.current_priorities = {
            need: self._calculate_priority(need) for need in self.VALID_NEEDS
        }

    def _calculate_priority(self, need: str) -> int:
        """Calcule la priorité d'un besoin"""
        return self.priority_calculator.calculate(
            need=need,
            base_priority=self.VALID_NEEDS[need].priority,
            urgency=self._calculate_urgency(need).value,
            current_value=self.current_needs[need],
        )
