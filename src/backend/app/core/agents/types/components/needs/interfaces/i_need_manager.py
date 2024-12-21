from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class INeedManager(ABC):
    @abstractmethod
    def update_need(self, need: str, amount: float) -> None:
        pass

    @abstractmethod
    def get_need_status(self, need: str) -> Dict:
        pass

    @abstractmethod
    def get_critical_needs(self) -> Dict[str, float]:
        pass

    @abstractmethod
    def add_observer(self, observer: "INeedObserver") -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: "INeedObserver") -> None:
        pass
