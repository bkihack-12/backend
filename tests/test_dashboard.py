import pytest

from api import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["city"] == "Toruń"


def test_dashboard(client):
    response = client.get("/api/dashboard")
    body = response.get_json()

    assert response.status_code == 200
    assert body["city"] == "Toruń"
    assert "events" in body
    assert "traffic" in body
    assert "transit" in body
    assert "offers" in body
    assert "heatmap" in body
