from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database.postgresql.database import get_db
from app.schemas.multiverse import MultiverseCreate, MultiverseUpdate, Multiverse
from app.application.services.multiverse_service import MultiverseService
from app.application.repositories.multiverse_repository import MultiverseRepository
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Multiverses"])  # Pas de préfixe ici si centralisé


def get_multiverse_service(db: Session = Depends(get_db)) -> MultiverseService:
    """
    Fournit une instance de `MultiverseService` pour les routes.

    :param db: Session SQLAlchemy injectée.
    :return: Instance de `MultiverseService`.
    """
    repository = MultiverseRepository(db)
    return MultiverseService(repository)


def handle_exception(e: Exception, message: str, status_code: int = 400):
    logger.error(f"{message} : {e}")
    raise HTTPException(
        status_code=status_code,
        detail=f"{message} : {str(e)}",
    )


@router.get("/", response_model=Dict[str, Any])
def get_multiverses(
    page: int = 1,
    size: int = 10,
    service: MultiverseService = Depends(get_multiverse_service),
):
    """
    Récupère une liste paginée des multivers.
    """
    try:
        multiverses, total = service.list_multiverses(page=page, size=size)
        logger.info(f"{len(multiverses)} multivers récupérés pour la page {page}.")
        return {
            "data": [Multiverse.from_orm(m).dict() for m in multiverses],
            "total": total,
            "page": page,
            "size": size,
        }
    except Exception as e:
        handle_exception(e, "Erreur lors de la récupération des multivers", 500)


@router.post("/", response_model=Dict[str, Any])
def add_multiverse(
    multiverse: MultiverseCreate,
    service: MultiverseService = Depends(get_multiverse_service),
):
    """
    Ajoute un nouveau multivers.
    """
    try:
        new_multiverse = service.create_multiverse(data=multiverse)
        logger.info(f"Multivers créé avec succès : {new_multiverse.name}.")
        return {
            "message": "Multivers créé avec succès.",
            "multiverse": Multiverse.from_orm(new_multiverse).dict(),
        }
    except Exception as e:
        handle_exception(e, "Erreur lors de la création du multivers")


@router.put("/{multiverse_id}", response_model=Dict[str, Any])
def update_multiverse(
    multiverse_id: int,
    updates: MultiverseUpdate,
    service: MultiverseService = Depends(get_multiverse_service),
):
    """
    Modifie un multivers existant.

    :param multiverse_id: ID du multivers à modifier.
    :param updates: Données de mise à jour du multivers.
    :param service: Instance de `MultiverseService`.
    :return: Détails du multivers mis à jour.
    """
    try:
        updated_multiverse = service.update_multiverse(
            multiverse_id=multiverse_id, updates=updates
        )
        logger.info(
            f"Multivers mis à jour : {updated_multiverse.name} (ID={multiverse_id})."
        )
        return {
            "message": "Multivers mis à jour avec succès.",
            "multiverse": Multiverse.from_orm(updated_multiverse).dict(),
        }
    except Exception as e:
        handle_exception(e, "Erreur lors de la mise à jour du multivers")


@router.delete("/{multiverse_id}", response_model=Dict[str, Any])
def remove_multiverse(
    multiverse_id: int, service: MultiverseService = Depends(get_multiverse_service)
):
    """
    Supprime un multivers existant.

    :param multiverse_id: ID du multivers à supprimer.
    :param service: Instance de `MultiverseService`.
    :return: Message confirmant la suppression.
    """
    try:
        service.delete_multiverse(multiverse_id=multiverse_id)
        logger.info(f"Multivers supprimé : ID={multiverse_id}.")
        return {"message": "Multivers supprimé avec succès."}
    except MultiverseNotFoundError as e:
        handle_exception(e, "Erreur lors de la suppression du multivers", 404)
    except Exception as e:
        handle_exception(e, "Erreur lors de la suppression du multivers")
