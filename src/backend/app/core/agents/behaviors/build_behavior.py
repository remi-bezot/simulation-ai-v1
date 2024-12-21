from app.core.agents.behaviors.agent_behavior import AgentBehavior


class BuildBehavior(AgentBehavior):
    """
    Comportement pour construire une structure avec un agent.
    """

    def __init__(self, structure_type: str):
        self.structure_type = structure_type

    def perform(self, agent):
        """
        Fait construire une structure à l'agent.

        :param agent: L'agent qui construit.
        """
        # Logique pour la construction de la structure
        print(f"L'agent {agent} construit une structure de type {self.structure_type}")
