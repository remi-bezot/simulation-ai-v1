from pydantic import BaseModel, Field, model_validator
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
        AtmosphereType.OXYGEN, description="Type d'atmosphère (par défaut: oxygen)"
    )

    @model_validator(mode="before")
    @classmethod
    def validate_properties(cls, values):
        if "gravity" in values:
            try:
                gravity = float(values["gravity"])
                if gravity <= 0:
                    raise ValueError("La gravité doit être un nombre positif.")
            except (ValueError, TypeError):
                raise ValueError("La gravité doit être un nombre valide.")
        return values


class MultiverseBase(BaseModel):
    """
    Schéma de base pour un multivers.
    """

    name: str = Field(
        ..., description="Nom du multivers (obligatoire, au moins 3 caractères)"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Description du multivers (500 caractères max)",
    )
    properties: Optional[Properties] = Field(
        default_factory=Properties, description="Propriétés dynamiques"
    )

    @model_validator(mode="before")
    @classmethod
    def validate_multiverse(cls, values):
        name = values.get("name", "").strip()
        if len(name) < 3:
            raise ValueError("Le nom du multivers doit contenir au moins 3 caractères.")
        return values


class UniverseLight(BaseModel):
    """
    Schéma pour un univers léger dans un multivers.
    """

    id: int
    name: str


class MultiverseCreate(MultiverseBase):
    """
    Schéma pour la création d'un nouveau multivers.
    """

    pass


class MultiverseUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'un multivers existant.
    """

    name: Optional[str] = Field(None, description="Nom du multivers")
    description: Optional[str] = Field(None, description="Description du multivers")
    properties: Optional[Properties] = Field(
        None, description="Propriétés dynamiques du multivers"
    )


class Multiverse(MultiverseBase):
    """
    Schéma pour un multivers retourné par l'API.
    """

    id: int = Field(..., description="ID unique du multivers")
    universes: Optional[List[UniverseLight]] = Field(
        default_factory=list,
        description="Liste des univers associés (format léger)",
    )

    class Config:
        from_attributes = True  # Compatibilité avec SQLAlchemy pour Pydantic v2
