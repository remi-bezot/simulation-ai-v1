import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.application.services.multiverse_service import MultiverseService
from app.application.repositories.multiverse_repository import MultiverseRepository
from app.infrastructure.database.postgresql.models.multiverse import Multiverse
from app.schemas.multiverse import MultiverseCreate, MultiverseUpdate
from app.application.utils.exceptions import MultiverseNotFoundError

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def multiverse_service(db):
    repository = MultiverseRepository(db)
    return MultiverseService(repository)


def test_create_multiverse(multiverse_service):
    data = MultiverseCreate(name="Test Multiverse")
    multiverse = multiverse_service.create_multiverse(data)
    assert multiverse.name == "Test Multiverse"


def test_delete_multiverse(multiverse_service, db):
    data = MultiverseCreate(name="Test Multiverse")
    multiverse = multiverse_service.create_multiverse(data)
    multiverse_id = multiverse.id

    multiverse_service.delete_multiverse(multiverse_id)
    with pytest.raises(MultiverseNotFoundError):
        multiverse_service.delete_multiverse(multiverse_id)


def test_update_multiverse(multiverse_service, db):
    data = MultiverseCreate(name="Test Multiverse")
    multiverse = multiverse_service.create_multiverse(data)
    multiverse_id = multiverse.id

    updates = MultiverseUpdate(name="Updated Multiverse")
    updated_multiverse = multiverse_service.update_multiverse(multiverse_id, updates)
    assert updated_multiverse.name == "Updated Multiverse"
