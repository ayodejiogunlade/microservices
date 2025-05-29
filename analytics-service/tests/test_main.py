import pytest
from fastapi.testclient import TestClient
from analytics_service.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_report():
    response = client.get("/analytics/report?report_type=summary&start_date=2025-01-01&end_date=2025-01-31")
    assert response.status_code == 200
    assert "report" in response.json()

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "analytics_reports_total" in response.text

def test_chaos():
    response = client.get("/chaos")
    assert response.status_code == 500
    assert response.json()["detail"] == "Chaos monkey triggered!"
