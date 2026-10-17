import pytest

from api import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_filter_events_by_category(client):
    response = client.get("/api/events?category=muzyka")

    assert response.status_code == 200
    assert response.get_json()
    assert all(event["category"] == "muzyka" for event in response.get_json())


def test_filter_events_by_interest(client):
    response = client.get("/api/events?minInterest=200")

    assert response.status_code == 200
    assert all(event["interested"] >= 200 for event in response.get_json())


def test_add_event_interest(client):
    response = client.post("/api/events/ev-rynek-jazz/interest")

    assert response.status_code == 200
    assert response.get_json()["interested"] > 214
