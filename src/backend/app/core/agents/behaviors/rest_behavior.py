from app.core.agents.behaviors.agent_behavior import AgentBehavior


class RestBehavior(AgentBehavior):
    """
    Comportement pour faire reposer un agent.
    """

    def perform(self, agent):
        """
        Fait reposer l'agent.

        :param agent: L'agent qui se repose.
        """
        # Logique pour faire reposer l'agent
        print(f"L'agent {agent} se repose")
