import logging
from datetime import datetime
from typing import List, Callable, Dict, Any
from app.application.repositories.event_repository import EventRepository
from app.application.interfaces.event_interface import IEventManager

# Configuration du logger
logger = logging.getLogger(__name__)


class EventManager(IEventManager):
    """
    Gestionnaire d'événements implémentant IEventManager.
    """

    def __init__(self, repository: EventRepository):
        """
        Initialise le gestionnaire d'événements avec un repository.

        :param repository: Instance de EventRepository pour la gestion des données.
        """
        self.repository = repository
        self._observers: List[Callable[[str, datetime], None]] = []

    def register_observer(self, observer: Callable[[str, datetime], None]) -> None:
        """
        Enregistre un observateur pour les notifications d'événements.

        :param observer: Fonction appelée à chaque événement déclenché.
        """
        if observer not in self._observers:
            self._observers.append(observer)
            logger.info(
                "Observateur enregistré : %s", getattr(observer, "__name__", "inconnu")
            )
        else:
            logger.warning(
                "Observateur déjà enregistré : %s",
                getattr(observer, "__name__", "inconnu"),
            )

    def trigger_event(self, event_name: str) -> Dict[str, Any]:
        """
        Déclenche un événement et notifie les observateurs.

        :param event_name: Nom de l'événement.
        :return: Détails de l'événement déclenché.
        """
        if not event_name.strip():
            raise ValueError("Le nom de l'événement ne peut pas être vide.")

        timestamp = datetime.now().isoformat()
        event_details = self.repository.add_event(event_name, timestamp)

        for observer in self._observers:
            try:
                observer(event_name, datetime.fromisoformat(timestamp))
            except Exception as e:
                logger.error(
                    "Erreur avec l'observateur '%s': %s",
                    getattr(observer, "__name__", "inconnu"),
                    e,
                )

        logger.info("Événement déclenché : %s", event_name)
        return {
            "message": f"Événement '{event_name}' déclenché.",
            "event_details": event_details,
        }

    def get_event_log(self) -> List[Dict[str, Any]]:
        """
        Retourne tous les événements enregistrés.

        :return: Liste des événements.
        """
        return self.repository.get_all_events()

    def export_event_log(self, filepath: str) -> None:
        """
        Exporte les logs des événements dans un fichier.

        :param filepath: Chemin du fichier de destination.
        """
        self.repository.export_to_file(filepath)
        logger.info("Logs exportés vers %s", filepath)

    def import_event_log(self, filepath: str) -> None:
        """
        Importe des logs d'événements depuis un fichier.

        :param filepath: Chemin du fichier source.
        """
        self.repository.import_from_file(filepath)
        logger.info("Logs importés depuis %s", filepath)
