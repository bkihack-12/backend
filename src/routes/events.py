from typing import Any

from flask import Blueprint, jsonify, request

from routes.dashboard import EVENTS

events_bp = Blueprint("events", __name__)


@events_bp.get("/api/events")
def get_events() -> Any:
    category = request.args.get("category")
    minimum_interest = request.args.get("minInterest", default=0, type=int)

    result = [
        event
        for event in EVENTS
        if event["interested"] >= minimum_interest
        and (not category or event["category"] == category)
    ]

    return jsonify(result)


@events_bp.post("/api/events/<event_id>/interest")
def add_interest(event_id: str) -> Any:
    event = next(
        (item for item in EVENTS if item["id"] == event_id),
        None,
    )

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    event["interested"] += 1

    return jsonify(
        {
            "eventId": event_id,
            "interested": event["interested"],
        }
    )
