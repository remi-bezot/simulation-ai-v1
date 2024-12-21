from sqlalchemy.orm import Session
from app.application.interfaces.event_interface import EventInterface
import logging

logger = logging.getLogger(__name__)


class ExportEventLogsUseCase:
    """
    Cas d'utilisation pour exporter les logs des événements.
    """

    def __init__(self, event_service: EventInterface):
        """
        Initialise le cas d'utilisation avec un service d'événements.

        :param event_service: Instance conforme à EventInterface.
        """
        self.event_service = event_service

    def execute(self, db: Session, filepath: str) -> None:
        """
        Exporte les logs des événements vers un fichier.

        :param db: Session SQLAlchemy.
        :param filepath: Chemin du fichier de destination.
        :raises RuntimeError: En cas d'erreur pendant l'exportation.
        """
        if not filepath.strip():
            logger.error("Le chemin du fichier est vide ou invalide.")
            raise ValueError("Le chemin du fichier ne peut pas être vide.")

        logger.info(f"Début de l'exportation des logs des événements vers : {filepath}")
        try:
            self.event_service.export_event_log(filepath)
            logger.info(f"Logs des événements exportés avec succès vers : {filepath}")
        except Exception as e:
            logger.error(f"Erreur lors de l'exportation des logs des événements : {e}")
            raise RuntimeError(
                f"Erreur lors de l'exportation des logs des événements : {e}"
            )
