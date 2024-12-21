from sqlalchemy import Column, Integer, String, JSON, DateTime, func, CheckConstraint
from sqlalchemy.orm import relationship
from app.infrastructure.database.postgresql.models.base import Base


class Multiverse(Base):
    """
    Modèle SQLAlchemy pour représenter un multivers contenant plusieurs univers.
    """

    __tablename__ = "multiverses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(500), nullable=True)
    properties = Column(JSON, default={})  # Données dynamiques associées au multivers
    created_at = Column(
        DateTime(timezone=True), server_default=func.now()
    )  # Date de création
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now()
    )  # Dernière mise à jour

    # Relation avec les univers
    universes = relationship(
        "Universe",
        back_populates="multiverse",
        cascade="all, delete-orphan",  # Supprime les univers liés lors de la suppression d'un multivers
    )

    # Contraintes supplémentaires
    __table_args__ = (
        CheckConstraint(
            "jsonb_typeof(properties) IS NOT DISTINCT FROM 'object'",
            name="valid_multiverse_properties_format",
        ),
    )

    def as_dict(self):
        """
        Retourne le multivers sous forme de dictionnaire.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "properties": self.properties,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "universes": [
                universe.as_dict() for universe in self.universes
            ],  # Inclure les univers liés
        }
