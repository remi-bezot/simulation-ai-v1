from abc import ABC, abstractmethod
from app.application.interfaces.agent_action_interface import IAgentAction


class ITradeAction(IAgentAction, ABC):
    """
    Interface pour les actions d'échange des agents.
    """

    @abstractmethod
    def set_target(self, target):
        """
        Définit la cible de l'échange.

        :param target: La cible de l'échange.
        """
        pass

    @abstractmethod
    def set_resources(self, resources: dict):
        """
        Définit les ressources à échanger.

        :param resources: Les ressources à échanger.
        """
        pass
