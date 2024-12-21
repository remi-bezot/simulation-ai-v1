from abc import ABC, abstractmethod


class IBuilder(ABC):
    @abstractmethod
    def build_structure(self, structure_type: str, required_resources: dict):
        pass
