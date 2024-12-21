# Définitions des événements

from datetime import datetime
from typing import Any
from app.core.events.interfaces.i_event import IEvent


class Event(IEvent):
    """
    Classe de base pour les événements.
    """

    def __init__(self, name: str, timestamp: datetime, data: Any):
        self.name = name
        self.timestamp = timestamp
        self.data = data

    def get_name(self) -> str:
        """
        Retourne le nom de l'événement.

        :return: Le nom de l'événement.
        """
        return self.name

    def get_timestamp(self) -> datetime:
        """
        Retourne le timestamp de l'événement.

        :return: Le timestamp de l'événement.
        """
        return self.timestamp

    def get_data(self) -> Any:
        """
        Retourne les données de l'événement.

        :return: Les données de l'événement.
        """
        return self.data
