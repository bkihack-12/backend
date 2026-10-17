import pytest

from api import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_get_traffic(client):
    response = client.get("/api/traffic")

    assert response.status_code == 200
    assert response.get_json()


def test_create_traffic_report(client):
    response = client.post(
        "/api/traffic",
        json={
            "type": "jam",
            "location": "Most Piłsudskiego",
            "description": "Duży korek",
        },
    )

    assert response.status_code == 201

    report = response.get_json()

    assert report["source"] == "user"
    assert report["lat"] == 53.0055
    assert report["lng"] == 18.6003


def test_traffic_report_requires_fields(client):
    response = client.post(
        "/api/traffic",
        json={
            "type": "jam",
        },
    )

    assert response.status_code == 400
