import logging
from logging.config import dictConfig
from app.core.config.settings import settings  # Import des configurations globales


def setup_logger():
    """
    Configure et retourne le logger principal.
    """
    log_level = settings.LOG_LEVEL

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
            "handlers": ["console"],
            "level": log_level,
        },
    }

    dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger("simulation_ai_v3")
    return logger
