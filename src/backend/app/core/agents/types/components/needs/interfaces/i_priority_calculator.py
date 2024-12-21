from abc import ABC, abstractmethod


class IPriorityCalculator(ABC):
    @abstractmethod
    def calculate(
        self, need: str, base_priority: int, urgency: float, current_value: float
    ) -> int:
        pass
