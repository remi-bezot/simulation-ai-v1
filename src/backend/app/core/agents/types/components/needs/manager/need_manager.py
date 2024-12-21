from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime
from ..enums.need_category import NeedCategory
from ..enums.need_urgency import NeedUrgency
from ..definitions.need_definition import NeedDefinition
from ..interfaces.i_need_manager import INeedManager
from ..interfaces.i_need_provider import INeedProvider
from ..validators.need_validator import NeedValidator
from ..interfaces.i_need_recorder import INeedRecorder
from ..interfaces.i_priority_calculator import IPriorityCalculator
from ..interfaces.i_need_registry_observer import INeedObserver


@dataclass
class NeedManager(INeedManager):
    """Système avancé de gestion des besoins pour agents intelligents"""

    need_provider: INeedProvider
    validator: NeedValidator
    recorder: INeedRecorder
    priority_calculator: IPriorityCalculator
    observers: List[INeedObserver] = field(default_factory=list)
    current_needs: Dict[str, float] = field(init=False)

    def __post_init__(self):
        self.current_needs = {
            need: 0.0 for need in self.need_provider.get_needs().keys()
        }
        self.need_history: List[Dict] = []

    def update_need(self, need: str, amount: float) -> None:
        """Met à jour un besoin spécifique"""
        if need not in self.current_needs:
            raise ValueError(f"Besoin invalide: {need}")

        self.current_needs[need] = max(
            0.0, min(100.0, self.current_needs[need] + amount)
        )
        self.recorder.record_change(need, self.current_needs[need], datetime.now())
        self._notify_observers(need)

    def get_need_status(self, need: str) -> Dict:
        """Retourne le statut détaillé d'un besoin"""
        if need not in self.current_needs:
            raise ValueError(f"Besoin invalide: {need}")

        return {
            "current": self.current_needs[need],
            "threshold": self.need_provider.get_needs()[need].threshold,
            "priority": self.priority_calculator.calculate(
                need,
                self.need_provider.get_needs()[need].priority,
                self._calculate_urgency(need).value,
                self.current_needs[need],
            ),
            "category": self.need_provider.get_needs()[need].category.value,
            "urgency": self._calculate_urgency(need),
        }

    def get_critical_needs(self) -> Dict[str, float]:
        """Retourne les besoins critiques"""
        return {
            need: value
            for need, value in self.current_needs.items()
            if value >= self.need_provider.get_needs()[need].threshold
        }

    def add_observer(self, observer: INeedObserver) -> None:
        """Ajoute un observateur"""
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer: INeedObserver) -> None:
        """Supprime un observateur"""
        if observer in self.observers:
            self.observers.remove(observer)

    def _calculate_urgency(self, need: str) -> NeedUrgency:
        """Calcule l'urgence d'un besoin"""
        value = self.current_needs[need]
        for urgency in reversed(NeedUrgency):
            if (
                value
                >= self.need_provider.get_needs()[need].threshold
                * urgency.get_threshold()
            ):
                return urgency
        return NeedUrgency.NORMAL

    def _notify_observers(self, need: str) -> None:
        """Notifie les observateurs d'un changement"""
        for observer in self.observers:
            observer.on_registry_change(
                "update", need, self.need_provider.get_needs()[need]
            )
