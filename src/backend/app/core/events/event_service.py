import logging
from datetime import datetime
from typing import List, Callable, Dict, Any
import json

# Configuration du logger centralisé
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class EventManager:
    """
    Gestionnaire d'événements modulaire avec support pour les logs,
    les observateurs, l'exportation des événements et l'importation.
    """

    def __init__(self):
        self._event_log: List[Dict[str, Any]] = []
        self._observers: List[Callable[[str, datetime], None]] = []

    def _log_event(self, event_name: str) -> Dict[str, Any]:
        timestamp = datetime.now()
        event_details = {"event_name": event_name, "timestamp": timestamp.isoformat()}
        self._event_log.append(event_details)
        logger.info("Événement enregistré : '%s' à %s", event_name, timestamp)
        return event_details

    def register_observer(self, observer: Callable[[str, datetime], None]) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
            logger.info("Observateur enregistré : %s", observer.__name__)

    def trigger_event(self, event_name: str) -> Dict[str, Any]:
        if not event_name.strip():
            raise ValueError("Le nom de l'événement ne peut pas être vide.")
        event_details = self._log_event(event_name)

        for observer in self._observers:
            try:
                observer(event_name, datetime.fromisoformat(event_details["timestamp"]))
            except Exception as e:
                logger.error("Erreur lors de la notification de l'observateur : %s", e)

        return {"message": f"Événement '{event_name}' déclenché avec succès."}

    def get_event_log(self) -> List[Dict[str, Any]]:
        logger.info("Historique des événements récupéré.")
        return self._event_log
