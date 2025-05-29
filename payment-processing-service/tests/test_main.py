import pytest
from fastapi.testclient import TestClient
from payment_processing_service.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_process_payment_success():
    payload = {"amount": 100, "currency": "USD", "user_id": "user123"}
    response = client.post("/payments", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Payment processed"

def test_process_payment_invalid_amount():
    payload = {"amount": 0, "currency": "USD", "user_id": "user123"}
    response = client.post("/payments", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Amount must be positive"

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "payments_processed_total" in response.text

def test_fraud_check():
    response = client.get("/fraud-check", params={"user_id": "user123"})
    assert response.status_code == 200
    assert response.json()["fraudulent"] is False

def test_chaos():
    response = client.get("/chaos")
    assert response.status_code == 500
    assert response.json()["detail"] == "Chaos monkey triggered!"
