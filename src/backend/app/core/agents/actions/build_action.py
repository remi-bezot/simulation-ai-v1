from app.core.agents.actions.agent_action import AgentAction
from app.core.agents.actions.interfaces.i_build_action import IBuildAction


class BuildAction(AgentAction, IBuildAction):
    """
    Action pour construire une structure avec un agent.
    """

    def __init__(self, structure_type: str):
        self.structure_type = structure_type

    def set_structure_type(self, structure_type: str):
        """
        Définit le type de structure à construire.

        :param structure_type: Le type de structure à construire.
        """
        self.structure_type = structure_type

    def initialize(self, agent):
        """
        Initialise l'action de construction pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        # Implémentation de l'initialisation
        pass

    def execute(self, agent):
        """
        Exécute l'action de construction sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        # Implémentation de l'exécution
        pass

    def finalize(self, agent):
        """
        Finalise l'action de construction pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        # Implémentation de la finalisation
        pass
