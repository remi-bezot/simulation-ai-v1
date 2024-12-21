from sqlalchemy.orm import Session
from app.application.interfaces.multiverse_interface import IMultiverseRepository
from app.core.exceptions import MultiverseNotFoundError
import logging

logger = logging.getLogger(__name__)


class DeleteMultiverseUseCase:
    """
    Cas d'utilisation pour supprimer un multivers.
    """

    def __init__(self, repository: IMultiverseRepository):
        """
        Initialise le cas d'utilisation avec un repository de multivers.

        :param repository: Instance conforme à IMultiverseRepository.
        """
        self.repository = repository

    def execute(self, db: Session, multiverse_id: int) -> Dict[str, str]:
        """
        Supprime un multivers.

        :param db: Session SQLAlchemy.
        :param multiverse_id: ID du multivers à supprimer.
        :return: Message de confirmation sous forme de dictionnaire.
        :raises MultiverseNotFoundError: Si le multivers n'existe pas.
        :raises RuntimeError: En cas d'erreur pendant la suppression.
        """
        # Vérification de l'existence du multivers
        multiverse = self.repository.get_by_id(multiverse_id)
        if not multiverse:
            logger.error(f"Multivers non trouvé : ID={multiverse_id}")
            raise MultiverseNotFoundError(multiverse_id)

        try:
            # Suppression du multivers
            self.repository.delete(multiverse)
            logger.info(f"Multivers ID={multiverse_id} supprimé avec succès.")
            return {"message": f"Multivers ID {multiverse_id} supprimé avec succès."}
        except Exception as e:
            db.rollback()
            logger.error(
                f"Erreur lors de la suppression du multivers ID={multiverse_id} : {e}"
            )
            raise RuntimeError(f"Erreur lors de la suppression du multivers : {e}")
