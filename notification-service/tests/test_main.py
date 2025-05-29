import pytest
from fastapi.testclient import TestClient
from notification_service.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_notify_success():
    payload = {"user_id": "bob", "message": "Hello!", "channel": "email"}
    response = client.post("/notify", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Notification sent"

def test_notify_invalid_channel():
    payload = {"user_id": "bob", "message": "Hi!", "channel": "invalid"}
    response = client.post("/notify", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid notification channel"

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "notifications_sent_total" in response.text

def test_chaos():
    response = client.get("/chaos")
    assert response.status_code == 500
    assert response.json()["detail"] == "Chaos monkey triggered!"
