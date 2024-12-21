from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
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
        self.current_needs = self.need_provider.provide_needs()

    def validate_needs(self):
        for need, value in self.current_needs.items():
            self.validator.validate(need, value)

    def record_needs(self):
        for need, value in self.current_needs.items():
            self.recorder.record(need, value)

    def calculate_priorities(self):
        priorities = {}
        for need, value in self.current_needs.items():
            urgency = self.determine_urgency(value)
            priorities[need] = self.priority_calculator.calculate(need, value, urgency)
        return priorities

    def determine_urgency(self, value: float) -> NeedUrgency:
        if value < 0.25:
            return NeedUrgency.EMERGENCY
        elif value < 0.5:
            return NeedUrgency.CRITICAL
        elif value < 0.75:
            return NeedUrgency.WARNING
        else:
            return NeedUrgency.NORMAL

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.current_needs)

    def update_needs(self, new_needs: Dict[str, float]):
        self.current_needs.update(new_needs)
        self.validate_needs()
        self.record_needs()
        self.notify_observers()

    def get_need_status(self, need: str) -> Optional[float]:
        return self.current_needs.get(need)

    def remove_need(self, need: str):
        if need in self.current_needs:
            del self.current_needs[need]
            self.notify_observers()

    def add_observer(self, observer: INeedObserver):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer: INeedObserver):
        if observer in self.observers:
            self.observers.remove(observer)

    def get_all_needs(self) -> Dict[str, float]:
        return self.current_needs

    def get_prioritized_needs(self) -> List[Tuple[str, int]]:
        priorities = self.calculate_priorities()
        return sorted(priorities.items(), key=lambda item: item[1], reverse=True)

    def add_need(self, need: NeedDefinition, value: float):
        self.current_needs[need.name] = value
        self.notify_observers()

    def get_needs_by_category(self, category: NeedCategory) -> Dict[str, float]:
        return {
            need: value
            for need, value in self.current_needs.items()
            if need.category == category
        }

    def get_needs_history(self) -> Dict[str, List[Tuple[datetime, float]]]:
        return {need: self.recorder.get_history(need) for need in self.current_needs}


# Ajoutez ici les autres méthodes et classes nécessaires
