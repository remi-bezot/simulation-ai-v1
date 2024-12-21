from app.application.interfaces.event_interface import EventInterface
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class EventUseCase:
    """
    Cas d'utilisation pour gérer les événements.
    """

    def __init__(self, event_service: EventInterface):
        """
        Initialise le cas d'utilisation avec un service d'événements.

        :param event_service: Instance conforme à EventInterface.
        """
        self.event_service = event_service

    def execute_trigger_event(self, event_name: str) -> Dict[str, Any]:
        """
        Déclenche un événement via le service.

        :param event_name: Nom de l'événement.
        :return: Résultat du déclenchement de l'événement.
        :raises ValueError: Si le nom de l'événement est vide ou invalide.
        """
        if not event_name.strip():
            logger.error("Le nom de l'événement est vide ou invalide.")
            raise ValueError("Le nom de l'événement ne peut pas être vide.")

        logger.info(f"Déclenchement de l'événement : {event_name}")
        return self.event_service.trigger_event(event_name)

    def execute_get_event_log(self) -> List[Dict[str, Any]]:
        """
        Récupère le journal des événements via le service.

        :return: Liste des événements enregistrés.
        """
        logger.info("Récupération du journal des événements.")
        return self.event_service.get_event_log()
