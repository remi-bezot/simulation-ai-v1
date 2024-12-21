
import pytest
from fastapi.testclient import TestClient
from src.backend.app.main import app

client = TestClient(app)

def test_get_worlds():
    response = client.get('/api/worlds/')
    assert response.status_code == 200
    assert 'worlds' in response.json()

def test_create_world():
    response = client.post('/api/worlds/', json={'name': 'Test World'})
    assert response.status_code == 200
    assert response.json()['message'] == 'World created'

