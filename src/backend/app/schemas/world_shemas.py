from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, constr


class WorldBase(BaseModel):
    """
    Schéma de base pour un monde.
    """

    name: constr(strip_whitespace=True, min_length=1) = Field(
        ..., description="Nom du monde (doit contenir au moins 1 caractère)."
    )
    description: Optional[str] = Field(
        None, description="Nouvelle description du monde."
    )
    properties: Optional[Dict[str, Any]] = Field(
        None, description="Mises à jour des propriétés du monde."
    )


class WorldCreate(WorldBase):
    """
    Schéma pour créer un nouveau monde.
    """

    properties: Optional[Dict[str, Any]] = Field(
        default_factory=dict, description="Propriétés supplémentaires du monde."
    )


class WorldUpdate(BaseModel):
    """
    Schéma pour mettre à jour un monde existant.
    """

    name: Optional[constr(strip_whitespace=True, min_length=1)] = Field(
        None, description="Nouveau nom du monde."
    )
    description: Optional[str] = Field(
        None, description="Nouvelle description du monde."
    )
    properties: Optional[Dict[str, Any]] = Field(
        None, description="Mises à jour des propriétés du monde."
    )


class WorldResponse(WorldBase):
    """
    Schéma pour retourner un monde existant.
    """

    id: int = Field(..., description="Identifiant unique du monde.")
    properties: Dict[str, Any] = Field(
        default_factory=dict, description="Propriétés du monde."
    )

    class Config:
        orm_mode = True
