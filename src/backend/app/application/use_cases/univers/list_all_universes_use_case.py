from sqlalchemy.orm import Session
from app.application.interfaces.universe_interface import IUniverseRepository
from app.infrastructure.database.postgresql.models.universe import Universe
from typing import List, Tuple
import logging

logger = logging.getLogger(__name__)


class ListAllUniversesUseCase:
    """
    Cas d'utilisation pour lister tous les univers avec pagination.
    """

    def __init__(self, repository: IUniverseRepository):
        """
        Initialise le cas d'utilisation avec un repository d'univers.

        :param repository: Instance conforme à IUniverseRepository.
        """
        self.repository = repository

    def execute(
        self, db: Session, page: int, size: int, order_by: str
    ) -> Tuple[List[Universe], int]:
        """
        Liste tous les univers avec pagination.

        :param db: Session SQLAlchemy.
        :param page: Numéro de la page.
        :param size: Nombre d'éléments par page.
        :param order_by: Champ utilisé pour trier les résultats.
        :return: Liste des univers et le nombre total d'univers.
        :raises ValueError: Si les paramètres de pagination ou de tri sont invalides.
        """
        if page < 1 or size < 1:
            logger.error(f"Pagination invalide : page={page}, size={size}")
            raise ValueError("Les paramètres de pagination doivent être positifs.")
        if not hasattr(Universe, order_by):
            logger.error(f"Champ de tri invalide : {order_by}")
            raise ValueError(f"Champ de tri invalide : {order_by}")

        offset = (page - 1) * size
        universes = self.repository.list_all(
            offset=offset, limit=size, order_by=order_by
        )
        total = self.repository.count_all()
        logger.info(
            f"Récupération de {len(universes)} univers (page={page}, size={size})."
        )
        return universes, total
