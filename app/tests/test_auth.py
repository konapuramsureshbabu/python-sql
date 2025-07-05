import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post(
        "/auth/register",
        json={"username": "testuser", "email": "test@example.com", "password": "securepassword"}
    )
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"

def test_login():
    # First register a user
    client.post(
        "/auth/register",
        json={"username": "testuser2", "email": "test2@example.com", "password": "securepassword"}
    )
    # Then login
    response = client.post(
        "/auth/login",
        data={"username": "testuser2", "password": "securepassword"}
    )
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"