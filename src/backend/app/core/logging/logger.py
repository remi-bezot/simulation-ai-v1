import logging
from logging.config import dictConfig
from app.core.config.settings import settings  # Import des configurations globales


def setup_logger():
    """
    Configure et retourne le logger principal.
    """
    log_level = settings.LOG_LEVEL.upper() if hasattr(settings, "LOG_LEVEL") else "INFO"

    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": log_level,
            },
        },
        "root": {
            "level": log_level,
            "handlers": ["console"],
        },
    }

    dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger("simulation-ai")
    return logger
