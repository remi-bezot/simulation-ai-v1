from app.core.agents.actions.base_agent_action import AgentAction
from app.core.agents.actions.interfaces.i_attack_action import IAttackAction


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
        # Implémentation de l'initialisation
        pass

    def execute(self, agent):
        """
        Exécute l'action d'attaque sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        # Implémentation de l'exécution
        pass

    def finalize(self, agent):
        """
        Finalise l'action d'attaque pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        # Implémentation de la finalisation
        pass
