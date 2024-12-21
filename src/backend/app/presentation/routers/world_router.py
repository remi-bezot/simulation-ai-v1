from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.world_schemas import WorldCreate, WorldUpdate, WorldResponse
from app.application.services.world_service import WorldService
from app.infrastructure.database.postgresql.database import get_db
from typing import List

router = APIRouter(prefix="/worlds", tags=["Worlds"])


def get_world_service(db: Session = Depends(get_db)) -> WorldService:
    """
    Fournit une instance de WorldService avec une session injectée.

    :param db: Session SQLAlchemy injectée.
    :return: Instance de WorldService.
    """
    return WorldService(db)


@router.get("/", response_model=List[WorldResponse])
def list_worlds(service: WorldService = Depends(get_world_service)):
    """
    Récupère tous les mondes existants.
    """
    try:
        return service.list_worlds()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur lors de la récupération des mondes : {e}"
        )


@router.post("/", response_model=WorldResponse)
def create_world(
    world: WorldCreate, service: WorldService = Depends(get_world_service)
):
    """
    Crée un nouveau monde.
    """
    try:
        return service.create_world(world)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{world_id}", response_model=dict)
def update_world(world_id: int, updates: WorldUpdate, db: Session = Depends(get_db)):
    """
    Met à jour un monde existant.
    """
    service = WorldService(db)
    try:
        updated_world = service.update_world(world_id, updates)
        return {"message": "Monde mis à jour avec succès.", "world": updated_world}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{world_id}", response_model=dict)
def delete_world(world_id: int, db: Session = Depends(get_db)):
    """
    Supprime un monde par son ID.
    """
    service = WorldService(db)
    try:
        service.delete_world(world_id)
        return {"message": f"Le monde avec l'ID {world_id} a été supprimé avec succès."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
