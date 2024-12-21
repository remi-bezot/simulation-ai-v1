from abc import ABC, abstractmethod


class ITrader(ABC):
    @abstractmethod
    def buy(self, item: str, quantity: int, price: float):
        pass

    @abstractmethod
    def sell(self, item: str, quantity: int, price: float):
        pass
