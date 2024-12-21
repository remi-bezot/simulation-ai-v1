from typing import Callable, List, Dict, Any
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class EventProcessorUseCase:
    """
    Cas d'utilisation pour traiter les événements et notifier les observateurs.
    """

    def __init__(self):
        self._observers: List[Callable[[str, datetime], None]] = []

    def register_observer(self, observer: Callable[[str, datetime], None]) -> None:
        """
        Enregistre un observateur à notifier lors d'un événement.

        :param observer: Fonction ou méthode à exécuter lors d'un événement.
        """
        if observer not in self._observers:
            self._observers.append(observer)
            logger.info(f"Observateur enregistré : {observer.__name__}")
        else:
            logger.warning(f"Observateur déjà enregistré : {observer.__name__}")

    def execute(self, event_name: str, event_data: Dict[str, Any]) -> None:
        """
        Exécute le traitement d'un événement et notifie les observateurs.

        :param event_name: Nom de l'événement.
        :param event_data: Données associées à l'événement.
        :raises ValueError: Si le nom de l'événement est vide.
        """
        if not event_name.strip():
            logger.error("Le nom de l'événement est vide.")
            raise ValueError("Le nom de l'événement ne peut pas être vide.")

        logger.info(f"Traitement de l'événement : {event_name}")
        timestamp = datetime.now()

        # Notifier tous les observateurs
        for observer in self._observers:
            try:
                observer(event_name, timestamp)
                logger.info(f"Observateur exécuté avec succès : {observer.__name__}")
            except Exception as e:
                logger.error(
                    f"Erreur lors de la notification de l'observateur {observer.__name__} : {e}"
                )

        logger.info(f"Événement '{event_name}' traité avec succès.")

    def clear_observers(self) -> None:
        """
        Supprime tous les observateurs enregistrés.
        """
        self._observers.clear()
        logger.info("Tous les observateurs ont été supprimés.")
