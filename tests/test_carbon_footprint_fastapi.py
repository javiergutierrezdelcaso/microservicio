import os
import pytest
from fastapi.testclient import TestClient
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../carbon-footprint-fastapi')))
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Healthy"
    assert data["version"] == "1.1.0"

def test_analyze():
    text = "Hola mundo"
    response = client.get(f"/analyze?text={text}")
    assert response.status_code == 200
    data = response.json()
    assert data["input"] == text
    assert data["estimated_carbon_gco2"] > 0
    assert data["status"] == "Success"