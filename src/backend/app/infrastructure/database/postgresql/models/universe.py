from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    DateTime,
    func,
    ForeignKey,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from app.infrastructure.database.postgresql.models.base import Base


class Universe(Base):
    """
    Modèle SQLAlchemy pour représenter un univers dans le multivers.
    """

    __tablename__ = "universes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(500), nullable=True)
    properties = Column(JSON, default={})
    color = Column(String(7), nullable=True)

    # Champs de date
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Clé étrangère pour relier à un multivers
    multiverse_id = Column(Integer, ForeignKey("multiverses.id", ondelete="CASCADE"))
    multiverse = relationship("Multiverse", back_populates="universes")

    # Contraintes supplémentaires
    __table_args__ = (
        CheckConstraint(
            "color ~ '^#(?:[0-9a-fA-F]{3}){1,2}$'", name="valid_color_format"
        ),
    )

    def as_dict(self):
        """Retourner l'objet sous forme de dictionnaire."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "properties": self.properties,
            "color": self.color,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "multiverse_id": self.multiverse_id,
        }
