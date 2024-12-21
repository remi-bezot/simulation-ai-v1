from app.core.agents.types.base.base_agent_type import BaseAgentType
from app.core.agents.types.managers.status_manager import AgentStatusManager
from app.core.agents.types.managers.action_manager import AgentActionManager
from app.core.agents.types.components.agent_behavior import AgentBehavior
from app.core.agents.types.components.agent_mind import AgentMind


class AgentType(BaseAgentType):
    """
    Classe de base pour les types d'agents.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.behavior = AgentBehavior()
        self.mind = AgentMind()
        self.status_manager = AgentStatusManager()
        self.action_manager = AgentActionManager()

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.
        """
        raise NotImplementedError("Les sous-classes doivent implémenter cette méthode!")

    def update(self) -> None:
        """
        Met à jour l'état de l'agent.
        """
        self.mind.update()
        self.behavior.update()
        self.status_manager.update()
        self.action_manager.update()

    def get_status(self) -> dict:
        """
        Retourne le statut complet de l'agent.
        """
        return {
            "name": self.name,
            "type": self.get_type_name(),
            "mind": self.mind.get_current_state(),
            "status": self.status_manager.get_status(),
            "base_stats": super().get_stats(),
        }

    def can_perform_action(self, action_name: str) -> bool:
        """
        Vérifie si l'agent peut effectuer une action.
        """
        return self.action_manager.can_perform_action(action_name, self)

    def perform_action(self, action_name: str) -> bool:
        """
        Fait exécuter une action à l'agent.
        """
        if self.can_perform_action(action_name):
            return self.action_manager.start_action(action_name, self)
        return False
