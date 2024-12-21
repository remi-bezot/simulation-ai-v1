from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from app.core.agents.actions.base_agent_action import AgentAction


class IActionManager(ABC):
    @abstractmethod
    def register_action(
        self, action_name: str, action: AgentAction, energy_cost: float
    ) -> None:
        """Enregistre une nouvelle action disponible"""
        pass

    @abstractmethod
    def can_perform_action(self, action_name: str, agent) -> bool:
        """Vérifie si l'agent peut effectuer l'action"""
        pass

    @abstractmethod
    def start_action(self, action_name: str, agent) -> bool:
        """Démarre une action si possible"""
        pass

    @abstractmethod
    def get_registered_actions(self) -> Dict[str, AgentAction]:
        """Retourne un dictionnaire des actions enregistrées"""
        pass

    @abstractmethod
    def get_action_energy_costs(self) -> Dict[str, float]:
        """Retourne un dictionnaire des coûts énergétiques des actions"""
        pass

    @abstractmethod
    def execute_current_action(self, agent) -> bool:
        """Exécute l'action en cours"""
        pass

    @abstractmethod
    def get_available_actions(self) -> List[str]:
        """Liste des actions disponibles"""
        pass

    @abstractmethod
    def get_current_action(self) -> Optional[AgentAction]:
        """Retourne l'action en cours"""
        pass

    @abstractmethod
    def get_action_history(self) -> List[AgentAction]:
        """Historique des actions"""
        pass

    @abstractmethod
    def clear_history(self) -> None:
        """Efface l'historique"""
        pass

    @abstractmethod
    def cancel_current_action(self) -> bool:
        """Annule l'action en cours"""
        pass

    @abstractmethod
    def get_action_cost(self, action_name: str) -> Optional[float]:
        """Retourne le coût en énergie d'une action"""
        pass
