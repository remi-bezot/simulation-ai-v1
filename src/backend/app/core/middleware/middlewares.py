from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.gzip import GZipMiddleware
from fastapi import Request
import time
import logging

# Initialisation du logger
logger = logging.getLogger("simulation-ai")


class LogRequestsMiddleware(BaseHTTPMiddleware):
    """
    Middleware pour journaliser les requêtes avec leur durée d'exécution.
    """

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        logger.info(f"Requête reçue : {request.method} {request.url}")
        response = await call_next(request)
        process_time = time.time() - start_time
        logger.info(
            f"Requête terminée : {request.method} {request.url} - "
            f"Statut : {response.status_code} - Temps : {process_time:.2f}s"
        )
        return response


def setup_middlewares(app, origins, environment="development"):
    """
    Ajoute tous les middlewares nécessaires à l'application.

    :param app: L'application FastAPI.
    :param origins: Liste des origines autorisées pour CORS.
    :param environment: Environnement courant ("development", "production").
    """
    # Middleware CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type"],
    )

    # Middleware pour compression des réponses
    app.add_middleware(GZipMiddleware)

    # Middleware pour journaliser les requêtes
    app.add_middleware(LogRequestsMiddleware)

    # Middleware pour les hôtes de confiance (activé uniquement en production)
    if environment == "production":
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=[
                "example.com",  # Remplace par les hôtes approuvés
                "*.example.com",
            ],
        )
        logger.info("TrustedHostMiddleware activé en production.")
