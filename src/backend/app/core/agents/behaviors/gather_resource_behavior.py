from app.core.agents.behaviors.agent_behavior import AgentBehavior


class GatherResourceBehavior(AgentBehavior):
    """
    Comportement pour collecter des ressources avec un agent.
    """

    def __init__(self, resource_type: str):
        self.resource_type = resource_type

    def perform(self, agent):
        """
        Fait collecter des ressources à l'agent.

        :param agent: L'agent qui collecte les ressources.
        """
        # Logique pour la collecte de ressources
        print(f"L'agent {agent} collecte des ressources de type {self.resource_type}")
