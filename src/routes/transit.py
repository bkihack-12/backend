from datetime import UTC, datetime
from itertools import count
from typing import Any

from flask import Blueprint, jsonify, request

from config import ALLOWED_TRANSIT_TYPES
from data.transit import TRANSIT_NOTICES
from utils.location import infer_location

transit_bp = Blueprint("transit", __name__)
_next_id = count(100)


@transit_bp.get("/api/transit")
def get_transit() -> Any:
    return jsonify(TRANSIT_NOTICES)


@transit_bp.post("/api/transit")
def create_transit_notice() -> Any:
    payload = request.get_json(silent=True) or {}

    required = ("type", "lines", "stop", "description")

    if any(not payload.get(field) for field in required):
        return jsonify(
            {
                "error": "type, lines, stop and description are required",
            }
        ), 400

    if payload["type"] not in ALLOWED_TRANSIT_TYPES:
        return jsonify({"error": "Invalid transit notice type"}), 400

    lat, lng = infer_location(payload["stop"])

    notice = {
        "id": f"tn-user-{next(_next_id)}",
        "type": payload["type"],
        "lines": payload["lines"],
        "stop": payload["stop"].strip(),
        "location": payload["stop"].strip(),
        "reportedAt": datetime.now(UTC).isoformat(),
        "severity": payload.get("severity", "medium"),
        "impact": "Zgłoszenie pasażera",
        "status": "Nowe zgłoszenie",
        "description": payload["description"].strip(),
        "source": "user",
        "author": payload.get("author", "Gość"),
        "lat": lat,
        "lng": lng,
        "path": [],
        "lengthLabel": "1,2 km trasy",
    }

    TRANSIT_NOTICES.insert(0, notice)

    return jsonify(notice), 201
