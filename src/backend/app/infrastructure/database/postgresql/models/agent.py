from sqlalchemy import Column, Integer, String, JSON, DateTime, func, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Agent(Base):
    """
    Modèle SQLAlchemy pour représenter un agent.
    """

    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String(255), nullable=False, unique=True
    )  # Nom unique avec limite de longueur
    properties = Column(JSON, default={})  # Données dynamiques associées à l'agent
    created_at = Column(
        DateTime(timezone=True), server_default=func.now()
    )  # Date de création
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now()
    )  # Dernière mise à jour

    # Contraintes supplémentaires
    __table_args__ = (
        CheckConstraint(
            "jsonb_typeof(properties) IS NOT DISTINCT FROM 'object'",
            name="valid_properties_format",
        ),
    )

    def as_dict(self):
        """
        Retourne l'agent sous forme de dictionnaire.
        """
        return {
            "id": self.id,
            "name": self.name,
            "properties": self.properties,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
