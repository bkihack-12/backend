from datetime import UTC, datetime
from typing import Any

from flask import Blueprint, jsonify

from config import TORUN_CENTER
from data.events import build_events
from data.offers import OFFERS
from data.traffic import TRAFFIC_REPORTS
from data.transit import TRANSIT_NOTICES

dashboard_bp = Blueprint("dashboard", __name__)

EVENTS = build_events()


@dashboard_bp.get("/health")
def health() -> Any:
    return jsonify(
        {
            "status": "ok",
            "city": "Toruń",
            "timestamp": datetime.now(UTC).isoformat(),
        }
    )


@dashboard_bp.get("/api/dashboard")
def dashboard() -> Any:
    heatmap = [
        {
            "lat": event["lat"],
            "lng": event["lng"],
            "intensity": min(1, event["interested"] / 500),
            "eventId": event["id"],
        }
        for event in EVENTS
    ]

    return jsonify(
        {
            "city": "Toruń",
            "center": TORUN_CENTER,
            "events": EVENTS,
            "traffic": TRAFFIC_REPORTS,
            "incidents": TRAFFIC_REPORTS,
            "transit": TRANSIT_NOTICES,
            "notices": TRANSIT_NOTICES,
            "offers": OFFERS,
            "heatmap": heatmap,
        }
    )
