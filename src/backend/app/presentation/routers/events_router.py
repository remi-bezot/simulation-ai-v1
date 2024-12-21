from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from src.backend.app.application.use_cases.events.event_management_use_case import (
    EventUseCase,
)
from app.application.services.event_service import EventManager
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Events"])  # Pas de préfixe si centralisé dans __init__.py


def get_event_use_case():
    """
    Fournit une instance d'EventUseCase avec EventManager comme dépendance.
    """
    return EventUseCase(EventManager())


class TriggerEventRequest(BaseModel):
    event_name: str


@router.get("/", response_model=dict)
def get_events(event_use_case: EventUseCase = Depends(get_event_use_case)):
    """
    Retourne la liste des événements.

    :param event_use_case: Dépendance pour accéder aux cas d'utilisation des événements.
    :return: Log des événements sous forme de liste.
    """
    try:
        events = event_use_case.execute_get_event_log()
        logger.info(f"{len(events)} événements récupérés.")
        return {"events": events}
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des événements : {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la récupération des événements : {str(e)}",
        )


@router.post("/trigger", response_model=dict)
def trigger_event(
    request: TriggerEventRequest,
    event_use_case: EventUseCase = Depends(get_event_use_case),
):
    """
    Déclenche un événement.

    :param request: Requête contenant le nom de l'événement à déclencher.
    :param event_use_case: Dépendance pour accéder aux cas d'utilisation des événements.
    :return: Résultat de l'exécution du déclenchement de l'événement.
    """
    try:
        result = event_use_case.execute_trigger_event(request.event_name.strip())
        logger.info(f"Événement déclenché : {request.event_name.strip()}")
        return result
    except Exception as e:
        logger.error(
            f"Erreur lors du déclenchement de l'événement '{request.event_name.strip()}': {e}"
        )
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors du déclenchement de l'événement : {str(e)}",
        )
