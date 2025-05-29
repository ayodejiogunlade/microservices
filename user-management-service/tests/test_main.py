import pytest
from fastapi.testclient import TestClient
from user_management_service.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_user_success():
    payload = {"username": "alice", "email": "alice@example.com", "password": "secret"}
    response = client.post("/users", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "User created"

def test_create_user_missing_fields():
    payload = {"username": "", "email": "", "password": ""}
    response = client.post("/users", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "All fields required"

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "users_created_total" in response.text

def test_chaos():
    response = client.get("/chaos")
    assert response.status_code == 500
    assert response.json()["detail"] == "Chaos monkey triggered!"
