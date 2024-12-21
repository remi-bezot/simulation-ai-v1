from typing import Dict, List, Optional
from app.core.components.skills import Skills
from app.core.components.resources import Resources
from app.core.agents.actions.base_agent_action import AgentAction


class AgentActionManager:
    def __init__(self):
        self.skills = Skills()
        self.resources = Resources()
        self.available_actions: Dict[str, AgentAction] = {}
        self.current_action: Optional[AgentAction] = None
        self.action_history: List[AgentAction] = []
        self.action_costs: Dict[str, float] = {}

    def register_action(
        self, action_name: str, action: AgentAction, energy_cost: float = 10.0
    ):
        """Enregistre une nouvelle action disponible"""
        self.available_actions[action_name] = action
        self.action_costs[action_name] = energy_cost

    def can_perform_action(self, action_name: str, agent) -> bool:
        """Vérifie si l'agent peut effectuer l'action"""
        if action_name not in self.available_actions:
            return False
        return agent.energy >= self.action_costs[action_name]

    def start_action(self, action_name: str, agent) -> bool:
        """Démarre une action"""
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
        """Retourne la liste des actions disponibles"""
        return list(self.available_actions.keys())

    def get_action_history(self) -> List[AgentAction]:
        """Retourne l'historique des actions"""
        return self.action_history

    def clear_history(self):
        """Efface l'historique des actions"""
        self.action_history.clear()
