from typing import List, Optional
from app.core.agents.types.interfaces.i_agent_behavior import IAgentBehavior
from app.core.agents.actions.base_agent_action import AgentAction


class AgentBehavior(IAgentBehavior):
    """
    Comportement de base pour un agent.
    """

    def __init__(self):
        self.current_action: Optional[AgentAction] = None
        self.action_queue: List[AgentAction] = []
        self.last_action: Optional[AgentAction] = None

    def perform(self, agent):
        """
        Exécute le comportement sur l'agent donné.

        :param agent: L'agent sur lequel le comportement est exécuté.
        """
        if not self.current_action and self.action_queue:
            self.current_action = self.action_queue.pop(0)

        if self.current_action:
            if self.current_action.is_completed():
                self.last_action = self.current_action
                self.current_action = None
            else:
                self.current_action.execute(agent)

    def add_action(self, action: AgentAction):
        """
        Ajoute une action à la file d'attente.

        :param action: L'action à ajouter
        """
        self.action_queue.append(action)

    def clear_actions(self):
        """
        Efface toutes les actions en attente.
        """
        self.action_queue.clear()
        self.current_action = None

    def has_actions(self) -> bool:
        """
        Vérifie si des actions sont en attente.

        :return: True si des actions sont en attente
        """
        return bool(self.current_action or self.action_queue)

    def update(self):
        """
        Met à jour l'état du comportement.
        """
        if self.current_action:
            self.current_action.update()
