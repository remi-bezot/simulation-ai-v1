from app.core.agents.behaviors.agent_behavior import AgentBehavior


class MoveBehavior(AgentBehavior):
    """
    Comportement pour déplacer un agent.
    """

    def __init__(self, direction: str):
        self.direction = direction

    def perform(self, agent):
        """
        Déplace l'agent dans la direction spécifiée.

        :param agent: L'agent à déplacer.
        """
        # Logique pour déplacer l'agent
        print(f"L'agent {agent} se déplace vers {self.direction}")
