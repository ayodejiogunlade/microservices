import pytest
from fastapi.testclient import TestClient
from wallet_service.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_wallet_transaction_success():
    payload = {"user_id": "bob", "amount": 50, "type": "deposit"}
    response = client.post("/wallets/transaction", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Transaction complete"

def test_wallet_transaction_invalid():
    payload = {"user_id": "bob", "amount": -10, "type": "withdraw"}
    response = client.post("/wallets/transaction", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid transaction request"

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "wallet_transactions_total" in response.text

def test_chaos():
    response = client.get("/chaos")
    assert response.status_code == 500
    assert response.json()["detail"] == "Chaos monkey triggered!"
