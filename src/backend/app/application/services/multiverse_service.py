from typing import Tuple, List, Dict
from app.schemas.multiverse import MultiverseCreate, MultiverseUpdate
from app.infrastructure.database.postgresql.models.multiverse import Multiverse
from app.application.interfaces.multiverse_interface import IMultiverseService
from app.application.utils.exceptions import MultiverseNotFoundError
from app.application.utils.decorators import handle_sqlalchemy_errors
from app.application.repositories.multiverse_repository import MultiverseRepository
from src.backend.app.core.logging.logging_config import logger


class MultiverseService(IMultiverseService):
    def __init__(self, repository: MultiverseRepository):
        """
        Initialise le service avec un repository injecté.

        :param repository: Instance de MultiverseRepository.
        """
        self.repository = repository

    @handle_sqlalchemy_errors
    def create_multiverse(self, data: MultiverseCreate) -> Multiverse:
        """
        Crée un nouveau multivers.
        """
        new_multiverse = Multiverse(**data.dict())
        self.repository.add(new_multiverse)
        self.repository.commit()
        self.repository.refresh(new_multiverse)
        return new_multiverse

    @handle_sqlalchemy_errors
    def list_multiverses(
        self, page: int = 1, size: int = 10, order_by: str = "id"
    ) -> Tuple[List[Multiverse], int]:
        """
        Liste les multivers avec pagination et tri.

        :param page: Numéro de la page (1 par défaut).
        :param size: Nombre d'éléments par page (10 par défaut).
        :param order_by: Champ utilisé pour trier les résultats.
        :return: Tuple contenant une liste des multivers et le total d'éléments.
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
            f"{len(multiverses)} multivers récupérés (page={page}, size={size})."
        )
        return multiverses, total

    @handle_sqlalchemy_errors
    def update_multiverse(
        self, multiverse_id: int, updates: MultiverseUpdate
    ) -> Multiverse:
        """
        Met à jour un multivers existant.

        :param multiverse_id: ID du multivers à mettre à jour.
        :param updates: Données pour la mise à jour.
        :return: Multivers mis à jour.
        :raises MultiverseNotFoundError: Si le multivers n'existe pas.
        """
        multiverse = self.repository.get_by_id(multiverse_id)
        if not multiverse:
            logger.error(f"Multivers non trouvé : ID={multiverse_id}")
            raise MultiverseNotFoundError(multiverse_id)
        if updates.name:
            multiverse.name = updates.name.strip()
        if updates.description is not None:
            multiverse.description = updates.description
        if updates.properties:
            multiverse.properties.update(updates.properties.dict())
        self.repository.update(multiverse)
        logger.info(
            f"Multivers '{multiverse.name}' mis à jour avec succès (ID={multiverse_id})."
        )
        return multiverse

    @handle_sqlalchemy_errors
    def delete_multiverse(self, multiverse_id: int):
        """
        Supprime un multivers par son ID.
        """
        multiverse = self.repository.get(multiverse_id)
        if not multiverse:
            raise MultiverseNotFoundError(f"Multivers avec l'ID {multiverse_id} non trouvé.")
        self.repository.delete(multiverse)
        self.repository.commit()
