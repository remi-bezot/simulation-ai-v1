from abc import ABC, abstractmethod
from typing import List, Dict, Any


class EventInterface(ABC):
    """
    Interface pour la gestion des événements.
    """

    @abstractmethod
    def trigger_event(self, event_name: str) -> Dict[str, Any]:
        """
        Déclenche un événement.

        :param event_name: Nom de l'événement à déclencher.
        :return: Un dictionnaire contenant :
            - "message" : Confirmation de l'action.
            - "event_details" : Détails de l'événement déclenché.
        :raises ValueError: Si le nom de l'événement est vide ou invalide.
        """
        pass

    @abstractmethod
    def get_event_log(self) -> List[Dict[str, Any]]:
        """
        Retourne le log des événements.

        :return: Une liste de dictionnaires représentant chaque événement, contenant :
            - "event_name" : Nom de l'événement.
            - "timestamp" : Date et heure de l'événement.
        """
        pass
