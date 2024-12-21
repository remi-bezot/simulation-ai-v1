from typing import Optional
from app.core.agents.actions.base_agent_action import AgentAction


class CurrentAction:
    """Classe pour gérer l'action en cours"""

    def __init__(self):
        self.current: Optional[AgentAction] = None
        self.last: Optional[AgentAction] = None

    def set_action(self, action: AgentAction) -> None:
        """Définit l'action en cours"""
        self.current = action

    def complete_action(self) -> None:
        """Marque l'action en cours comme terminée"""
        self.last = self.current
        self.current = None

    def is_completed(self) -> bool:
        """Vérifie si l'action en cours est terminée"""
        return self.current is None

    def update(self) -> None:
        """Met à jour l'état de l'action en cours"""
        if self.current:
            self.current.update()
