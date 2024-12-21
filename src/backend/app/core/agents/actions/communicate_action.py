from app.core.agents.actions.base_agent_action import AgentAction
from app.core.agents.actions.interfaces.i_communicate_action import ICommunicateAction


class CommunicateAction(AgentAction, ICommunicateAction):
    """
    Action pour communiquer avec un autre agent.
    """

    def __init__(self, message: str):
        self.message = message

    def set_message(self, message: str):
        """
        Définit le message à communiquer.

        :param message: Le message à communiquer.
        """
        self.message = message

    def initialize(self, agent):
        """
        Initialise l'action de communication pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        # Implémentation de l'initialisation
        pass

    def execute(self, agent):
        """
        Exécute l'action de communication sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        # Implémentation de l'exécution
        pass

    def finalize(self, agent):
        """
        Finalise l'action de communication pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        # Implémentation de la finalisation
        pass
