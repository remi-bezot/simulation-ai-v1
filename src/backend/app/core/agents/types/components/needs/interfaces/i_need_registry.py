from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from ..definitions.need_definition import NeedDefinition
from ..enums.need_category import NeedCategory


class INeedRegistry(ABC):
    @abstractmethod
    def register_need(self, name: str, definition: NeedDefinition) -> None:
        pass

    @abstractmethod
    def get_need(self, name: str) -> Optional[NeedDefinition]:
        pass

    @abstractmethod
    def get_needs_by_category(
        self, category: NeedCategory
    ) -> Dict[str, NeedDefinition]:
        pass

    @abstractmethod
    def get_priority_needs(self, limit: Optional[int] = None) -> List[str]:
        pass

    @abstractmethod
    def add_observer(self, observer: "INeedRegistryObserver") -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: "INeedRegistryObserver") -> None:
        pass
