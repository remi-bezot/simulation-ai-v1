from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.application.interfaces.universe_interface import IUniverseService
from app.application.repositories.universe_repository import UniverseRepository
from app.infrastructure.database.postgresql.models.universe import Universe
from app.schemas.universe import UniverseCreate, UniverseUpdate
from app.application.utils.exceptions import UniverseNotFoundError
import logging

logger = logging.getLogger(__name__)


class UniverseService(IUniverseService):
    """
    Service pour gérer les univers.
    """

    def __init__(self, repository: UniverseRepository):
        """
        Initialise le service avec un repository injecté.

        :param repository: Instance de UniverseRepository.
        """
        self.repository = repository

    def create_universe(self, db: Session, universe_data: Dict[str, Any]) -> Universe:
        """
        Crée un nouvel univers.

        :param db: Session SQLAlchemy utilisée pour la requête.
        :param universe_data: Dictionnaire contenant les données de l'univers à créer.
        :return: Instance de l'univers créé.
        :raises ValueError: Si les données de l'univers sont invalides.
        """
        universe = Universe(**universe_data)
        self.repository.create(universe)
        return universe

    def update_universe(
        self, db: Session, universe_id: int, updates: Dict[str, Any]
    ) -> Universe:
        """
        Met à jour un univers existant.

        :param db: Session SQLAlchemy utilisée pour la requête.
        :param universe_id: ID de l'univers à mettre à jour.
        :param updates: Dictionnaire contenant les mises à jour.
        :return: Instance de l'univers mis à jour.
        :raises UniverseNotFoundError: Si l'univers n'existe pas.
        """
        universe = self.repository.get(universe_id)
        if not universe:
            raise ValueError("Universe not found")
        for key, value in updates.items():
            setattr(universe, key, value)
        self.repository.update(universe)
        return universe

    def delete_universe(self, db: Session, universe_id: int) -> Dict[str, str]:
        """
        Supprime un univers.

        :param db: Session SQLAlchemy utilisée pour la requête.
        :param universe_id: ID de l'univers à supprimer.
        :return: Message de confirmation sous forme de dictionnaire.
        :raises UniverseNotFoundError: Si l'univers n'existe pas.
        """
        universe = self.repository.get(universe_id)
        if not universe:
            raise ValueError("Universe not found")
        self.repository.delete(universe)
        return {"message": "Universe deleted successfully"}

    def list_all_universes(
        self, db: Session, page: int, size: int, order_by: str
    ) -> List[Universe]:
        """
        Liste tous les univers avec pagination.

        :param db: Session SQLAlchemy utilisée pour la requête.
        :param page: Numéro de la page.
        :param size: Nombre d'éléments par page.
        :param order_by: Champ utilisé pour trier les résultats.
        :return: Liste des univers.
        :raises ValueError: Si les paramètres de pagination sont invalides.
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
        logger.info(f"{len(universes)} univers récupérés (page={page}, size={size}).")
        return universes
