from sqlalchemy.orm import Session
from app.application.interfaces.universe_interface import IUniverseRepository
from app.schemas.universe import UniverseCreate
from app.infrastructure.database.postgresql.models.universe import Universe
from app.core.exceptions import MultiverseNotFoundError
import logging

logger = logging.getLogger(__name__)


class CreateUniverseUseCase:
    """
    Cas d'utilisation pour créer un univers.
    """

    def __init__(self, repository: IUniverseRepository):
        """
        Initialise le cas d'utilisation avec un repository d'univers.

        :param repository: Instance conforme à IUniverseRepository.
        """
        self.repository = repository

    def execute(
        self, db: Session, multiverse_id: int, data: UniverseCreate
    ) -> Universe:
        """
        Crée un nouvel univers.

        :param db: Session SQLAlchemy.
        :param multiverse_id: ID du multivers auquel l'univers appartient.
        :param data: Données pour créer l'univers.
        :return: Univers créé.
        :raises MultiverseNotFoundError: Si le multivers n'existe pas.
        :raises RuntimeError: En cas d'erreur pendant la création.
        """
        # Vérification de l'existence du multivers
        multiverse = self.repository.get_multiverse_by_id(multiverse_id)
        if not multiverse:
            logger.error(f"Multivers non trouvé : ID={multiverse_id}")
            raise MultiverseNotFoundError(multiverse_id)

        try:
            # Création de l'univers
            new_universe = Universe(
                name=data.name.strip(),
                description=data.description or "",
                properties=data.properties or {},
                multiverse=multiverse,  # Relation avec le multivers
            )
            db.add(new_universe)
            db.commit()
            db.refresh(new_universe)
            logger.info(
                f"Univers '{new_universe.name}' créé avec succès dans le multivers ID={multiverse_id}."
            )
            return new_universe
        except Exception as e:
            db.rollback()
            logger.error(f"Erreur lors de la création de l'univers : {e}")
            raise RuntimeError(f"Erreur lors de la création de l'univers : {e}")
