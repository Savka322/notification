from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_notification():
    response = client.post(
        "/api/v1/notifications/",
        json={"user_id": "123e4567-e89b-12d3-a456-426614174000", "title": "Test", "text": "This is a test notification."},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test"

def test_read_notifications():
    response = client.get("/api/v1/notifications/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_notification():
    response = client.post(
        "/api/v1/notifications/",
        json={"user_id": "123e4567-e89b-12d3-a456-426614174000", "title": "Test Read", "text": "This is a test notification."},
    )
    notification_id = response.json()["id"]
    response = client.get(f"/api/v1/notifications/{notification_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Read"