from app.core.agents.behaviors.agent_behavior import AgentBehavior


class CommunicateBehavior(AgentBehavior):
    """
    Comportement pour communiquer avec un autre agent.
    """

    def __init__(self, message: str):
        self.message = message

    def perform(self, agent):
        """
        Fait communiquer l'agent avec un autre agent.

        :param agent: L'agent qui communique.
        """
        # Logique pour la communication
        print(f"L'agent {agent} communique : {self.message}")
