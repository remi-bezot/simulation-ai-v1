from abc import ABC, abstractmethod
from typing import Dict


class IAgentStats(ABC):
    """
    Interface pour les statistiques des agents.
    """

    @abstractmethod
    def update_stat(self, stat: str, value: float) -> None:
        """
        Met à jour une statistique de l'agent.

        :param stat: Le nom de la statistique à mettre à jour.
        :param value: La valeur à ajouter à la statistique.
        """
        pass

    @abstractmethod
    def get_stats(self) -> Dict[str, float]:
        """
        Retourne les statistiques actuelles de l'agent.

        :return: Un dictionnaire contenant les statistiques de l'agent.
        """
        pass
