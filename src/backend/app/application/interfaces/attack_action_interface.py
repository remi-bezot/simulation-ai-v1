from abc import ABC, abstractmethod
from app.application.interfaces.agent_action_interface import IAgentAction


class IAttackAction(IAgentAction, ABC):
    """
    Interface pour les actions d'attaque des agents.
    """

    @abstractmethod
    def set_target(self, target):
        """
        Définit la cible de l'attaque.

        :param target: La cible de l'attaque.
        """
        pass
