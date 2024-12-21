from abc import ABC, abstractmethod


class ISoldier(ABC):
    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def defend(self):
        pass
