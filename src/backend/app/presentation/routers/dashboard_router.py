from fastapi import APIRouter, Depends
from typing import List, Dict, Any
from pydantic import BaseModel
from app.application.services.dashboard_service import DashboardService
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Dashboard"])


class DashboardData(BaseModel):
    id: int
    name: str
    value: int


def get_dashboard_service() -> DashboardService:
    """
    Fournit une instance de `DashboardService` pour les routes.

    :return: Instance de `DashboardService`.
    """
    return DashboardService()


@router.get("/", response_model=List[Dict[str, Any]])
def get_dashboard_data(service: DashboardService = Depends(get_dashboard_service)):
    """
    Retourne les données statiques du tableau de bord.

    :param service: Instance de `DashboardService`.
    :return: Liste de DashboardData représentant les données du tableau de bord.
    """
    dashboard_data = service.get_dashboard_data()
    logger.info(f"Données du tableau de bord renvoyées : {dashboard_data}")
    return dashboard_data
