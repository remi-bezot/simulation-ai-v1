import json
import logging
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.core.exceptions.handlers import handle_repository_exception

logger = logging.getLogger(__name__)


class EventRepository:
    """
    Repository pour gérer les logs d'événements en mémoire.
    Peut être étendu pour supporter un stockage persistant.
    """

    def __init__(self, db: Session):
        """
        Initialise le repository avec un journal des événements en mémoire.
        """
        self.db = db
        self._event_log: List[Dict[str, Any]] = []

    def add_event(self, event_name: str, timestamp: str) -> Dict[str, Any]:
        """
        Ajoute un événement au log.

        :param event_name: Nom de l'événement.
        :param timestamp: Horodatage de l'événement.
        :return: Détails de l'événement ajouté.
        :raises ValueError: Si les données sont invalides.
        """
        if not event_name.strip():
            logger.error("Nom de l'événement vide ou invalide.")
            raise ValueError("Le nom de l'événement ne peut pas être vide.")
        if not timestamp.strip():
            logger.error("Horodatage vide ou invalide.")
            raise ValueError("L'horodatage ne peut pas être vide.")

        event_details = {"event_name": event_name, "timestamp": timestamp}
        self._event_log.append(event_details)
        logger.info(
            f"Événement ajouté : {event_details}. Total d'événements : {len(self._event_log)}"
        )
        return event_details

    def get_all_events(self) -> List[Dict[str, Any]]:
        """
        Retourne tous les événements enregistrés.

        :return: Liste des événements.
        """
        logger.info(f"Récupération de {len(self._event_log)} événements.")
        return self._event_log

    def export_to_file(self, filepath: str) -> None:
        """
        Exporte les événements dans un fichier JSON.

        :param filepath: Chemin du fichier de destination.
        :raises ValueError: Si le chemin est vide ou invalide.
        :raises RuntimeError: En cas d'erreur d'exportation.
        """
        if not filepath.strip():
            logger.error("Le chemin du fichier est vide ou invalide.")
            raise ValueError("Le chemin du fichier ne peut pas être vide.")
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(self._event_log, file, indent=4)
            logger.info(
                f"Logs exportés avec succès vers {filepath}. Total d'événements : {len(self._event_log)}"
            )
        except IOError as e:
            logger.error(f"Erreur lors de l'exportation des logs : {e}")
            raise RuntimeError(f"Erreur lors de l'exportation des logs : {e}")

    def import_from_file(self, filepath: str) -> None:
        """
        Importe des événements depuis un fichier JSON.

        :param filepath: Chemin du fichier source.
        :raises ValueError: Si le chemin est vide ou invalide.
        :raises RuntimeError: En cas d'erreur d'importation.
        """
        if not filepath.strip():
            logger.error("Le chemin du fichier est vide ou invalide.")
            raise ValueError("Le chemin du fichier ne peut pas être vide.")
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                self._event_log = json.load(file)
            logger.info(
                f"Logs importés avec succès depuis {filepath}. Total d'événements : {len(self._event_log)}"
            )
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Erreur lors de l'importation des logs : {e}")
            raise RuntimeError(f"Erreur lors de l'importation des logs : {e}")

    def import_events_from_json(self, filepath: str) -> None:
        """
        Importe des événements depuis un fichier JSON.

        :param filepath: Chemin du fichier source.
        :raises ValueError: Si le chemin est vide ou invalide.
        :raises RuntimeError: En cas d'erreur d'importation.
        """
        if not filepath.strip():
            logger.error("Le chemin du fichier est vide ou invalide.")
            raise ValueError("Le chemin du fichier ne peut pas être vide.")
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                self._event_log = json.load(file)
            logger.info(
                f"Logs importés avec succès depuis {filepath}. Total d'événements : {len(self._event_log)}"
            )
        except (IOError, json.JSONDecodeError) as e:
            handle_repository_exception(
                self.db, e, "Erreur lors de l'importation des logs"
            )

    def get_events(self) -> List[Dict[str, Any]]:
        """
        Retourne la liste des événements importés.

        :return: Liste des événements.
        """
        return self._event_log
