from typing import Any

from flask import Blueprint, jsonify, request

from data.offers import BENEFITS, OFFERS

offers_bp = Blueprint("offers", __name__)


@offers_bp.get("/api/offers")
def get_offers() -> Any:
    citizen_card = request.args.get("citizenCard")

    if citizen_card == "true":
        return jsonify([offer for offer in OFFERS if offer["tkm"] is True])

    return jsonify(OFFERS)


@offers_bp.get("/api/benefits")
def get_benefits() -> Any:
    return jsonify(BENEFITS)
