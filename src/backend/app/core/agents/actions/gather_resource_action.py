from app.core.agents.actions.base_agent_action import AgentAction
from app.core.agents.actions.interfaces.i_gather_resource_action import (
    IGatherResourceAction,
)


class GatherResourceAction(AgentAction, IGatherResourceAction):
    """
    Action pour collecter des ressources avec un agent.
    """

    def __init__(self, resource_type: str):
        self.resource_type = resource_type

    def set_resource_type(self, resource_type: str):
        """
        Définit le type de ressource à collecter.

        :param resource_type: Le type de ressource à collecter.
        """
        self.resource_type = resource_type

    def initialize(self, agent):
        """
        Initialise l'action de collecte de ressources pour l'agent donné.

        :param agent: L'agent pour lequel l'action est initialisée.
        """
        # Implémentation de l'initialisation
        pass

    def execute(self, agent):
        """
        Exécute l'action de collecte de ressources sur l'agent donné.

        :param agent: L'agent sur lequel l'action est exécutée.
        """
        # Implémentation de l'exécution
        pass

    def finalize(self, agent):
        """
        Finalise l'action de collecte de ressources pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        # Implémentation de la finalisation
        pass
