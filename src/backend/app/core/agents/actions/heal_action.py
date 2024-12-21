from app.core.agents.actions.base_agent_action import AgentAction
from app.core.agents.actions.interfaces.i_heal_action import IHealAction


class HealAction(AgentAction, IHealAction):
    """
    Action pour soigner un autre agent.
    """

    def __init__(self, target):
        self.target = target

    def set_target(self, target):
        """
        Définit la cible du soin.

        :param target: La cible du soin.
        """
        self.target = target

    def initialize(self, agent):
        """
        Initialise l'action de soin pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        # Implémentation de l'initialisation
        pass

    def execute(self, agent):
        """
        Exécute l'action de soin sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        # Implémentation de l'exécution
        pass

    def finalize(self, agent):
        """
        Finalise l'action de soin pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        # Implémentation de la finalisation
        pass
