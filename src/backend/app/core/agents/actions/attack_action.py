from app.core.agents.actions.base_agent_action import AgentAction
from app.application.interfaces.attack_action_interface import IAttackAction


class AttackAction(AgentAction, IAttackAction):
    """
    Action pour attaquer avec un agent.
    """

    def __init__(self, target):
        self.target = target

    def set_target(self, target):
        """
        Définit la cible de l'attaque.

        :param target: La cible de l'attaque.
        """
        self.target = target

    def initialize(self, agent):
        """
        Initialise l'action d'attaque pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        print(f"Initialisation de l'attaque de l'agent {agent} sur {self.target}")

    def execute(self, agent):
        """
        Fait attaquer l'agent la cible spécifiée.

        :param agent: L'agent qui attaque.
        """
        # Logique pour l'attaque de l'agent
        print(f"L'agent {agent} attaque {self.target}")

    def finalize(self, agent):
        """
        Finalise l'action d'attaque pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        print(f"Finalisation de l'attaque de l'agent {agent}")
