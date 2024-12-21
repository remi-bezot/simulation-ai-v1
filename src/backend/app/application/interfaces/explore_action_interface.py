from abc import ABC, abstractmethod
from app.application.interfaces.agent_action_interface import IAgentAction


class IExploreAction(IAgentAction, ABC):
    """
    Interface pour les actions d'exploration des agents.
    """

    @abstractmethod
    def set_area(self, area: str):
        """
        Définit la zone à explorer.

        :param area: La zone à explorer.
        """
        pass
