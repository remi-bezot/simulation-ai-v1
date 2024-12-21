from app.core.agents.behaviors.interfaces.i_agent_behavior import IAgentBehavior


class AgentBehavior(IAgentBehavior):
    """
    Comportement de base pour un agent.
    """

    def perform(self, agent):
        """
        Exécute le comportement sur l'agent donné.

        :param agent: L'agent sur lequel le comportement est exécuté.
        """
        # Implémentation du comportement
        pass
