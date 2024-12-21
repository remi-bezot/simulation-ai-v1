from typing import List
from app.core.agents.actions.base_agent_action import AgentAction


class ActionQueue:
    """Classe pour gérer la file d'attente des actions"""

    def __init__(self):
        self.queue: List[AgentAction] = []

    def add_action(self, action: AgentAction) -> None:
        """Ajoute une action à la file d'attente"""
        self.queue.append(action)

    def pop_action(self) -> AgentAction:
        """Récupère et retire la première action de la file d'attente"""
        return self.queue.pop(0) if self.queue else None

    def clear(self) -> None:
        """Efface toutes les actions en attente"""
        self.queue.clear()

    def has_actions(self) -> bool:
        """Vérifie si des actions sont en attente"""
        return bool(self.queue)
