from abc import ABC, abstractmethod


class BasePriorityStrategy(ABC):
    @abstractmethod
    def calculate_priority(
        self, base_priority: int, urgency_factor: float, current_value: float
    ) -> int:
        pass


class SimplePriorityStrategy(BasePriorityStrategy):
    def calculate_priority(
        self, base_priority: int, urgency_factor: float, current_value: float
    ) -> int:
        return int(base_priority * urgency_factor * (current_value / 100))
