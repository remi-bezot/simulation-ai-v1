from sqlalchemy.orm import Session
from typing import List
from app.application.interfaces.multiverse_interface import IMultiverseRepository
from app.core.exceptions import MultiverseNotFoundError
import logging

logger = logging.getLogger(__name__)


class ListUniversesInMultiverseUseCase:
    """
    Cas d'utilisation pour lister tous les univers dans un multivers.
    """

    def __init__(self, repository: IMultiverseRepository):
        """
        Initialise le cas d'utilisation avec un repository de multivers.

        :param repository: Instance conforme à IMultiverseRepository.
        """
        self.repository = repository

    def execute(self, db: Session, multiverse_id: int) -> List:
        """
        Liste tous les univers dans un multivers.

        :param db: Session SQLAlchemy.
        :param multiverse_id: ID du multivers.
        :return: Liste des univers dans le multivers.
        :raises MultiverseNotFoundError: Si le multivers n'existe pas.
        """
        logger.info(
            f"Début de la récupération des univers pour le multivers ID={multiverse_id}"
        )

        # Vérification de l'existence du multivers
        multiverse = self.repository.get_by_id(multiverse_id)
        if not multiverse:
            logger.error(f"Multivers non trouvé : ID={multiverse_id}")
            raise MultiverseNotFoundError(multiverse_id)

        # Récupération des univers
        universes = getattr(multiverse, "universes", [])
        logger.info(
            f"{len(universes)} univers récupérés pour le multivers ID={multiverse_id}."
        )
        return universes
