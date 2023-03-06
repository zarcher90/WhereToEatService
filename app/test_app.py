"""Main Application Test"""
from fastapi.testclient import TestClient

from app.application import app

client = TestClient(app)


def test_root():
    """Test the response at the root level"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Hallo :)"


def test_info():
    """Test the reponse for the info url"""
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "version" in data
    assert data["version"] == "1.1.0"
