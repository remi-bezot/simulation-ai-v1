from abc import ABC, abstractmethod
from app.application.interfaces.agent_action_interface import IAgentAction


class ICommunicateAction(IAgentAction, ABC):
    """
    Interface pour les actions de communication des agents.
    """

    @abstractmethod
    def set_message(self, message: str):
        """
        Définit le message à communiquer.

        :param message: Le message à communiquer.
        """
        pass
