from sqlalchemy.orm import Session
from app.application.interfaces.multiverse_interface import IMultiverseRepository
from app.schemas.multiverse import MultiverseUpdate
from app.infrastructure.database.postgresql.models.multiverse import Multiverse
from app.core.exceptions import MultiverseNotFoundError
import logging

logger = logging.getLogger(__name__)


class UpdateMultiverseUseCase:
    """
    Cas d'utilisation pour mettre à jour un multivers.
    """

    def __init__(self, repository: IMultiverseRepository):
        """
        Initialise le cas d'utilisation avec un repository de multivers.

        :param repository: Instance conforme à IMultiverseRepository.
        """
        self.repository = repository

    def execute(
        self, db: Session, multiverse_id: int, updates: MultiverseUpdate
    ) -> Multiverse:
        """
        Met à jour un multivers.

        :param db: Session SQLAlchemy.
        :param multiverse_id: ID du multivers à mettre à jour.
        :param updates: Données pour mettre à jour le multivers.
        :return: Multivers mis à jour.
        :raises MultiverseNotFoundError: Si le multivers n'existe pas.
        """
        # Vérification de l'existence du multivers
        multiverse = self.repository.get_by_id(multiverse_id)
        if not multiverse:
            logger.error(f"Multivers non trouvé : ID={multiverse_id}")
            raise MultiverseNotFoundError(multiverse_id)

        # Mise à jour des champs
        if updates.name:
            multiverse.name = updates.name.strip()
        if updates.description is not None:
            multiverse.description = updates.description
        if updates.properties:
            multiverse.properties.update(updates.properties.dict())

        # Persistance des modifications
        db.commit()
        db.refresh(multiverse)
        logger.info(f"Multivers ID={multiverse_id} mis à jour avec succès.")
        return multiverse
