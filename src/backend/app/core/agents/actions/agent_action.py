from ..interfaces.i_agent_action import IAgentAction
from ..exceptions.agent_action_exception import AgentActionException


class AgentAction(IAgentAction):
    """
    Classe de base pour les actions des agents.
    """

    def initialize(self, agent) -> None:
        """
        Initialise l'action pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        pass

    def execute(self, agent) -> None:
        """
        Exécute l'action sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        raise NotImplementedError("Subclasses should implement this method!")

    def finalize(self, agent) -> None:
        """
        Finalise l'action pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        pass


class MoveAction(AgentAction):
    """
    Action de déplacement pour un agent.
    """

    def __init__(self, destination):
        self.destination = destination

    def initialize(self, agent) -> None:
        """
        Initialise l'action de déplacement pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        agent.set_destination(self.destination)

    def execute(self, agent) -> None:
        """
        Exécute l'action de déplacement sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        if not agent.move_towards(self.destination):
            raise AgentActionException(
                "L'agent ne peut pas se déplacer vers la destination."
            )

    def finalize(self, agent) -> None:
        """
        Finalise l'action de déplacement pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        agent.clear_destination()
