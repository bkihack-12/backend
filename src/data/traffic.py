from datetime import UTC, datetime
from typing import Any


def now_iso() -> str:
    return datetime.now(UTC).isoformat()


TRAFFIC_REPORTS: list[dict[str, Any]] = [
    {
        "id": "tr-1",
        "type": "jam",
        "title": "Zator na Moście Piłsudskiego",
        "location": "Most im. Józefa Piłsudskiego",
        "reportedAt": now_iso(),
        "severity": "high",
        "impact": "+15 min",
        "status": "Utrzymuje się",
        "description": "Zator przez całą przeprawę w kierunku Placu Rapackiego.",
        "source": "sample",
        "lat": 53.0048,
        "lng": 18.5998,
        "path": [
            {"lat": 53.001, "lng": 18.5972},
            {"lat": 53.0087, "lng": 18.6029},
        ],
        "lengthLabel": "1,9 km",
    },
    {
        "id": "tr-2",
        "type": "roadworks",
        "title": "Zwężenie jezdni — wymiana asfaltu",
        "location": "ul. Szosa Chełmińska",
        "reportedAt": now_iso(),
        "severity": "medium",
        "impact": "+8 min",
        "status": "Ruch wahadłowy",
        "description": "Frezowanie i układanie nawierzchni na jednym pasie.",
        "source": "sample",
        "lat": 53.0218,
        "lng": 18.5975,
        "path": [
            {"lat": 53.01713, "lng": 18.600429},
            {"lat": 53.0234, "lng": 18.5961},
        ],
        "lengthLabel": "1,1 km",
    },
    {
        "id": "tr-3",
        "type": "accident",
        "title": "Kolizja dwóch aut osobowych",
        "location": "ul. Bydgoska / ul. Sienkiewicza",
        "reportedAt": now_iso(),
        "severity": "high",
        "impact": "+12 min",
        "status": "Zablokowany prawy pas",
        "description": "Zator w stronę Bydgoskiego Przedmieścia.",
        "source": "sample",
        "lat": 53.0142,
        "lng": 18.5835,
        "path": [
            {"lat": 53.0131, "lng": 18.5945},
            {"lat": 53.0152, "lng": 18.579},
        ],
        "lengthLabel": "1,5 km",
    },
]
