from datetime import UTC, datetime
from itertools import count
from typing import Any

from flask import Blueprint, jsonify, request

from config import ALLOWED_TRAFFIC_TYPES
from data.traffic import TRAFFIC_REPORTS
from utils.location import infer_location

traffic_bp = Blueprint("traffic", __name__)
_next_id = count(100)


@traffic_bp.get("/api/traffic")
def get_traffic() -> Any:
    severity = request.args.get("severity")

    result = [
        report for report in TRAFFIC_REPORTS if not severity or report["severity"] == severity
    ]

    return jsonify(result)


@traffic_bp.post("/api/traffic")
def create_traffic_report() -> Any:
    payload = request.get_json(silent=True) or {}

    required = ("type", "location", "description")

    if any(not payload.get(field) for field in required):
        return jsonify(
            {
                "error": "type, location and description are required",
            }
        ), 400

    if payload["type"] not in ALLOWED_TRAFFIC_TYPES:
        return jsonify({"error": "Invalid traffic report type"}), 400

    lat = payload.get("lat")
    lng = payload.get("lng")

    if lat is None or lng is None:
        lat, lng = infer_location(payload["location"])

    report = {
        "id": f"tr-user-{next(_next_id)}",
        "type": payload["type"],
        "title": payload.get("title", "Nowe zgłoszenie drogowe"),
        "location": payload["location"].strip(),
        "reportedAt": datetime.now(UTC).isoformat(),
        "severity": payload.get("severity", "medium"),
        "impact": "Zgłoszenie mieszkańca",
        "status": "Nowe zgłoszenie",
        "description": payload["description"].strip(),
        "source": "user",
        "author": payload.get("author", "Gość"),
        "lat": lat,
        "lng": lng,
        "path": [],
        "lengthLabel": payload.get("lengthLabel", "500 m"),
    }

    TRAFFIC_REPORTS.insert(0, report)

    return jsonify(report), 201
