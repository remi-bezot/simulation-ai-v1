from app.core.agents.behaviors.agent_behavior import AgentBehavior


class AttackBehavior(AgentBehavior):
    """
    Comportement pour attaquer avec un agent.
    """

    def __init__(self, target):
        self.target = target

    def perform(self, agent):
        """
        Fait attaquer l'agent la cible spécifiée.

        :param agent: L'agent qui attaque.
        """
        # Logique pour l'attaque de l'agent
        print(f"L'agent {agent} attaque {self.target}")
