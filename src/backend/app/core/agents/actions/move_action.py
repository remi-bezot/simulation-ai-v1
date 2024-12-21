from app.core.agents.actions.base_agent_action import AgentAction
from app.application.interfaces.move_action_interface import IMoveAction


class MoveAction(AgentAction, IMoveAction):
    """
    Action pour déplacer un agent.
    """

    def __init__(self, direction: str):
        self.direction = direction

    def set_direction(self, direction: str):
        """
        Définit la direction du déplacement.

        :param direction: La direction du déplacement.
        """
        self.direction = direction

    def initialize(self, agent):
        """
        Initialise l'action de déplacement pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        print(f"Initialisation du déplacement de l'agent {agent} vers {self.direction}")

    def execute(self, agent):
        """
        Déplace l'agent dans la direction spécifiée.

        :param agent: L'agent à déplacer.
        """
        # Logique pour déplacer l'agent
        print(f"Déplacement de l'agent {agent} vers {self.direction}")

    def finalize(self, agent):
        """
        Finalise l'action de déplacement pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        print(f"Finalisation du déplacement de l'agent {agent}")
