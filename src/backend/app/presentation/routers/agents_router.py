from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database.postgresql.database import get_db
from app.application.services.agent_service import AgentService
from app.schemas.agent import AgentCreate, AgentUpdate, AgentResponse
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Agents"])


def get_agent_service(db: Session = Depends(get_db)) -> AgentService:
    """
    Fournit une instance de `AgentService` avec une session injectée.

    :param db: Session SQLAlchemy injectée.
    :return: Instance de `AgentService`.
    """
    return AgentService(db)


@router.get("/", response_model=List[AgentResponse])
def list_agents(service: AgentService = Depends(get_agent_service)):
    """
    Retourne la liste de tous les agents.
    """
    try:
        agents = service.list_agents()
        logger.info(f"{len(agents)} agents récupérés.")
        return agents
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des agents : {e}")
        raise HTTPException(
            status_code=500,
            detail="Erreur lors de la récupération des agents.",
        )


@router.get("/{agent_id}", response_model=AgentResponse)
def get_agent(agent_id: int, service: AgentService = Depends(get_agent_service)):
    """
    Retourne un agent par son ID.
    """
    try:
        agent = service.get_agent_by_id(agent_id)
        logger.info(f"Agent récupéré : ID={agent_id}")
        return agent
    except ValueError as e:
        logger.warning(f"Agent non trouvé : ID={agent_id}")
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=AgentResponse)
def create_agent(
    agent: AgentCreate, service: AgentService = Depends(get_agent_service)
):
    """
    Crée un nouvel agent.
    """
    try:
        created_agent = service.create_agent(agent)
        logger.info(f"Agent créé avec succès : {created_agent.name}")
        return created_agent
    except ValueError as e:
        logger.error(f"Erreur lors de la création d'un agent : {e}")
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{agent_id}", response_model=AgentResponse)
def update_agent(
    agent_id: int,
    agent: AgentUpdate,
    service: AgentService = Depends(get_agent_service),
):
    """
    Met à jour un agent existant.
    """
    try:
        updated_agent = service.update_agent(agent_id, agent)
        logger.info(f"Agent mis à jour : ID={agent_id}")
        return updated_agent
    except ValueError as e:
        logger.warning(f"Erreur lors de la mise à jour de l'agent : ID={agent_id}")
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{agent_id}", response_model=Dict[str, str])
def delete_agent(agent_id: int, service: AgentService = Depends(get_agent_service)):
    """
    Supprime un agent par son ID.
    """
    try:
        service.delete_agent(agent_id)
        logger.info(f"Agent supprimé : ID={agent_id}")
        return {"message": f"L'agent avec l'ID {agent_id} a été supprimé."}
    except ValueError as e:
        logger.warning(f"Erreur lors de la suppression de l'agent : ID={agent_id}")
        raise HTTPException(status_code=404, detail=str(e))
