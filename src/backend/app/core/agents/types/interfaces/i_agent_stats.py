from abc import ABC, abstractmethod
from typing import Dict


class IAgentStats(ABC):
    @abstractmethod
    def update_stat(self, stat: str, value: float) -> None:
        pass

    @abstractmethod
    def get_stats(self) -> Dict[str, float]:
        pass
