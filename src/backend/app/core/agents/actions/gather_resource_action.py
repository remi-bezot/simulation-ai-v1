from app.core.agents.actions.base_agent_action import AgentAction
from app.application.interfaces.gather_resource_action_interface import (
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
        print(
            f"Initialisation de la collecte de ressources de type {self.resource_type} par l'agent {agent}"
        )

    def execute(self, agent):
        """
        Fait collecter des ressources à l'agent.

        :param agent: L'agent qui collecte les ressources.
        """
        # Logique pour la collecte de ressources
        print(f"L'agent {agent} collecte des ressources de type {self.resource_type}")

    def finalize(self, agent):
        """
        Finalise l'action de collecte de ressources pour l'agent donné.

        :param agent: L'agent pour lequel l'action est finalisée.
        """
        print(f"Finalisation de la collecte de ressources de l'agent {agent}")
