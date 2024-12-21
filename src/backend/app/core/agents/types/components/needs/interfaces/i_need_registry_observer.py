from abc import ABC, abstractmethod
from typing import Literal
from ..definitions.need_definition import NeedDefinition

ActionType = Literal["add", "update", "remove"]


class INeedObserver(ABC):
    """Interface pour observer les changements dans le registre des besoins"""

    @abstractmethod
    def on_registry_change(
        self, action: ActionType, name: str, definition: NeedDefinition
    ) -> None:
        pass

    @abstractmethod
    def on_need_added(self, name: str, definition: NeedDefinition) -> None:
        pass

    @abstractmethod
    def on_need_updated(self, name: str, definition: NeedDefinition) -> None:
        pass

    @abstractmethod
    def on_need_removed(self, name: str) -> None:
        pass
