import pytest
from fastapi.testclient import TestClient
from merchant_onboarding_service.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_onboard_success():
    payload = {"merchant_name": "Acme Corp", "kyc_passed": True}
    response = client.post("/onboard", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Merchant onboarded"

def test_onboard_kyc_failed():
    payload = {"merchant_name": "Acme Corp", "kyc_passed": False}
    response = client.post("/onboard", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "KYC not passed"

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "merchants_onboarded_total" in response.text

def test_chaos():
    response = client.get("/chaos")
    assert response.status_code == 500
    assert response.json()["detail"] == "Chaos monkey triggered!"
