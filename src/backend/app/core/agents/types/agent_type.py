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

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.
        """
        raise NotImplementedError("Subclasses should implement this method!")

    def update(self):
        """
        Met à jour l'état de l'agent.
        """
        self.mind.update()
        self.behavior.update()
        self.status_manager.update()
