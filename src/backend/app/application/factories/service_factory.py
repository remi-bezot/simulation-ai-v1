from sqlalchemy.orm import Session
from app.application.repositories.event_repository import EventRepository
from app.application.managers.event_manager import EventManager
from app.application.repositories.universe_repository import UniverseRepository
from app.application.managers.universe_manager import UniverseManager

class ServiceFactory:
    """Factory pour créer des services avec leurs dépendances."""

    @staticmethod
    def get_event_manager(db: Session) -> EventManager:
        """
        Crée une instance de EventManager avec ses dépendances.

        :param db: Session SQLAlchemy.
        :return: Instance de EventManager.
        """
        repository = EventRepository(db)
        return EventManager(repository)

    @staticmethod
    def get_universe_manager(db: Session) -> UniverseManager:
        """
        Crée une instance de UniverseManager avec ses dépendances.

        :param db: Session SQLAlchemy.
        :return: Instance de UniverseManager.
        """
        repository = UniverseRepository(db)
        return UniverseManager(repository)
