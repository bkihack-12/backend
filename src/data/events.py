from datetime import UTC, datetime, timedelta
from typing import Any


def _date(days: int, hour: int, minute: int) -> tuple[str, str]:
    start = datetime.now(UTC).replace(
        hour=hour,
        minute=minute,
        second=0,
        microsecond=0,
    ) + timedelta(days=days)

    end = start + timedelta(hours=2)

    return start.isoformat(), end.isoformat()


def build_events() -> list[dict[str, Any]]:
    today_start, today_end = _date(0, 19, 0)
    tomorrow_start, tomorrow_end = _date(1, 20, 30)
    weekend_start, weekend_end = _date(2, 12, 0)

    return [
        {
            "id": "ev-rynek-jazz",
            "title": "Jesienny jazz na Rynku",
            "category": "muzyka",
            "startsAt": today_start,
            "endsAt": today_end,
            "venue": "Rynek Staromiejski",
            "address": "Rynek Staromiejski 1, Toruń",
            "lat": 53.01035,
            "lng": 18.60425,
            "isFree": True,
            "priceZl": None,
            "type": "open",
            "capacity": None,
            "taken": None,
            "action": None,
            "interested": 214,
            "description": "Plenerowy koncert toruńskich zespołów jazzowych.",
            "organizer": "Stowarzyszenie Muzyczny Toruń",
        },
        {
            "id": "ev-planetarium",
            "title": "Nocne niebo jesienią",
            "category": "edukacja",
            "startsAt": tomorrow_start,
            "endsAt": tomorrow_end,
            "venue": "Planetarium Toruń",
            "address": "ul. Franciszkańska 15/21, Toruń",
            "lat": 53.01165,
            "lng": 18.6112,
            "isFree": False,
            "priceZl": 28,
            "type": "limited",
            "capacity": 90,
            "taken": 84,
            "action": "ticket",
            "interested": 132,
            "description": "Seans o jesiennych konstelacjach i planetach.",
            "organizer": "Planetarium Toruń",
        },
        {
            "id": "ev-piernik",
            "title": "Warsztaty wypieku toruńskich pierników",
            "category": "rodzina",
            "startsAt": weekend_start,
            "endsAt": weekend_end,
            "venue": "Muzeum Toruńskiego Piernika",
            "address": "ul. Rabiańska 9, Toruń",
            "lat": 53.0107,
            "lng": 18.6081,
            "isFree": False,
            "priceZl": 45,
            "type": "limited",
            "capacity": 24,
            "taken": 15,
            "action": "ticket",
            "interested": 97,
            "description": "Rodzinne warsztaty wypieku i dekorowania pierników.",
            "organizer": "Manufaktura Piernika",
        },
        {
            "id": "ev-food-truck",
            "title": "Festiwal food trucków nad Wisłą",
            "category": "jedzenie",
            "startsAt": weekend_start,
            "endsAt": weekend_end,
            "venue": "Bulwar Filadelfijski",
            "address": "Bulwar Filadelfijski, Toruń",
            "lat": 53.00695,
            "lng": 18.6044,
            "isFree": True,
            "priceZl": None,
            "type": "open",
            "capacity": None,
            "taken": None,
            "action": None,
            "interested": 402,
            "description": "Ponad 20 food trucków, muzyka i strefa dla dzieci.",
            "organizer": "Toruńska Gastro Ekipa",
        },
    ]
