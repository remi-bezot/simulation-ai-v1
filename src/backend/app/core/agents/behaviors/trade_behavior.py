from app.core.agents.behaviors.agent_behavior import AgentBehavior


class TradeBehavior(AgentBehavior):
    """
    Comportement pour échanger des ressources avec un autre agent.
    """

    def __init__(self, target, resources: dict):
        self.target = target
        self.resources = resources

    def perform(self, agent):
        """
        Fait échanger des ressources à l'agent avec un autre agent.

        :param agent: L'agent qui échange.
        """
        # Logique pour échanger des ressources
        print(
            f"L'agent {agent} échange des ressources avec {self.target} : {self.resources}"
        )
