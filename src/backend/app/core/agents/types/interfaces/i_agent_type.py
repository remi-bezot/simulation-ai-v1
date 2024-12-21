from abc import ABC, abstractmethod
from typing import Dict


class IAgentType(ABC):
    """
    Interface pour les types d'agents.
    """

    @abstractmethod
    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.
        """
        pass

    @abstractmethod
    def get_stats(self) -> Dict[str, any]:
        """
        Retourne les statistiques de l'agent.
        """
        pass

    @abstractmethod
    def update(self) -> None:
        """
        Met à jour l'état de l'agent.
        """
        pass

    @abstractmethod
    def can_perform_action(self, action_name: str) -> bool:
        """
        Vérifie si l'agent peut effectuer une action.
        """
        pass

    @abstractmethod
    def perform_action(self, action_name: str) -> bool:
        """
        Fait exécuter une action à l'agent.
        """
        pass

    @abstractmethod
    def gain_experience(self, amount: float) -> None:
        """
        Fait gagner de l'expérience à l'agent.
        """
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        """
        Vérifie si l'agent est en vie.
        """
        pass
