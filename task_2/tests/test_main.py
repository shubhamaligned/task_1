import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)  # Use TestClient instead of AsyncClient

def test_create_post():
    response = client.post("/posts/", json={
        "title": "Test Post",
        "content": "This is a test post",
        "author": "Shubham"
    })
    assert response.status_code == 201
    data = response.json()
    assert "title" in data and data["title"] == "Test Post"