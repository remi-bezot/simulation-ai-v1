from abc import ABC, abstractmethod
from typing import Optional
from app.core.agents.actions.base_agent_action import AgentAction


class IAgentBehavior(ABC):
    """
    Interface pour le comportement des agents.
    """

    @abstractmethod
    def perform(self, agent) -> Optional[bool]:
        """
        Exécute le comportement sur l'agent donné.

        :param agent: L'agent sur lequel le comportement est exécuté.
        :return: True si l'action est réussie, False si échouée, None si pas d'action
        """
        pass

    @abstractmethod
    def add_action(self, action: AgentAction) -> None:
        """
        Ajoute une action à la file d'attente.

        :param action: L'action à ajouter
        """
        pass

    @abstractmethod
    def clear_actions(self):
        """
        Efface toutes les actions en attente.
        """
        pass

    @abstractmethod
    def has_actions(self) -> bool:
        """
        Vérifie si des actions sont en attente.

        :return: True si des actions sont en attente
        """
        pass

    @abstractmethod
    def update(self):
        """
        Met à jour l'état du comportement.
        """
        pass

    @abstractmethod
    def get_current_action(self) -> Optional[AgentAction]:
        """
        Retourne l'action en cours d'exécution.

        :return: L'action courante ou None si aucune action en cours
        """
        pass

    @abstractmethod
    def get_last_action(self) -> Optional[AgentAction]:
        """
        Retourne la dernière action exécutée.

        :return: La dernière action ou None si aucune action exécutée
        """
        pass
