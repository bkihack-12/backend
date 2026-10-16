import pytest

from api import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_dashboard_contains_city_modules(client):
    response = client.get("/api/dashboard")
    assert response.status_code == 200
    body = response.get_json()
    assert body["city"] == "Toruń"
    assert {"events", "traffic", "offers", "transit"} <= body.keys()


def test_event_interest_filter(client):
    response = client.get("/api/events?minInterest=80")
    assert response.status_code == 200
    assert all(event["interest"] >= 80 for event in response.get_json())


def test_traffic_report_requires_location(client):
    response = client.post("/api/traffic", json={"title": "Test"})
    assert response.status_code == 400
