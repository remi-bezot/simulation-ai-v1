from typing import Dict, List, Optional
from app.core.components.skills import Skills
from app.core.components.resources import Resources
from app.core.agents.actions.base_agent_action import AgentAction
from app.core.agents.types.interfaces.i_action_manager import IActionManager


class AgentActionManager(IActionManager):
    """
    Gère les actions des agents.
    """

    def __init__(self):
        self.skills = Skills()
        self.resources = Resources()
        self.available_actions: Dict[str, AgentAction] = {}
        self.current_action: Optional[AgentAction] = None
        self.action_history: List[AgentAction] = []
        self.action_costs: Dict[str, float] = {}

    def register_action(
        self, action_name: str, action: AgentAction, energy_cost: float = 10.0
    ) -> None:
        """
        Enregistre une nouvelle action disponible.

        :param action_name: Le nom de l'action.
        :param action: L'action à enregistrer.
        :param energy_cost: Le coût en énergie de l'action.
        """
        if action_name not in self.available_actions:
            self.available_actions[action_name] = action
            self.action_costs[action_name] = energy_cost

    def perform_action(self, action_name: str) -> Optional[bool]:
        """
        Exécute une action enregistrée.

        :param action_name: Le nom de l'action à exécuter.
        :return: True si l'action est réussie, False si échouée, None si pas d'action
        """
        if action_name in self.available_actions:
            action = self.available_actions[action_name]
            if self.resources.energy >= self.action_costs[action_name]:
                self.current_action = action
                self.resources.energy -= self.action_costs[action_name]
                self.action_history.append(action)
                return action.execute()
        return None

    def can_perform_action(self, action_name: str, agent) -> bool:
        """Vérifie si l'agent peut effectuer l'action"""
        if action_name not in self.available_actions:
            return False
        return agent.energy >= self.action_costs[action_name]

    def start_action(self, action_name: str, agent) -> bool:
        """Démarre une action si possible"""
        if not self.can_perform_action(action_name, agent):
            return False

        action = self.available_actions[action_name]
        self.current_action = action
        agent.energy -= self.action_costs[action_name]
        action.initialize(agent)
        return True

    def execute_current_action(self, agent) -> bool:
        """Exécute l'action en cours"""
        if not self.current_action:
            return False

        success = self.current_action.execute(agent)
        if success:
            self.action_history.append(self.current_action)
            self.current_action.finalize(agent)
            self.current_action = None
        return success

    def get_available_actions(self) -> List[str]:
        """Liste des actions disponibles"""
        return list(self.available_actions.keys())

    def get_action_history(self) -> List[AgentAction]:
        """Historique des actions"""
        return self.action_history.copy()

    def clear_history(self) -> None:
        """Efface l'historique"""
        self.action_history.clear()
