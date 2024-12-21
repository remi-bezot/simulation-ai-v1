from app.application.interfaces.agent_behavior_interface import IAgentBehavior


# Comportements des agents
class AgentBehavior(IAgentBehavior):
    """
    Classe de base pour les comportements des agents.
    """

    def perform(self, agent):
        """
        Exécute le comportement sur l'agent donné.

        :param agent: L'agent sur lequel le comportement est exécuté.
        """
        raise NotImplementedError("Subclasses should implement this method!")
