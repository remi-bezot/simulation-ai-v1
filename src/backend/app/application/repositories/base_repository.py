from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, List, Optional
from app.core.exceptions.handlers import handle_repository_exception
import logging

logger = logging.getLogger(__name__)

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """
    Repository générique pour gérer les opérations CRUD.
    """

    def __init__(self, db: Session, model: Type[T]):
        """
        Initialise le repository avec une session et un modèle.

        :param db: Session SQLAlchemy.
        :param model: Modèle SQLAlchemy associé.
        """
        self.db = db
        self.model = model

    def get(self, id: int) -> Optional[T]:
        """
        Récupère un enregistrement par son ID.

        :param id: ID de l'enregistrement.
        :return: Enregistrement correspondant ou None.
        """
        try:
            return self.db.query(self.model).filter(self.model.id == id).first()
        except Exception as e:
            handle_repository_exception(
                self.db, e, "Erreur lors de la récupération de l'enregistrement"
            )

    def list(self) -> List[T]:
        """
        Récupère tous les enregistrements.

        :return: Liste de tous les enregistrements.
        """
        try:
            return self.db.query(self.model).all()
        except Exception as e:
            handle_repository_exception(
                self.db,
                e,
                "Erreur lors de la récupération de la liste des enregistrements",
            )

    def create(self, obj_in: T) -> T:
        """
        Crée un nouvel enregistrement.

        :param obj_in: Objet à créer.
        :return: Objet créé.
        """
        try:
            self.db.add(obj_in)
            self.db.commit()
            self.db.refresh(obj_in)
            return obj_in
        except Exception as e:
            handle_repository_exception(
                self.db, e, "Erreur lors de la création de l'enregistrement"
            )

    def update(self, obj_in: T) -> T:
        """
        Met à jour un enregistrement existant.

        :param obj_in: Objet à mettre à jour.
        :return: Objet mis à jour.
        """
        try:
            self.db.commit()
            self.db.refresh(obj_in)
            return obj_in
        except Exception as e:
            handle_repository_exception(
                self.db, e, "Erreur lors de la mise à jour de l'enregistrement"
            )

    def delete(self, id: int) -> None:
        """
        Supprime un enregistrement par son ID.

        :param id: ID de l'enregistrement à supprimer.
        """
        try:
            obj = self.get(id)
            if obj:
                self.db.delete(obj)
                self.db.commit()
                logger.info(f"{self.model.__name__} supprimé avec succès : ID={id}.")
        except Exception as e:
            handle_repository_exception(
                self.db, e, "Erreur lors de la suppression de l'enregistrement"
            )
