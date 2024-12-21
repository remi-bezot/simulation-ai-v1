from app.core.agents.actions.agent_action import AgentAction
from app.application.interfaces.build_action_interface import IBuildAction


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
        print(
            f"Initialisation de la construction d'une structure de type {self.structure_type} par l'agent {agent}"
        )

    def execute(self, agent):
        """
        Fait construire une structure à l'agent.

        :param agent: L'agent qui construit.
        """
        # Logique pour la construction de la structure
        print(f"L'agent {agent} construit une structure de type {self.structure_type}")

    def finalize(self, agent):
        """
        Finalise l'action de construction pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        print(f"Finalisation de la construction de l'agent {agent}")
