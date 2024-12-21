from sqlalchemy.orm import Session
from app.infrastructure.database.postgresql.models.universe import Universe
from app.core.exceptions.handlers import handle_repository_exception
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


class UniverseRepository:
    """
    Repository pour gérer les opérations sur les univers.
    """

    def __init__(self, db: Session):
        """
        Initialise le repository avec une session SQLAlchemy.
        """
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

    def get_by_id(self, universe_id: int) -> Optional[Universe]:
        """
        Récupère un univers par son ID.

        :param universe_id: ID de l'univers à récupérer.
        :return: Instance de Universe ou None si non trouvé.
        """
        universe = self.db.query(Universe).filter(Universe.id == universe_id).first()
        if not universe:
            logger.warning(f"Univers introuvable : ID={universe_id}")
        return universe

    def list_all(self, offset: int, limit: int) -> List[Universe]:
        """
        Récupère une liste d'univers avec pagination.

        :param offset: Début de la pagination.
        :param limit: Nombre maximum de résultats.
        :return: Liste des univers.
        """
        if offset < 0 or limit < 1:
            logger.error(
                f"Paramètres de pagination invalides : offset={offset}, limit={limit}"
            )
            raise ValueError("Les paramètres de pagination doivent être positifs.")
        universes = self.db.query(Universe).offset(offset).limit(limit).all()
        logger.info(
            f"{len(universes)} univers récupérés (offset={offset}, limit={limit})."
        )
        return universes

    def count_all(self) -> int:
        """
        Compte le nombre total d'univers.

        :return: Nombre total d'univers dans la base.
        """
        total = self.db.query(Universe).count()
        logger.info(f"Nombre total d'univers : {total}.")
        return total

    def create(self, universe: Universe) -> Universe:
        """
        Crée un nouvel univers.

        :param universe: Instance de Universe à ajouter.
        :return: Instance créée et persistée.
        """
        try:
            self.db.add(universe)
            self.db.commit()
            self.db.refresh(universe)
            logger.info(
                f"Univers créé avec succès : {universe.name} (ID={universe.id})."
            )
            return universe
        except Exception as e:
            self.handle_exception(e, "Erreur lors de la création de l'univers")

    def update(self, universe: Universe) -> Universe:
        """
        Met à jour un univers existant.

        :param universe: Instance de Universe avec des modifications.
        :return: Instance mise à jour et persistée.
        """
        try:
            self.db.commit()
            self.db.refresh(universe)
            logger.info(
                f"Univers mis à jour avec succès : {universe.name} (ID={universe.id})."
            )
            return universe
        except Exception as e:
            self.handle_exception(e, "Erreur lors de la mise à jour de l'univers")

    def delete(self, universe: Universe):
        """
        Supprime un univers existant.

        :param universe: Instance de Universe à supprimer.
        """
        try:
            self.db.delete(universe)
            self.db.commit()
            logger.info(f"Univers supprimé avec succès : ID={universe.id}.")
        except Exception as e:
            handle_repository_exception(self.db, e, "Erreur lors de la suppression de l'univers")
