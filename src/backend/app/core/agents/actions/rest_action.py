from app.core.agents.actions.base_agent_action import AgentAction
from app.application.interfaces.rest_action_interface import IRestAction


class RestAction(AgentAction, IRestAction):
    """
    Action pour faire reposer un agent.
    """

    def initialize(self, agent):
        """
        Initialise l'action de repos pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        print(f"Initialisation du repos de l'agent {agent}")

    def execute(self, agent):
        """
        Fait reposer l'agent.

        :param agent: L'agent qui se repose.
        """
        # Logique pour faire reposer l'agent
        print(f"L'agent {agent} se repose")

    def finalize(self, agent):
        """
        Finalise l'action de repos pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        print(f"Finalisation du repos de l'agent {agent}")
