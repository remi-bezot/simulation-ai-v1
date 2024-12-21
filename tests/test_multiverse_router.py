import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infrastructure.database.postgresql.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="module")
def client():
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c


def test_remove_multiverse(client):
    response = client.delete("/multiverses/1")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Erreur lors de la suppression du multivers : Multivers avec l'ID 1 non trouvé."
    }


def test_update_multiverse(client):
    response = client.put("/multiverses/1", json={"name": "Updated Multiverse"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Erreur lors de la mise à jour du multivers : Multivers avec l'ID 1 non trouvé."
    }
