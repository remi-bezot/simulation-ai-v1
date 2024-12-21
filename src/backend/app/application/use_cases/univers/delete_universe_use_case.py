from sqlalchemy.orm import Session
from app.application.interfaces.universe_interface import IUniverseRepository
from app.core.exceptions import UniverseNotFoundError
import logging

logger = logging.getLogger(__name__)


class DeleteUniverseUseCase:
    """
    Cas d'utilisation pour supprimer un univers existant.
    """

    def __init__(self, repository: IUniverseRepository):
        """
        Initialise le use case avec un repository.

        :param repository: Instance de IUniverseRepository.
        """
        self.repository = repository

    def execute(self, db: Session, universe_id: int) -> dict:
        """
        Supprime un univers existant.

        :param db: Session SQLAlchemy.
        :param universe_id: ID de l'univers à supprimer.
        :return: Message de confirmation.
        :raises UniverseNotFoundError: Si l'univers n'existe pas.
        """
        # Vérification de l'existence de l'univers
        universe = self.repository.get_by_id(universe_id)
        if not universe:
            logger.error(f"Univers non trouvé : ID={universe_id}")
            raise UniverseNotFoundError(universe_id)

        try:
            # Suppression de l'univers
            self.repository.delete(universe)
            db.commit()
            logger.info(f"Univers ID={universe_id} supprimé avec succès.")
            return {"message": f"Univers ID {universe_id} supprimé avec succès."}
        except Exception as e:
            db.rollback()
            logger.error(
                f"Erreur lors de la suppression de l'univers ID={universe_id} : {e}"
            )
            raise RuntimeError(f"Erreur lors de la suppression de l'univers : {e}")
