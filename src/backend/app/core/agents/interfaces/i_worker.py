from abc import ABC, abstractmethod


class IWorker(ABC):
    @abstractmethod
    def work(self, task: str, duration: int):
        pass

    @abstractmethod
    def take_break(self, duration: int):
        pass
