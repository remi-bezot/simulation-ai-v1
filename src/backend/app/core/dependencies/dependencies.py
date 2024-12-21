from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.database.postgresql.database import get_db
from app.core.config.settings import settings
from app.application.services.event_service import EventService
from app.application.services.multiverse_service import MultiverseService
from app.application.services.universe_service import UniverseService
from app.application.services.world_service import WorldService


def get_settings():
    """
    Retourne les paramètres de configuration globale.
    """
    return settings


def get_db_session(db: Session = Depends(get_db)) -> Session:
    """
    Retourne une session SQLAlchemy injectée.
    """
    return db


def get_event_service(db: Session = Depends(get_db_session)) -> EventService:
    """
    Retourne une instance de EventService avec la base de données injectée.
    """
    return EventService(db)


def get_multiverse_service(db: Session = Depends(get_db_session)) -> MultiverseService:
    """
    Retourne une instance de MultiverseService avec la base de données injectée.
    """
    return MultiverseService(db)


def get_universe_service(db: Session = Depends(get_db_session)) -> UniverseService:
    """
    Retourne une instance de UniverseService avec la base de données injectée.
    """
    return UniverseService(db)


def get_world_service(db: Session = Depends(get_db_session)) -> WorldService:
    """
    Retourne une instance de WorldService avec la base de données injectée.
    """
    return WorldService(db)
