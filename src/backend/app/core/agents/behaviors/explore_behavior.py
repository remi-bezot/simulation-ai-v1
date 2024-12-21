from app.core.agents.behaviors.agent_behavior import AgentBehavior


class ExploreBehavior(AgentBehavior):
    """
    Comportement pour explorer une zone avec un agent.
    """

    def __init__(self, area: str):
        self.area = area

    def perform(self, agent):
        """
        Fait explorer une zone à l'agent.

        :param agent: L'agent qui explore.
        """
        # Logique pour explorer la zone
        print(f"L'agent {agent} explore la zone {self.area}")
