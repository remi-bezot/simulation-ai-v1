from sqlalchemy.orm import Session
from app.application.interfaces.event_interface import EventInterface
import logging

logger = logging.getLogger(__name__)


class ImportEventLogsUseCase:
    """
    Cas d'utilisation pour importer les logs des événements.
    """

    def __init__(self, event_service: EventInterface):
        """
        Initialise le cas d'utilisation avec un service d'événements.

        :param event_service: Instance conforme à EventInterface.
        """
        self.event_service = event_service

    def execute(self, db: Session, filepath: str) -> None:
        """
        Importe des logs d'événements depuis un fichier.

        :param db: Session SQLAlchemy.
        :param filepath: Chemin du fichier source.
        :raises RuntimeError: En cas d'erreur pendant l'importation.
        """
        if not filepath.strip():
            logger.error("Le chemin du fichier est vide ou invalide.")
            raise ValueError("Le chemin du fichier ne peut pas être vide.")

        logger.info(
            f"Début de l'importation des logs des événements depuis : {filepath}"
        )
        try:
            self.event_service.import_event_log(filepath)
            logger.info(f"Logs des événements importés avec succès depuis : {filepath}")
        except Exception as e:
            logger.error(f"Erreur lors de l'importation des logs des événements : {e}")
            raise RuntimeError(
                f"Erreur lors de l'importation des logs des événements : {e}"
            )
