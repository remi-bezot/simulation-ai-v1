from sqlalchemy.exc import SQLAlchemyError
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def handle_sqlalchemy_errors(func):
    """
    Décorateur pour gérer les erreurs SQLAlchemy.

    :param func: Fonction à décorer.
    :return: Fonction décorée.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            logger.error("Erreur SQLAlchemy : %s", e)
            raise RuntimeError(f"Erreur d'exécution : {e}")

    return wrapper
