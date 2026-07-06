
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_create_short_url():

    response = client.post(
        "/shorten",
        json={
            "original_url": "https://google.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "short_code" in data

    assert data["original_url"] == "https://google.com"


def test_get_all_urls():

    response = client.get("/urls")

    assert response.status_code == 200
