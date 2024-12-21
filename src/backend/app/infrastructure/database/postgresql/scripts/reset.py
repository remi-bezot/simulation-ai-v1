from app.infrastructure.database.postgresql.database import engine
from app.infrastructure.database.postgresql.models import Base


def reset_postgres_database():
    """Réinitialiser la base PostgreSQL."""
    # Supprimer toutes les tables
    Base.metadata.drop_all(bind=engine)
    print("Base PostgreSQL réinitialisée.")

    # Recréer toutes les tables
    Base.metadata.create_all(bind=engine)
    print("Tables PostgreSQL recréées.")


if __name__ == "__main__":
    reset_postgres_database()
