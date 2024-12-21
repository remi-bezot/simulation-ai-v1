from app.core.agents.behaviors.agent_behavior import AgentBehavior


class HealBehavior(AgentBehavior):
    """
    Comportement pour soigner un autre agent.
    """

    def __init__(self, target):
        self.target = target

    def perform(self, agent):
        """
        Fait soigner un autre agent.

        :param agent: L'agent qui soigne.
        """
        # Logique pour soigner l'agent
        print(f"L'agent {agent} soigne {self.target}")
