from app.core.agents.actions.base_agent_action import AgentAction
from app.core.agents.actions.interfaces.i_defend_action import IDefendAction


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
        # Implémentation de l'initialisation
        pass

    def execute(self, agent):
        """
        Exécute l'action de défense sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        # Implémentation de l'exécution
        pass

    def finalize(self, agent):
        """
        Finalise l'action de défense pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        # Implémentation de la finalisation
        pass
