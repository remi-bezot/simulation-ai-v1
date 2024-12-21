from abc import ABC, abstractmethod


class IScout(ABC):
    @abstractmethod
    def scout_area(self, area: str):
        pass
