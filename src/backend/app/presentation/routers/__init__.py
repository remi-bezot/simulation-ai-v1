from fastapi import APIRouter, FastAPI
from .agents_router import router as agents_router
from .events_router import router as events_router
from .multiverse_router import router as multiverse_router
from .dashboard_router import router as dashboard_router
from .universe_router import router as universe_router
from .world_router import router as world_router
import logging

logger = logging.getLogger(__name__)

# Liste des routes à inclure dans l'application principale
ROUTERS = [
    {"router": agents_router, "prefix": "/agents", "tag": "Agents"},
    {"router": events_router, "prefix": "/events", "tag": "Events"},
    {"router": multiverse_router, "prefix": "/multiverses", "tag": "Multiverses"},
    {"router": dashboard_router, "prefix": "/dashboard", "tag": "Dashboard"},
    {"router": universe_router, "prefix": "/universes", "tag": "Universes"},
    {"router": world_router, "prefix": "/worlds", "tag": "Worlds"},
]


def include_routers(app: FastAPI) -> None:
    """
    Inclut toutes les routes définies dans l'application principale.

    :param app: Instance de l'application FastAPI.
    """
    for route in ROUTERS:
        try:
            app.include_router(
                route["router"], prefix=route["prefix"], tags=[route["tag"]]
            )
            logger.info(f"Routeur inclus : {route['tag']} ({route['prefix']})")
        except KeyError as e:
            logger.error(f"Clé manquante dans la définition du routeur : {e}")
            raise ValueError("Erreur dans la configuration des routes.")
        except Exception as e:
            logger.error(
                f"Erreur lors de l'inclusion du routeur {route.get('tag', 'inconnu')} : {e}"
            )
            raise RuntimeError("Une erreur inattendue s'est produite.")
