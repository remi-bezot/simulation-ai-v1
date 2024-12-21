from sqlalchemy.orm import Session
from app.application.interfaces.event_interface import EventInterface
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class TriggerEventUseCase:
    """
    Cas d'utilisation pour déclencher un événement.
    """

    def __init__(self, event_service: EventInterface):
        """
        Initialise le cas d'utilisation avec un service d'événements.

        :param event_service: Instance conforme à EventInterface.
        """
        self.event_service = event_service

    def execute(self, db: Session, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Déclenche un événement via le service.

        :param db: Session SQLAlchemy.
        :param event_data: Données de l'événement.
        :return: Résultat de l'exécution de l'événement.
        :raises ValueError: Si le nom de l'événement est invalide.
        """
        event_name = event_data.get("name", "").strip()
        if not event_name:
            logger.error("Le nom de l'événement est vide ou invalide.")
            raise ValueError("Le nom de l'événement est obligatoire.")

        logger.info(f"Déclenchement de l'événement : {event_name}")
        try:
            result = self.event_service.trigger_event(event_name)
            logger.info(f"Événement '{event_name}' déclenché avec succès.")
            return result
        except Exception as e:
            logger.error(f"Erreur lors du déclenchement de l'événement : {e}")
            raise RuntimeError(f"Erreur lors du déclenchement de l'événement : {e}")
