from sqlalchemy.orm import Session
from app.application.interfaces.multiverse_interface import IMultiverseRepository
from app.infrastructure.database.postgresql.models.multiverse import Multiverse
from typing import List, Tuple
import logging

logger = logging.getLogger(__name__)


class ListAllMultiversesUseCase:
    """
    Cas d'utilisation pour lister tous les multivers avec pagination.
    """

    def __init__(self, repository: IMultiverseRepository):
        """
        Initialise le cas d'utilisation avec un repository de multivers.

        :param repository: Instance conforme à IMultiverseRepository.
        """
        self.repository = repository

    def execute(
        self, db: Session, page: int, size: int, order_by: str
    ) -> Tuple[List[Multiverse], int]:
        """
        Liste tous les multivers avec pagination.

        :param db: Session SQLAlchemy.
        :param page: Numéro de la page.
        :param size: Nombre d'éléments par page.
        :param order_by: Champ utilisé pour trier les résultats.
        :return: Liste des multivers et le nombre total de multivers.
        :raises ValueError: Si les paramètres de pagination ou de tri sont invalides.
        """
        if page < 1 or size < 1:
            logger.error(f"Pagination invalide : page={page}, size={size}")
            raise ValueError("Les paramètres de pagination doivent être positifs.")
        if not hasattr(Multiverse, order_by):
            logger.error(f"Champ de tri invalide : {order_by}")
            raise ValueError(f"Champ de tri invalide : {order_by}")

        offset = (page - 1) * size
        multiverses = self.repository.list_all(
            offset=offset, limit=size, order_by=order_by
        )
        total = self.repository.count_all()
        logger.info(
            f"Récupération de {len(multiverses)} multivers (page={page}, size={size})."
        )
        return multiverses, total
