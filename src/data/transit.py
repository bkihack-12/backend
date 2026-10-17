from datetime import UTC, datetime
from typing import Any


def now_iso() -> str:
    return datetime.now(UTC).isoformat()


TRANSIT_NOTICES: list[dict[str, Any]] = [
    {
        "id": "tn-1",
        "type": "delay",
        "lines": ["1"],
        "stop": "Plac Rapackiego — Aleja Solidarności",
        "location": "Centrum — kierunek Olimpijska",
        "reportedAt": now_iso(),
        "severity": "medium",
        "impact": "Opóźnienie do 9 min",
        "status": "W toku",
        "description": "Tramwaje linii 1 kursują z opóźnieniem.",
        "source": "sample",
        "author": "MZK Toruń",
        "lat": 53.0118,
        "lng": 18.6062,
        "path": [
            {"lat": 53.0087, "lng": 18.6029},
            {"lat": 53.0156, "lng": 18.6225},
        ],
        "lengthLabel": "1,8 km trasy",
    },
    {
        "id": "tn-2",
        "type": "interruption",
        "lines": ["2", "4"],
        "stop": "ul. Gagarina / Aula UMK",
        "location": "Bielany — Bydgoskie Przedmieście",
        "reportedAt": now_iso(),
        "severity": "high",
        "impact": "Autobus zastępczy za tramwaj",
        "status": "Awaria sieci trakcyjnej",
        "description": "Wstrzymany ruch tramwajowy do CKK Jordanki.",
        "source": "sample",
        "author": "MZK Toruń",
        "lat": 53.0165,
        "lng": 18.5825,
        "path": [
            {"lat": 53.0185, "lng": 18.5665},
            {"lat": 53.0127, "lng": 18.5985},
        ],
        "lengthLabel": "2,4 km trasy",
    },
]
