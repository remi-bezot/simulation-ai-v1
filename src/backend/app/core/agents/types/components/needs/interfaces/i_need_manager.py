from abc import ABC, abstractmethod
from typing import Dict, Optional


class INeedManager(ABC):
    @abstractmethod
    def update_need(self, need: str, amount: float) -> None:
        pass

    @abstractmethod
    def get_need_status(self, need: str) -> Dict:
        pass
