from datetime import datetime
from typing import List, Callable, Dict, Any
from abc import ABC, abstractmethod


class IEventManager(ABC):
    """
    Interface pour le gestionnaire d'événements.
    """

    @abstractmethod
    def log_event(self, event: Dict[str, Any]):
        """
        Enregistre un événement dans le journal des événements.

        :param event: L'événement à enregistrer.
        """
        pass

    @abstractmethod
    def add_observer(self, observer: Callable[[str, datetime], None]):
        """
        Ajoute un observateur pour les événements.

        :param observer: La fonction observateur.
        """
        pass

    @abstractmethod
    def notify_observers(self, event_name: str, timestamp: datetime):
        """
        Notifie tous les observateurs d'un événement.

        :param event_name: Le nom de l'événement.
        :param timestamp: Le timestamp de l'événement.
        """
        pass

    @abstractmethod
    def export_events(self) -> str:
        """
        Exporte les événements en format JSON.

        :return: Les événements en format JSON.
        """
        pass

    @abstractmethod
    def import_events(self, events_json: str):
        """
        Importe les événements à partir d'un format JSON.

        :param events_json: Les événements en format JSON.
        """
        pass
