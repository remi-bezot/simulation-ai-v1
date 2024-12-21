from abc import ABC, abstractmethod


class IHealer(ABC):
    @abstractmethod
    def heal(self, target, healing_amount: float):
        pass
