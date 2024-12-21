from app.core.agents.actions.base_agent_action import AgentAction
from app.application.interfaces.heal_action_interface import IHealAction


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
        print(f"Initialisation du soin de l'agent {agent} sur {self.target}")

    def execute(self, agent):
        """
        Fait soigner un autre agent.

        :param agent: L'agent qui soigne.
        """
        # Logique pour soigner l'agent
        print(f"L'agent {agent} soigne {self.target}")

    def finalize(self, agent):
        """
        Finalise l'action de soin pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        print(f"Finalisation du soin de l'agent {agent}")
