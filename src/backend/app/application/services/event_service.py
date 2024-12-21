from sqlalchemy.orm import Session
from app.application.interfaces.event_interface import EventInterface
from src.backend.app.application.managers.event_manager import EventManager
from app.application.repositories.event_repository import EventRepository
from app.core.logging.logger import logger
from typing import List, Dict, Any


class EventService(EventInterface):
    """
    Service pour orchestrer EventManager.
    Utilisé pour les opérations liées aux événements.
    """

    def __init__(self, db: Session, repository: EventRepository = None):
        """
        Initialise le service avec un EventManager et un EventRepository.

        :param db: Session SQLAlchemy pour la base de données.
        :param repository: Référentiel d'événements, injecté pour respecter DIP.
        """
        self.repository = repository or EventRepository(db)
        self.event_manager = EventManager(self.repository)

    def trigger_event(self, event_name: str) -> Dict[str, Any]:
        """
        Déclenche un événement et retourne les détails.

        :param event_name: Nom de l'événement.
        :return: Dictionnaire avec les détails de l'événement.
        :raises ValueError: Si le nom de l'événement est vide.
        """
        if not event_name.strip():
            logger.error("Le nom de l'événement est vide ou invalide.")
            raise ValueError("Le nom de l'événement ne peut pas être vide.")
        logger.info(f"Déclenchement de l'événement : {event_name}")
        return self.event_manager.trigger_event(event_name)

    def get_event_log(self) -> List[Dict[str, Any]]:
        """
        Retourne tous les événements enregistrés.

        :return: Liste des événements.
        """
        logger.info("Récupération de l'historique des événements.")
        try:
            return self.event_manager.get_event_log()
        except Exception as e:
            logger.error(f"Erreur lors de la récupération des logs : {e}")
            raise RuntimeError(f"Erreur lors de la récupération des logs : {e}")

    def export_event_log(self, filepath: str) -> None:
        """
        Exporte les événements vers un fichier JSON.

        :param filepath: Chemin du fichier de destination.
        :raises ValueError: Si le chemin est vide ou invalide.
        :raises RuntimeError: En cas d'erreur pendant l'exportation.
        """
        if not filepath.strip():
            logger.error("Le chemin du fichier est vide ou invalide.")
            raise ValueError("Le chemin du fichier ne peut pas être vide.")
        try:
            self.event_manager.export_event_log(filepath)
            logger.info(f"Exportation des logs dans le fichier : {filepath}")
        except Exception as e:
            logger.error(f"Erreur lors de l'exportation des logs : {e}")
            raise RuntimeError(f"Erreur lors de l'exportation des logs : {e}")

    def import_event_log(self, filepath: str) -> None:
        """
        Importe des événements depuis un fichier JSON.

        :param filepath: Chemin du fichier source.
        :raises ValueError: Si le chemin est vide ou invalide.
        :raises RuntimeError: En cas d'erreur pendant l'importation.
        """
        if not filepath.strip():
            logger.error("Le chemin du fichier est vide ou invalide.")
            raise ValueError("Le chemin du fichier ne peut pas être vide.")
        try:
            self.event_manager.import_event_log(filepath)
            logger.info(f"Importation des logs depuis le fichier : {filepath}")
        except Exception as e:
            logger.error(f"Erreur lors de l'importation des logs : {e}")
            raise RuntimeError(f"Erreur lors de l'importation des logs : {e}")
