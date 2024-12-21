from typing import Dict, Any
from sqlalchemy.orm import Session
from app.infrastructure.database.postgresql.models.agent import Agent
from app.application.repositories.agent_repository import AgentRepository
from app.schemas.agent import AgentCreate, AgentUpdate
from app.core.agents.actions.agent_action import (
    AgentAction,
    MoveAction,
    AttackAction,
    GatherResourceAction,
    BuildAction,
    DefendAction,
    HealAction,
    CommunicateAction,
    ExploreAction,
    TradeAction,
    RestAction,
)
import logging

logger = logging.getLogger(__name__)


class AgentService:
    """
    Service pour gérer les opérations liées aux agents.
    """

    def __init__(self, repository: AgentRepository):
        """
        Initialise le service avec un repository.

        :param repository: Instance de AgentRepository.
        """
        self.repository = repository

    def list_agents(self) -> list:
        """
        Récupère la liste de tous les agents.

        :return: Liste d'agents.
        """
        agents = self.repository.list_all()
        logger.info(f"{len(agents)} agents récupérés.")
        return agents

    def get_agent_by_id(self, db: Session, agent_id: int) -> Agent:
        """
        Récupère un agent par son ID.

        :param db: Session SQLAlchemy utilisée pour la requête.
        :param agent_id: ID de l'agent à récupérer.
        :return: Instance de l'agent récupéré.
        :raises ValueError: Si l'agent n'existe pas.
        """
        agent = self.repository.get(agent_id)
        if not agent:
            raise ValueError("Agent not found")
        return agent

    def create_agent(self, db: Session, agent_data: dict) -> Agent:
        """
        Crée un nouvel agent.

        :param db: Session SQLAlchemy utilisée pour la requête.
        :param agent_data: Dictionnaire contenant les données de l'agent à créer.
        :return: Instance de l'agent créé.
        :raises ValueError: Si les données de l'agent sont invalides.
        """
        agent = Agent(**agent_data)
        self.repository.create(agent)
        return agent

    def update_agent(self, db: Session, agent_id: int, data: dict) -> Agent:
        """
        Met à jour un agent existant.

        :param db: Session SQLAlchemy utilisée pour la requête.
        :param agent_id: ID de l'agent à mettre à jour.
        :param data: Dictionnaire contenant les mises à jour.
        :return: Instance de l'agent mis à jour.
        :raises ValueError: Si l'agent n'existe pas.
        """
        agent = self.repository.get(agent_id)
        if not agent:
            raise ValueError("Agent not found")
        if data.get("name"):
            agent.name = data["name"].strip()
        if data.get("properties"):
            agent.properties.update(data["properties"])
        updated_agent = self.repository.update(agent)
        logger.info(f"Agent mis à jour : {updated_agent.name} (ID={updated_agent.id}).")
        return updated_agent

    def delete_agent(self, db: Session, agent_id: int) -> None:
        """
        Supprime un agent existant.

        :param db: Session SQLAlchemy utilisée pour la requête.
        :param agent_id: ID de l'agent à supprimer.
        :raises ValueError: Si l'agent n'existe pas.
        """
        agent = self.repository.get(agent_id)
        if not agent:
            raise ValueError("Agent not found")
        self.repository.delete(agent)
        logger.info(f"Agent supprimé avec succès : ID={agent_id}.")

    def perform_action(self, db: Session, agent_id: int, action: AgentAction) -> None:
        """
        Exécute une action sur un agent.

        :param db: Session SQLAlchemy utilisée pour la requête.
        :param agent_id: ID de l'agent sur lequel exécuter l'action.
        :param action: Instance de AgentAction à exécuter.
        :raises ValueError: Si l'agent n'existe pas.
        """
        agent = self.repository.get(agent_id)
        if not agent:
            raise ValueError("Agent not found")
        action.execute(agent)
        logger.info(
            f"Action {action.__class__.__name__} exécutée sur l'agent ID={agent_id}."
        )
