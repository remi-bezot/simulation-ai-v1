from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database.postgresql.database import get_db
from app.schemas.universe import UniverseCreate, Universe
from app.application.services.universe_service import UniverseService
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Universes"])


def get_universe_service(db: Session = Depends(get_db)) -> UniverseService:
    """
    Fournit une instance de `UniverseService` pour les routes.

    :param db: Session SQLAlchemy injectée.
    :return: Instance de `UniverseService`.
    """
    return UniverseService(db)


@router.get("/{multiverse_id}", response_model=Dict[str, Any])
def get_universes(multiverse_id: int, db: Session = Depends(get_db)):
    """
    Récupère la liste des univers pour un multivers donné.

    :param multiverse_id: ID du multivers.
    :param db: Session SQLAlchemy injectée.
    :return: Liste des univers.
    """
    service = get_universe_service(db)
    try:
        universes = service.get_universes(multiverse_id)
        return {"universes": universes}
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des univers : {e}")
        raise HTTPException(
            status_code=500, detail="Erreur lors de la récupération des univers."
        )


@router.post("/", response_model=Dict[str, Any])
def create_universe(universe: UniverseCreate, db: Session = Depends(get_db)):
    """
    Crée un nouvel univers.

    :param universe: Schéma de création d'univers.
    :param db: Session SQLAlchemy injectée.
    :return: Détails de l'univers créé.
    """
    service = get_universe_service(db)
    try:
        new_universe = service.create_universe(universe)
        return {"message": "Univers créé avec succès.", "universe": new_universe}
    except Exception as e:
        logger.error(f"Erreur lors de la création de l'univers : {e}")
        raise HTTPException(
            status_code=500, detail="Erreur lors de la création de l'univers."
        )


@router.delete("/{universe_id}", response_model=Dict[str, Any])
def remove_universe(
    universe_id: int, service: UniverseService = Depends(get_universe_service)
):
    """
    Supprimer un univers par son ID.
    """
    try:
        service.delete_universe(universe_id=universe_id)
        logger.info(f"Univers supprimé avec succès : ID={universe_id}.")
        return {
            "message": f"L'univers avec l'ID {universe_id} a été supprimé avec succès."
        }
    except ValueError as e:
        logger.warning(f"Erreur lors de la suppression de l'univers : {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Erreur système : {e}")
        raise HTTPException(status_code=500, detail="Erreur interne du serveur.")
