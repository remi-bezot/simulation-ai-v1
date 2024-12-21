import logging
from datetime import datetime
from typing import List, Callable, Dict, Any
import json
from app.core.events.interfaces.i_event_manager import IEventManager

# Configuration du logger centralisé
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class EventManager(IEventManager):
    """
    Gestionnaire d'événements modulaire avec support pour les logs,
    les observateurs, l'exportation des événements et l'importation.
    """

    def __init__(self):
        self._event_log: List[Dict[str, Any]] = []
        self._observers: List[Callable[[str, datetime], None]] = []

    def log_event(self, event: Dict[str, Any]):
        """
        Enregistre un événement dans le journal des événements.

        :param event: L'événement à enregistrer.
        """
        self._event_log.append(event)
        logger.info(f"Event logged: {event}")

    def add_observer(self, observer: Callable[[str, datetime], None]):
        """
        Ajoute un observateur pour les événements.

        :param observer: La fonction observateur.
        """
        self._observers.append(observer)

    def notify_observers(self, event_name: str, timestamp: datetime):
        """
        Notifie tous les observateurs d'un événement.

        :param event_name: Le nom de l'événement.
        :param timestamp: Le timestamp de l'événement.
        """
        for observer in self._observers:
            observer(event_name, timestamp)

    def export_events(self) -> str:
        """
        Exporte les événements en format JSON.

        :return: Les événements en format JSON.
        """
        return json.dumps(self._event_log, default=str)

    def import_events(self, events_json: str):
        """
        Importe les événements à partir d'un format JSON.

        :param events_json: Les événements en format JSON.
        """
        self._event_log = json.loads(events_json)
