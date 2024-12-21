from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL_POSTGRESQL
import logging

# Configuration du logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Vérification de la configuration de l'URL de la base de données
if not DATABASE_URL_POSTGRESQL:
    logger.critical("DATABASE_URL_POSTGRESQL n'est pas défini dans la configuration.")
    raise RuntimeError("La connexion à la base de données nécessite une URL valide.")

try:
    # Configuration de l'engine PostgreSQL avec options avancées
    engine = create_engine(
        DATABASE_URL_POSTGRESQL,
        echo=False,  # Désactiver les logs SQL en production pour éviter une surcharge
        pool_size=10,  # Nombre maximum de connexions dans le pool
        max_overflow=20,  # Connexions supplémentaires au-delà du pool_size
        pool_timeout=30,  # Temps d'attente avant expiration d'une connexion
        pool_recycle=1800,  # Recyclage des connexions pour éviter les connexions inactives
        pool_pre_ping=True,  # Vérifie la validité des connexions avant utilisation
        future=True,  # Compatibilité avec SQLAlchemy 2.x
    )
    logger.info("Connexion à la base de données PostgreSQL réussie.")
except Exception as e:
    logger.critical(f"Erreur lors de la configuration de l'engine SQLAlchemy : {e}")
    raise

# Création d'une session locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Obtenir une session PostgreSQL.

    Cette fonction est utilisée pour fournir une session de base de données
    gérée automatiquement dans les dépendances FastAPI ou autres cas d'usage.

    Yields:
        Session: Une instance de session SQLAlchemy.
    """
    db = SessionLocal()
    try:
        logger.debug("Session de base de données ouverte.")
        yield db
    except Exception as e:
        logger.error(f"Erreur lors de l'utilisation de la session : {e}")
        raise
    finally:
        db.close()
        logger.debug("Session de base de données fermée.")
