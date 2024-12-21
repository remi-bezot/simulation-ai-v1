from pydantic import BaseSettings, Field, validator
from typing import List
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis un fichier .env
load_dotenv()


class Settings(BaseSettings):
    """
    Configuration générale de l'application.
    """

    # Configuration générale
    APP_NAME: str = Field("Simulation AI", description="Nom de l'application.")
    APP_VERSION: str = Field("3.0.1", description="Version de l'application.")
    DEBUG: bool = Field(False, description="Mode debug activé/désactivé.")
    ENVIRONMENT: str = Field(
        "development", description="Environnement de l'application."
    )

    # Configuration base de données
    DATABASE_URL: str = Field(..., description="URL de connexion à la base de données.")
    DATABASE_POOL_SIZE: int = Field(
        5, description="Nombre maximum de connexions dans le pool de base de données."
    )

    # Configuration API et CORS
    CORS_ALLOWED_ORIGINS: List[str] = Field(
        ["http://localhost:3000", "http://localhost:3001"],
        description="Liste des origines CORS autorisées.",
    )

    # Configuration du logger
    LOG_LEVEL: str = Field("INFO", description="Niveau de log de l'application.")

    @validator("LOG_LEVEL")
    def validate_log_level(cls, v):
        levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if v.upper() not in levels:
            raise ValueError(f"Invalid log level: {v}")
        return v.upper()

    @validator("CORS_ALLOWED_ORIGINS", pre=True)
    def split_origins(cls, value: str) -> List[str]:
        """
        Transforme une chaîne d'origines séparées par des virgules en liste.
        """
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value

    class Config:
        env_file = ".env"


# Instance de configuration globale
settings = Settings()
