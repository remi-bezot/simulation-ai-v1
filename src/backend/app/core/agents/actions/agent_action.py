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
        raise NotImplementedError("Subclasses should implement this method!")

    def finalize(self, agent):
        """
        Finalise l'action pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        pass


class MoveAction(IAgentAction):
    """
    Action de déplacement pour un agent.
    """

    def initialize(self, agent):
        """
        Initialise l'action de déplacement pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        agent.position = (0, 0)

    def execute(self, agent):
        """
        Exécute l'action de déplacement sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        agent.position = (agent.position[0] + 1, agent.position[1] + 1)

    def finalize(self, agent):
        """
        Finalise l'action de déplacement pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        agent.position = (0, 0)
