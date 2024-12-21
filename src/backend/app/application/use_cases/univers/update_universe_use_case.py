from sqlalchemy.orm import Session
from app.infrastructure.database.postgresql.models.universe import Universe
from app.schemas.universe import UniverseUpdate
from app.application.interfaces.universe_interface import IUniverseRepository
from app.core.exceptions import UniverseNotFoundError
import logging

logger = logging.getLogger(__name__)


class UpdateUniverseUseCase:
    """
    Cas d'utilisation pour mettre à jour un univers.
    """

    def __init__(self, repository: IUniverseRepository):
        """
        Initialise le cas d'utilisation avec un repository d'univers.

        :param repository: Instance conforme à IUniverseRepository.
        """
        self.repository = repository

    def execute(
        self, db: Session, universe_id: int, updates: UniverseUpdate
    ) -> Universe:
        """
        Met à jour un univers.

        :param db: Session SQLAlchemy.
        :param universe_id: ID de l'univers à mettre à jour.
        :param updates: Données pour mettre à jour l'univers.
        :return: Univers mis à jour.
        :raises UniverseNotFoundError: Si l'univers n'existe pas.
        """
        # Vérification de l'existence de l'univers
        universe = self.repository.get_by_id(universe_id)
        if not universe:
            logger.error(f"Univers non trouvé : ID={universe_id}")
            raise UniverseNotFoundError(universe_id)

        # Mise à jour des champs
        if updates.name:
            universe.name = updates.name.strip()
        if updates.description is not None:
            universe.description = updates.description
        if updates.properties:
            universe.properties.update(updates.properties.dict())

        # Persistance des modifications
        db.commit()
        db.refresh(universe)
        logger.info(f"Univers ID={universe_id} mis à jour avec succès.")
        return universe
