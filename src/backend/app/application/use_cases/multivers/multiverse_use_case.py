from sqlalchemy.orm import Session
from app.application.interfaces.multiverse_interface import IMultiverseService
from app.schemas.multiverse import MultiverseCreate, MultiverseUpdate
from app.infrastructure.database.postgresql.models.multiverse import Multiverse
from typing import List, Dict, Any, Tuple


class CreateMultiverseUseCase:
    """
    Use case pour créer un multivers.
    """

    def __init__(self, service: IMultiverseService):
        """
        Initialise le cas d'utilisation avec un service de multivers.

        :param service: Instance conforme à IMultiverseService.
        """
        self.service = service

    def execute(self, db: Session, data: MultiverseCreate) -> Multiverse:
        """
        Exécute la création d'un multivers.

        :param db: Session SQLAlchemy.
        :param data: Données pour créer le multivers.
        :return: Multivers créé.
        """
        return self.service.create_multiverse(db, data)


class ListMultiversesUseCase:
    """
    Use case pour lister tous les multivers avec pagination.
    """

    def __init__(self, service: IMultiverseService):
        """
        Initialise le cas d'utilisation avec un service de multivers.

        :param service: Instance conforme à IMultiverseService.
        """
        self.service = service

    def execute(
        self, db: Session, page: int, size: int, order_by: str
    ) -> Tuple[List[Multiverse], int]:
        """
        Exécute la récupération de tous les multivers avec pagination.

        :param db: Session SQLAlchemy.
        :param page: Numéro de la page.
        :param size: Nombre d'éléments par page.
        :param order_by: Champ utilisé pour trier les résultats.
        :return: Liste des multivers et le nombre total de multivers.
        """
        return self.service.list_all_universes(db, page, size, order_by)


class UpdateMultiverseUseCase:
    """
    Use case pour mettre à jour un multivers.
    """

    def __init__(self, service: IMultiverseService):
        """
        Initialise le cas d'utilisation avec un service de multivers.

        :param service: Instance conforme à IMultiverseService.
        """
        self.service = service

    def execute(
        self, db: Session, multiverse_id: int, data: MultiverseUpdate
    ) -> Multiverse:
        """
        Exécute la mise à jour d'un multivers.

        :param db: Session SQLAlchemy.
        :param multiverse_id: ID du multivers à mettre à jour.
        :param data: Données pour mettre à jour le multivers.
        :return: Multivers mis à jour.
        """
        return self.service.update_multiverse(db, multiverse_id, data)


class DeleteMultiverseUseCase:
    """
    Use case pour supprimer un multivers.
    """

    def __init__(self, service: IMultiverseService):
        """
        Initialise le cas d'utilisation avec un service de multivers.

        :param service: Instance conforme à IMultiverseService.
        """
        self.service = service

    def execute(self, db: Session, multiverse_id: int) -> Dict[str, str]:
        """
        Exécute la suppression d'un multivers.

        :param db: Session SQLAlchemy.
        :param multiverse_id: ID du multivers à supprimer.
        :return: Message de confirmation sous forme de dictionnaire.
        """
        return self.service.delete_multiverse(db, multiverse_id)
