from abc import ABC, abstractmethod
from typing import Dict


class IMetricsCalculator(ABC):
    @abstractmethod
    def calculate_performance(self, data: Dict) -> float:
        pass

    @abstractmethod
    def calculate_efficiency(self, data: Dict) -> float:
        pass

    @abstractmethod
    def calculate_durability(self, data: Dict) -> float:
        pass

    @abstractmethod
    def calculate_overall_score(self, metrics: Dict[str, float]) -> float:
        pass

    @abstractmethod
    def validate_metrics(self, metrics: Dict[str, float]) -> None:
        pass
