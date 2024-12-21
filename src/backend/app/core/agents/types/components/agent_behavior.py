from typing import Optional
from app.core.agents.types.interfaces.i_agent_behavior import IAgentBehavior
from app.core.agents.actions.base_agent_action import AgentAction
from app.core.agents.types.components.action_queue import ActionQueue
from app.core.agents.types.components.current_action import CurrentAction


class AgentBehavior(IAgentBehavior):
    """
    Comportement de base pour un agent.
    """

    def __init__(self):
        self.current_action = CurrentAction()
        self.action_queue = ActionQueue()

    def perform(self, agent) -> Optional[bool]:
        """
        Exécute le comportement sur l'agent donné.

        :param agent: L'agent sur lequel le comportement est exécuté.
        :return: True si l'action est réussie, False si échouée, None si pas d'action
        """
        if self.current_action.is_completed() and self.action_queue.has_actions():
            self.current_action.set_action(self.action_queue.pop_action())
        return self.current_action.execute(agent)

    def add_action(self, action: AgentAction) -> None:
        """
        Ajoute une action à la file d'attente.

        :param action: L'action à ajouter
        """
        self.action_queue.add_action(action)

    def clear_actions(self) -> None:
        """
        Efface toutes les actions en attente.
        """
        self.action_queue.clear()
        self.current_action.complete_action()

    def has_actions(self) -> bool:
        """
        Vérifie si des actions sont en attente.

        :return: True si des actions sont en attente
        """
        return (
            self.current_action.current is not None or self.action_queue.has_actions()
        )

    def update(self) -> None:
        """
        Met à jour l'état du comportement.
        """
        self.current_action.update()
