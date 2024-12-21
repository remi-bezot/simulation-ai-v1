from app.infrastructure.database.postgresql.database import SessionLocal
from app.infrastructure.database.postgresql.models import Agent


def seed_postgres_data():
    """Insérer des données initiales dans PostgreSQL."""
    db = SessionLocal()
    try:
        agent1 = Agent(name="Agent Alpha", properties={"role": "explorer"})
        agent2 = Agent(name="Agent Beta", properties={"role": "scientist"})
        db.add_all([agent1, agent2])
        db.commit()
        print("Données initiales insérées dans PostgreSQL.")
    finally:
        db.close()


if __name__ == "__main__":
    seed_postgres_data()
