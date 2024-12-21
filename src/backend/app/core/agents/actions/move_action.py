from app.core.agents.actions.interfaces.i_move_action import IMoveAction


class MoveAction(IMoveAction):
    """
    Action de déplacement pour un agent.
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
        # Implémentation de l'initialisation
        pass

    def execute(self, agent):
        """
        Exécute l'action de déplacement sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        # Implémentation de l'exécution
        pass

    def finalize(self, agent):
        """
        Finalise l'action de déplacement pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        # Implémentation de la finalisation
        pass
