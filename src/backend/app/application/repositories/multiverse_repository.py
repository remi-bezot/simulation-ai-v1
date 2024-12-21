from sqlalchemy.orm import Session
from app.infrastructure.database.postgresql.models.multiverse import Multiverse
from app.core.exceptions.handlers import handle_repository_exception
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


class MultiverseRepository:
    """Repository pour gérer les opérations sur les multivers."""

    def __init__(self, db: Session):
        self.db = db

    def handle_exception(self, e: Exception, message: str):
        """
        Gère les exceptions en effectuant un rollback et en enregistrant l'erreur.

        :param e: Exception levée.
        :param message: Message d'erreur à enregistrer.
        """
        self.db.rollback()
        logger.error(f"{message} : {e}")
        raise RuntimeError(f"{message} : {e}")

    def get_by_id(self, multiverse_id: int) -> Optional<Multiverse]:
        """
        Récupère un multivers par son ID.

        :param multiverse_id: ID du multivers à récupérer.
        :return: Instance de Multiverse ou None si non trouvé.
        """
        multiverse = (
            self.db.query(Multiverse).filter(Multiverse.id == multiverse_id).first()
        )
        if not multiverse:
            logger.warning(f"Multivers introuvable : ID={multiverse_id}")
        return multiverse

    def list_all(self, offset: int, limit: int, order_by: str) -> List<Multiverse]:
        """
        Récupère une liste de multivers avec pagination et tri.

        :param offset: Début de la pagination.
        :param limit: Nombre maximum de résultats.
        :param order_by: Champ utilisé pour trier les résultats.
        :return: Liste des multivers.
        :raises ValueError: Si les paramètres sont invalides.
        """
        if offset < 0 or limit < 1:
            logger.error(
                f"Paramètres de pagination invalides : offset={offset}, limit={limit}"
            )
            raise ValueError("Les paramètres de pagination doivent être positifs.")
        if not hasattr(Multiverse, order_by):
            logger.error(f"Champ de tri invalide : {order_by}")
            raise ValueError(f"Champ de tri invalide : {order_by}")
        multiverses = (
            self.db.query(Multiverse)
            .order_by(getattr(Multiverse, order_by))
            .offset(offset)
            .limit(limit)
            .all()
        )
        logger.info(
            f"{len(multiverses)} multivers récupérés (offset={offset}, limit={limit})."
        )
        return multiverses

    def count_all(self) -> int:
        """
        Compte le nombre total de multivers.

        :return: Nombre total de multivers dans la base.
        """
        total = self.db.query(Multiverse).count()
        logger.info(f"Nombre total de multivers : {total}.")
        return total

    def create(self, multiverse: Multiverse) -> Multiverse:
        """
        Crée un nouveau multivers.

        :param multiverse: Instance de Multiverse à ajouter.
        :return: Instance créée et persistée.
        """
        try:
            self.db.add(multiverse)
            self.db.commit()
            self.db.refresh(multiverse)
            logger.info(
                f"Multivers créé avec succès : {multiverse.name} (ID={multiverse.id})."
            )
            return multiverse
        except Exception as e:
            self.handle_exception(e, "Erreur lors de la création du multivers")

    def update(self, multiverse: Multiverse) -> Multiverse:
        """
        Met à jour un multivers existant.

        :param multiverse: Instance de Multiverse avec des modifications.
        :return: Instance mise à jour et persistée.
        """
        try:
            self.db.commit()
            self.db.refresh(multiverse)
            logger.info(
                f"Multivers mis à jour avec succès : {multiverse.name} (ID={multiverse.id})."
            )
            return multiverse
        except Exception as e:
            self.handle_exception(e, "Erreur lors de la mise à jour du multivers")

    def delete(self, multiverse: Multiverse):
        """
        Supprime un multivers existant.

        :param multiverse: Instance de Multiverse à supprimer.
        """
        try:
            self.db.delete(multiverse)
            self.db.commit()
            logger.info(f"Multivers supprimé avec succès : ID={multiverse.id}.")
        except Exception as e:
            handle_repository_exception(self.db, e, "Erreur lors de la suppression du multivers")
