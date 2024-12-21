from sqlalchemy.orm import Session
from app.application.interfaces.multiverse_interface import IMultiverseRepository
from app.infrastructure.database.postgresql.models.multiverse import Multiverse
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class CreateMultiverseUseCase:
    """
    Cas d'utilisation pour créer un multivers.
    """

    def __init__(self, repository: IMultiverseRepository):
        """
        Initialise le cas d'utilisation avec un repository de multivers.

        :param repository: Instance conforme à IMultiverseRepository.
        """
        self.repository = repository

    def execute(self, db: Session, data: Dict[str, Any]) -> Multiverse:
        """
        Crée un nouveau multivers.

        :param db: Session SQLAlchemy.
        :param data: Données du multivers.
        :return: Instance du multivers créé.
        :raises ValueError: Si le nom du multivers est invalide.
        :raises RuntimeError: En cas d'erreur pendant la création.
        """
        if not data.get("name", "").strip():
            logger.error("Le nom du multivers est vide ou invalide.")
            raise ValueError("Le nom du multivers est obligatoire.")

        try:
            # Création de l'objet multivers
            new_multiverse = Multiverse(
                name=data["name"].strip(),
                description=data.get("description", ""),
                properties=data.get("properties", {}),
            )
            # Enregistrement dans le repository
            created_multiverse = self.repository.create(new_multiverse)
            logger.info(
                f"Multivers '{created_multiverse.name}' créé avec succès (ID={created_multiverse.id})."
            )
            return created_multiverse
        except Exception as e:
            logger.error(f"Erreur lors de la création du multivers : {e}")
            raise RuntimeError(f"Erreur lors de la création du multivers : {e}")
