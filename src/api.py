from __future__ import annotations

from datetime import UTC, datetime
from itertools import count
from typing import Any

from flask import Flask, jsonify, request
from flask_cors import CORS


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)

    next_id = count(4)
    traffic_reports: list[dict[str, Any]] = [
        {
            "id": 1,
            "title": "Roboty drogowe",
            "description": "Zwężenie na ul. Szosa Lubicka",
            "severity": "medium",
            "lat": 53.018,
            "lng": 18.648,
            "createdAt": "2026-10-16T08:30:00Z",
        },
        {
            "id": 2,
            "title": "Stłuczka",
            "description": "Utrudnienia przy moście im. Piłsudskiego",
            "severity": "high",
            "lat": 53.008,
            "lng": 18.606,
            "createdAt": "2026-10-16T09:10:00Z",
        },
    ]
    events = [
        {
            "id": 1,
            "title": "Festiwal Wisły",
            "category": "culture",
            "venue": "Bulwar Filadelfijski",
            "interest": 92,
            "lat": 53.009,
            "lng": 18.606,
            "startsAt": "2026-10-17T16:00:00Z",
            "isPrivate": False,
        },
        {
            "id": 2,
            "title": "Koncert w CKK Jordanki",
            "category": "music",
            "venue": "CKK Jordanki",
            "interest": 78,
            "lat": 53.015,
            "lng": 18.600,
            "startsAt": "2026-10-18T19:00:00Z",
            "isPrivate": False,
        },
        {
            "id": 3,
            "title": "Planszówki znajomych",
            "category": "community",
            "venue": "Bydgoskie Przedmieście",
            "interest": 48,
            "lat": 53.021,
            "lng": 18.578,
            "startsAt": "2026-10-17T18:30:00Z",
            "isPrivate": True,
        },
    ]
    city_offers = [
        {
            "id": 1,
            "business": "Piekarnia Toruńska",
            "title": "Kawa -20%",
            "description": "Rabat z Kartą Mieszkańca",
            "category": "food",
            "citizenCard": True,
        },
        {
            "id": 2,
            "business": "Kino Centrum",
            "title": "Bilet 2D za 18 zł",
            "description": "Oferta ważna od poniedziałku do czwartku",
            "category": "entertainment",
            "citizenCard": True,
        },
        {
            "id": 3,
            "business": "Rowerowy Toruń",
            "title": "Serwis roweru -15%",
            "description": "Promocja sezonowa",
            "category": "services",
            "citizenCard": False,
        },
    ]
    transit_updates = [
        {
            "id": 1,
            "line": "Tramwaj 1",
            "title": "Opóźnienia do 12 min",
            "description": "Kierunek Olimpijska — Motoarena",
            "severity": "medium",
            "updatedAt": "2026-10-16T09:22:00Z",
        },
        {
            "id": 2,
            "line": "Autobus 15",
            "title": "Zmiana trasy",
            "description": "Przystanek Plac Rapackiego pominięty",
            "severity": "high",
            "updatedAt": "2026-10-16T08:55:00Z",
        },
    ]

    @app.get("/health")
    def health() -> Any:
        return jsonify(
            {
                "status": "ok",
                "city": "Toruń",
                "timestamp": datetime.now(UTC).isoformat(),
            }
        )

    @app.get("/api/dashboard")
    def dashboard() -> Any:
        return jsonify(
            {
                "city": "Toruń",
                "events": events,
                "traffic": traffic_reports,
                "offers": city_offers,
                "transit": transit_updates,
            }
        )

    @app.get("/api/events")
    def get_events() -> Any:
        category = request.args.get("category")
        minimum_interest = request.args.get("minInterest", default=0, type=int)
        visible = [
            event
            for event in events
            if event["interest"] >= minimum_interest
            and (not category or event["category"] == category)
        ]
        return jsonify(visible)

    @app.post("/api/traffic")
    def create_traffic_report() -> Any:
        payload = request.get_json(silent=True) or {}
        required = ("title", "description", "lat", "lng")
        if any(field not in payload for field in required):
            return jsonify({"error": "title, description, lat and lng are required"}), 400

        report = {
            "id": next(next_id),
            "severity": payload.get("severity", "medium"),
            "createdAt": datetime.now(UTC).isoformat(),
            **payload,
        }
        traffic_reports.insert(0, report)
        return jsonify(report), 201

    @app.get("/api/offers")
    def get_offers() -> Any:
        citizen_card = request.args.get("citizenCard")
        if citizen_card == "true":
            return jsonify([offer for offer in city_offers if offer["citizenCard"]])
        return jsonify(city_offers)

    @app.get("/api/transit")
    def get_transit() -> Any:
        return jsonify(transit_updates)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
