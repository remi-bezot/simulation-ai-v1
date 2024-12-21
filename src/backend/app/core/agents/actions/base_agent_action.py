from app.application.interfaces.agent_action_interface import IAgentAction


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
        raise NotImplementedError("Subclasses should implement this method!")

    def finalize(self, agent):
        """
        Finalise l'action pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        pass
