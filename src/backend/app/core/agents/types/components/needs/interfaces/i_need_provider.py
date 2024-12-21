from abc import ABC, abstractmethod
from typing import Dict
from ..definitions.need_definition import NeedDefinition


class INeedProvider(ABC):
    @abstractmethod
    def get_needs(self) -> Dict[str, NeedDefinition]:
        pass
