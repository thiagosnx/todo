from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post("/users/", json={"username": "testuser4", "password": "testpass4"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser4"

def test_login():
    response = client.post("/token/", data={"username": "testuser4", "password": "testpass4"})
    assert response.status_code == 200
    assert "access_token" in response.json()
