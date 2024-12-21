from fastapi import FastAPI
from app.core.config.settings import get_cors_origins
from app.core.logging.logging_config import setup_logger
from app.core.middleware.middlewares import setup_middlewares
from app.presentation.routers import include_routers
from app.core.exceptions.handlers import (
    http_exception_handler,
    global_exception_handler,
)
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

# Initialisation de l'application
app = FastAPI(
    title="Simulation AI v3",
    description="Une API modulaire pour la gestion des agents, multivers et événements.",
    version="3.0.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Configuration
logger = setup_logger()
origins = get_cors_origins()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware
setup_middlewares(app)

# Inclusion des routes
include_routers(app)

# Gestion des erreurs
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)


# Routes principales
@app.get("/")
def root():
    """Route racine pour tester l'accès au serveur."""
    logger.info("Accès à la route racine.")
    return {"message": "Bienvenue dans Simulation AI v3!"}


@app.get("/health")
def health_check():
    """Route de vérification de l'état du serveur."""
    logger.info("Vérification de l'état du serveur.")
    return {
        "status": "ok",
        "version": "3.0.1",
        "message": "Le serveur est opérationnel.",
    }


# Lancer l'application uniquement si elle est exécutée directement
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
