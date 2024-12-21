from abc import ABC, abstractmethod
from app.application.interfaces.agent_action_interface import IAgentAction


class IGatherResourceAction(IAgentAction, ABC):
    """
    Interface pour les actions de collecte de ressources des agents.
    """

    @abstractmethod
    def set_resource_type(self, resource_type: str):
        """
        Définit le type de ressource à collecter.

        :param resource_type: Le type de ressource à collecter.
        """
        pass
