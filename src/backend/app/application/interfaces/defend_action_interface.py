from abc import ABC, abstractmethod
from app.application.interfaces.agent_action_interface import IAgentAction


class IDefendAction(IAgentAction, ABC):
    """
    Interface pour les actions de défense des agents.
    """

    @abstractmethod
    def set_position(self, position: str):
        """
        Définit la position à défendre.

        :param position: La position à défendre.
        """
        pass
