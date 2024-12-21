from datetime import datetime
from typing import Any
from abc import ABC, abstractmethod


class IEvent(ABC):
    """
    Interface pour les événements.
    """

    @abstractmethod
    def get_name(self) -> str:
        """
        Retourne le nom de l'événement.

        :return: Le nom de l'événement.
        """
        pass

    @abstractmethod
    def get_timestamp(self) -> datetime:
        """
        Retourne le timestamp de l'événement.

        :return: Le timestamp de l'événement.
        """
        pass

    @abstractmethod
    def get_data(self) -> Any:
        """
        Retourne les données de l'événement.

        :return: Les données de l'événement.
        """
        pass
