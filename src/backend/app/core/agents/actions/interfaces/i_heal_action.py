from abc import ABC, abstractmethod
from app.application.interfaces.agent_action_interface import IAgentAction


class IHealAction(IAgentAction, ABC):
    """
    Interface pour les actions de soin des agents.
    """

    @abstractmethod
    def set_target(self, target):
        """
        Définit la cible du soin.

        :param target: La cible du soin.
        """
        pass
