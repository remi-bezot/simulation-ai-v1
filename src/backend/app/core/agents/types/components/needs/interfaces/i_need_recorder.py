from abc import ABC, abstractmethod
from typing import Dict, List
from datetime import datetime


class INeedRecorder(ABC):
    """Interface pour l'enregistrement de l'historique des besoins"""

    @abstractmethod
    def record_change(self, need: str, value: float, timestamp: datetime) -> None:
        """
        Enregistre un changement de valeur d'un besoin.

        :param need: Le besoin concerné
        :param value: La nouvelle valeur
        :param timestamp: L'horodatage du changement
        """
        pass

    @abstractmethod
    def get_history(self, need: str) -> List[Dict]:
        """
        Récupère l'historique des changements pour un besoin.

        :param need: Le besoin concerné
        :return: Liste des changements enregistrés
        """
        pass

    @abstractmethod
    def get_last_value(self, need: str) -> float:
        """
        Récupère la dernière valeur enregistrée pour un besoin.

        :param need: Le besoin concerné
        :return: La dernière valeur ou None si aucun historique
        """
        pass

    @abstractmethod
    def clear_history(self, need: str) -> None:
        """
        Efface l'historique d'un ou tous les besoins.

        :param need: Le besoin à effacer ou None pour tout effacer
        """
        pass
