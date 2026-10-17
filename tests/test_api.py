import pytest

from api import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_dashboard_matches_mobile_modules(client):
    response = client.get("/api/dashboard")

    assert response.status_code == 200

    body = response.get_json()

    assert body["city"] == "Toruń"
    assert {
        "events",
        "traffic",
        "incidents",
        "transit",
        "notices",
        "offers",
        "heatmap",
    } <= body.keys()

    assert body["events"][0]["id"].startswith("ev-")
    assert "path" in body["traffic"][0]


def test_event_interest_filter_and_shape(client):
    response = client.get("/api/events?minInterest=200&category=muzyka")

    assert response.status_code == 200

    events = response.get_json()

    assert events
    assert all(event["interested"] >= 200 for event in events)
    assert events[0]["category"] == "muzyka"

    assert {
        "startsAt",
        "endsAt",
        "venue",
        "lat",
        "lng",
        "organizer",
    } <= events[0].keys()


def test_create_traffic_report_matches_mobile_shape(client):
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
    assert report["path"] == []
    assert report["lat"]
    assert report["lng"]


def test_create_transit_notice(client):
    response = client.post(
        "/api/transit",
        json={
            "type": "delay",
            "lines": ["1"],
            "stop": "Plac Rapackiego",
            "description": "Opóźnienie 5 minut",
        },
    )

    assert response.status_code == 201
    assert response.get_json()["source"] == "user"


def test_citizen_card_offers(client):
    response = client.get("/api/offers?citizenCard=true")

    assert response.status_code == 200
    assert response.get_json()
    assert all(offer["tkm"] is True for offer in response.get_json())


def test_missing_traffic_fields_returns_bad_request(client):
    response = client.post("/api/traffic", json={"type": "jam"})

    assert response.status_code == 400
