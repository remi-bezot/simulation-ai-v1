from app.core.agents.actions.base_agent_action import AgentAction
from app.application.interfaces.explore_action_interface import IExploreAction


class ExploreAction(AgentAction, IExploreAction):
    """
    Action pour explorer une zone avec un agent.
    """

    def __init__(self, area: str):
        self.area = area

    def set_area(self, area: str):
        """
        Définit la zone à explorer.

        :param area: La zone à explorer.
        """
        self.area = area

    def initialize(self, agent):
        """
        Initialise l'action d'exploration pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        print(
            f"Initialisation de l'exploration de la zone {self.area} par l'agent {agent}"
        )

    def execute(self, agent):
        """
        Fait explorer une zone à l'agent.

        :param agent: L'agent qui explore.
        """
        # Logique pour explorer la zone
        print(f"L'agent {agent} explore la zone {self.area}")

    def finalize(self, agent):
        """
        Finalise l'action d'exploration pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        print(f"Finalisation de l'exploration de l'agent {agent}")
