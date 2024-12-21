from app.core.agents.actions.base_agent_action import AgentAction
from app.core.agents.actions.interfaces.i_rest_action import IRestAction


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
        # Implémentation de l'exécution
        pass

    def finalize(self, agent):
        """
        Finalise l'action de repos pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        # Implémentation de la finalisation
        pass
