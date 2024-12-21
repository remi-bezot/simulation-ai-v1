from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
from fastapi import Request
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
import logging
import uuid
from sqlalchemy.orm import Session

logger = logging.getLogger("simulation-ai")


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """
    Gestion des erreurs HTTP spécifiées.

    :param request: La requête FastAPI à l'origine de l'erreur.
    :param exc: L'exception HTTP levée.
    :return: JSONResponse avec le code d'erreur et un message clair.
    """
    request_id = str(uuid.uuid4())
    logger.error(
        f"[{request_id}] Erreur HTTP {exc.status_code}: {exc.detail} | URL: {request.url}"
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "code": "HTTP_ERROR",
            "message": exc.detail or "Erreur HTTP non spécifiée.",
            "url": str(request.url),
            "request_id": request_id,
        },
    )


async def validation_exception_handler(request: Request, exc: ValidationError):
    """
    Gestion des erreurs de validation Pydantic.

    :param request: La requête FastAPI à l'origine de l'erreur.
    :param exc: L'exception de validation levée.
    :return: JSONResponse avec les détails des erreurs de validation.
    """
    request_id = str(uuid.uuid4())
    logger.warning(
        f"[{request_id}] Erreur de validation : {exc.errors()} | URL: {request.url}"
    )
    return JSONResponse(
        status_code=422,
        content={
            "error": True,
            "code": "VALIDATION_ERROR",
            "message": "Erreur de validation.",
            "details": exc.errors(),
            "url": str(request.url),
            "request_id": request_id,
        },
    )


async def database_exception_handler(request: Request, exc: SQLAlchemyError):
    """
    Gestion des erreurs liées à SQLAlchemy.

    :param request: La requête FastAPI à l'origine de l'erreur.
    :param exc: L'exception SQLAlchemy levée.
    :return: JSONResponse avec un message d'erreur de base de données.
    """
    request_id = str(uuid.uuid4())
    logger.error(f"[{request_id}] Erreur SQLAlchemy : {exc} | URL: {request.url}")
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "code": "DATABASE_ERROR",
            "message": "Une erreur de base de données est survenue.",
            "url": str(request.url),
            "request_id": request_id,
        },
    )


async def global_exception_handler(request: Request, exc: Exception):
    """
    Gestion des erreurs globales non spécifiées.

    :param request: La requête FastAPI à l'origine de l'erreur.
    :param exc: L'exception levée.
    :return: JSONResponse avec un message générique d'erreur.
    """
    request_id = str(uuid.uuid4())
    logger.exception(f"[{request_id}] Erreur non gérée : {exc} | URL: {request.url}")
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "code": "INTERNAL_SERVER_ERROR",
            "message": "Une erreur interne est survenue.",
            "url": str(request.url),
            "request_id": request_id,
        },
    )


def handle_repository_exception(db: Session, e: Exception, message: str):
    """
    Gère les exceptions des repositories en effectuant un rollback et en enregistrant l'erreur.

    :param db: Session SQLAlchemy.
    :param e: Exception levée.
    :param message: Message d'erreur à enregistrer.
    """
    db.rollback()
    request_id = str(uuid.uuid4())
    logger.error(f"[{request_id}] {message} : {e}")
    raise RuntimeError(f"{message} : {e}")


def handle_global_exception(request, exc):
    """
    Gestion des erreurs globales non spécifiées.

    :param request: La requête FastAPI à l'origine de l'erreur.
    :param exc: L'exception levée.
    :return: JSONResponse avec un message générique d'erreur.
    """
    request_id = str(uuid.uuid4())
    logger.exception(f"[{request_id}] Erreur non gérée : {exc} | URL: {request.url}")
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "code": "INTERNAL_SERVER_ERROR",
            "message": "Une erreur interne est survenue.",
            "url": str(request.url),
            "request_id": request_id,
        },
    )
