from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from typing import Tuple, List, Dict, Any
from app.schemas.multiverse import MultiverseCreate, MultiverseUpdate
from app.infrastructure.database.postgresql.models.multiverse import Multiverse


class IMultiverseService(ABC):
    """
    Interface pour le service Multiverse.
    Définit les méthodes nécessaires pour gérer les multivers.
    """

    @abstractmethod
    def create_multiverse(self, db: Session, data: MultiverseCreate) -> Multiverse:
        """
        Crée un nouveau multivers.

        :param db: Session SQLAlchemy.
        :param data: Données pour créer le multivers, comprenant :
            - name : Nom du multivers (str).
            - description : Description du multivers (str, optionnel).
            - properties : Propriétés additionnelles (dict, optionnel).
        :return: Instance du multivers créé.
        :raises ValueError: Si les données sont invalides.
        """
        pass

    @abstractmethod
    def list_multiverses(
        self, db: Session, page: int, size: int, order_by: str
    ) -> Tuple[List[Multiverse], int]:
        """
        Récupère une liste paginée de multivers.

        :param db: Session SQLAlchemy.
        :param page: Numéro de la page (commençant à 1).
        :param size: Nombre d'éléments par page.
        :param order_by: Champ utilisé pour trier les résultats.
        :return: Tuple contenant :
            - Une liste de multivers correspondant à la requête.
            - Le nombre total de multivers dans la base de données.
        :raises ValueError: Si les paramètres de pagination ou de tri sont invalides.
        """
        pass

    @abstractmethod
    def update_multiverse(
        self, db: Session, multiverse_id: int, updates: Dict[str, Any]
    ) -> Any:
        """
        Met à jour un multivers existant.

        :param db: Session SQLAlchemy.
        :param multiverse_id: ID du multivers à mettre à jour.
        :param updates: Dictionnaire contenant les mises à jour, par exemple :
            - name : Nouveau nom (optionnel).
            - description : Nouvelle description (optionnel).
            - properties : Propriétés additionnelles mises à jour (optionnel).
        :return: Instance du multivers mis à jour.
        :raises MultiverseNotFoundError: Si le multivers n'existe pas.
        """
        pass

    @abstractmethod
    def delete_multiverse(self, db: Session, multiverse_id: int) -> Dict[str, str]:
        """
        Supprime un multivers.

        :param db: Session SQLAlchemy.
        :param multiverse_id: ID du multivers à supprimer.
        :return: Message de confirmation sous forme de dictionnaire.
        :raises MultiverseNotFoundError: Si le multivers n'existe pas.
        """
        pass
