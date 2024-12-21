from app.core.agents.actions.interfaces.i_agent_action import IAgentAction


class AgentAction(IAgentAction):
    """
    Classe de base pour les actions spécifiques aux agents.
    """

    def initialize(self, agent):
        """
        Initialise l'action pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        pass

    def execute(self, agent):
        """
        Exécute l'action sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        pass

    def finalize(self, agent):
        """
        Finalise l'action pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        pass
