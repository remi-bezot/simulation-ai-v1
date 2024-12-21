from sqlalchemy.orm import Session
from app.application.interfaces.event_interface import EventInterface
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


class ListEventsUseCase:
    """
    Cas d'utilisation pour lister tous les événements.
    """

    def __init__(self, event_service: EventInterface):
        """
        Initialise le cas d'utilisation avec un service d'événements.

        :param event_service: Instance conforme à EventInterface.
        """
        self.event_service = event_service

    def execute(self, db: Session) -> List[Dict[str, Any]]:
        """
        Récupère la liste de tous les événements.

        :param db: Session SQLAlchemy.
        :return: Liste des événements enregistrés.
        """
        logger.info("Début de la récupération de tous les événements.")
        try:
            events = self.event_service.get_event_log()
            logger.info(f"{len(events)} événements récupérés.")
            return events
        except Exception as e:
            logger.error(f"Erreur lors de la récupération des événements : {e}")
            raise RuntimeError(f"Erreur lors de la récupération des événements : {e}")
