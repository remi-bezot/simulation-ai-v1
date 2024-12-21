from pydantic import BaseModel, Field, model_validator, validator
from typing import Optional, Dict, List
from enum import Enum


class AtmosphereType(str, Enum):
    """
    Enumération pour décrire les types d'atmosphères possibles.
    """

    OXYGEN = "oxygen"
    CO2 = "carbon_dioxide"
    NITROGEN = "nitrogen"


class Properties(BaseModel):
    """
    Schéma pour les propriétés dynamiques associées à un multivers.
    """

    gravity: Optional[float] = Field(
        9.8, description="Gravité en m/s² (par défaut 9.8, doit être positive)"
    )
    atmosphere: Optional[AtmosphereType] = Field(
        default=AtmosphereType.OXYGEN, description="Type d'atmosphère (par défaut: oxygen)"
    )

    @model_validator(mode="before")
    @classmethod
    def validate_gravity(cls, values):
        if "gravity" in values:
            try:
                gravity = float(values["gravity"])
                if gravity <= 0:
                    raise ValueError("La gravité doit être un nombre positif.")
            except (ValueError, TypeError):
                raise ValueError("La gravité doit être un nombre valide.")
        return values


# Schéma de base du Multiverse
class MultiverseBase(BaseModel):
    name: str = Field(
        ..., description="Nom du multivers (obligatoire, au moins 3 caractères)"
    )
    description: Optional[str] = Field(
        None, description="Description optionnelle du multivers"
    )
    properties: Optional[Properties] = Field(
        default=None, description="Propriétés dynamiques du multivers"
    )

    @validator("name")
    def validate_name(cls, value):
        if len(value.strip()) < 3:
            raise ValueError("Le nom du multivers doit contenir au moins 3 caractères.")
        return value


# Schéma pour la création d'un Multiverse
class MultiverseCreate(MultiverseBase):
    pass


# Schéma pour la mise à jour d'un Multiverse
class MultiverseUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Nom du multivers")
    description: Optional[str] = Field(None, description="Description du multivers")
    properties: Optional[Properties] = Field(
        None, description="Propriétés dynamiques du multivers"
    )


# Schéma pour la réponse d'un Multiverse
class Multiverse(MultiverseBase):
    id: int
    universes: Optional[List[Dict]] = Field(
        default_factory=list, description="Liste des univers associés"
    )

    class Config:
        from_attributes = True  # Compatibilité avec SQLAlchemy pour Pydantic v2
