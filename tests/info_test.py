from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_response():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}
