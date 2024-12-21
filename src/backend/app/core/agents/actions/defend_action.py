from app.core.agents.actions.base_agent_action import AgentAction
from app.application.interfaces.defend_action_interface import IDefendAction


class DefendAction(AgentAction, IDefendAction):
    """
    Action pour défendre une position avec un agent.
    """

    def __init__(self, position: str):
        self.position = position

    def set_position(self, position: str):
        """
        Définit la position à défendre.

        :param position: La position à défendre.
        """
        self.position = position

    def initialize(self, agent):
        """
        Initialise l'action de défense pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        print(
            f"Initialisation de la défense de la position {self.position} par l'agent {agent}"
        )

    def execute(self, agent):
        """
        Fait défendre une position à l'agent.

        :param agent: L'agent qui défend.
        """
        # Logique pour défendre la position
        print(f"L'agent {agent} défend la position {self.position}")

    def finalize(self, agent):
        """
        Finalise l'action de défense pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        print(f"Finalisation de la défense de l'agent {agent}")
