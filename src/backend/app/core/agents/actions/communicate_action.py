from app.core.agents.actions.base_agent_action import AgentAction
from app.application.interfaces.communicate_action_interface import ICommunicateAction


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
        print(
            f"Initialisation de la communication de l'agent {agent} avec le message : {self.message}"
        )

    def execute(self, agent):
        """
        Fait communiquer l'agent avec un autre agent.

        :param agent: L'agent qui communique.
        """
        # Logique pour la communication
        print(f"L'agent {agent} communique : {self.message}")

    def finalize(self, agent):
        """
        Finalise l'action de communication pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        print(f"Finalisation de la communication de l'agent {agent}")
