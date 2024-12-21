from app.core.agents.actions.base_agent_action import AgentAction
from app.core.agents.actions.interfaces.i_explore_action import IExploreAction


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
        # Implémentation de l'initialisation
        pass

    def execute(self, agent):
        """
        Exécute l'action d'exploration sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        # Implémentation de l'exécution
        pass

    def finalize(self, agent):
        """
        Finalise l'action d'exploration pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        # Implémentation de la finalisation
        pass
