from app.core.agents.behaviors.agent_behavior import AgentBehavior


class DefendBehavior(AgentBehavior):
    """
    Comportement pour défendre une position avec un agent.
    """

    def __init__(self, position: str):
        self.position = position

    def perform(self, agent):
        """
        Fait défendre une position à l'agent.

        :param agent: L'agent qui défend.
        """
        # Logique pour défendre la position
        print(f"L'agent {agent} défend la position {self.position}")
