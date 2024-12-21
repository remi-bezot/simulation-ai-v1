from abc import ABC, abstractmethod
from app.application.interfaces.agent_action_interface import IAgentAction


class IMoveAction(IAgentAction, ABC):
    """
    Interface pour les actions de déplacement des agents.
    """

    @abstractmethod
    def set_direction(self, direction: str):
        """
        Définit la direction du déplacement.

        :param direction: La direction du déplacement.
        """
        pass
