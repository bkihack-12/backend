import re
import secrets
from datetime import UTC, datetime
from typing import Any

from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

from data.users import TOKENS, USERS

auth_bp = Blueprint("auth", __name__)


def public_user(user: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "createdAt": user["createdAt"],
    }


def get_current_user() -> dict[str, Any] | None:
    header = request.headers.get("Authorization", "")

    if not header.startswith("Bearer "):
        return None

    token = header.removeprefix("Bearer ").strip()
    user_id = TOKENS.get(token)

    if user_id is None:
        return None

    return next(
        (user for user in USERS if user["id"] == user_id),
        None,
    )


def valid_email(email: str) -> bool:
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))


@auth_bp.post("/api/auth/register")
def register() -> Any:
    payload = request.get_json(silent=True) or {}

    name = str(payload.get("name", "")).strip()
    email = str(payload.get("email", "")).strip().lower()
    password = str(payload.get("password", ""))

    errors: dict[str, str] = {}

    if len(name) < 2:
        errors["name"] = "Name must contain at least 2 characters."

    if not valid_email(email):
        errors["email"] = "Enter a valid email address."

    if len(password) < 6:
        errors["password"] = "Password must contain at least 6 characters."

    if any(user["email"] == email for user in USERS):
        errors["email"] = "An account with this email already exists."

    if errors:
        return jsonify(
            {
                "error": "Validation failed",
                "fields": errors,
            }
        ), 400

    user = {
        "id": f"user-{len(USERS) + 1}",
        "name": name,
        "email": email,
        "passwordHash": generate_password_hash(password),
        "createdAt": datetime.now(UTC).isoformat(),
    }

    USERS.append(user)

    token = secrets.token_urlsafe(32)
    TOKENS[token] = user["id"]

    return jsonify(
        {
            "user": public_user(user),
            "token": token,
        }
    ), 201


@auth_bp.post("/api/auth/login")
def login() -> Any:
    payload = request.get_json(silent=True) or {}

    email = str(payload.get("email", "")).strip().lower()
    password = str(payload.get("password", ""))

    user = next(
        (item for item in USERS if item["email"] == email),
        None,
    )

    if user is None or not check_password_hash(
        user["passwordHash"],
        password,
    ):
        return jsonify(
            {
                "error": "Invalid email or password",
            }
        ), 401

    token = secrets.token_urlsafe(32)
    TOKENS[token] = user["id"]

    return jsonify(
        {
            "user": public_user(user),
            "token": token,
        }
    )


@auth_bp.get("/api/auth/me")
def me() -> Any:
    user = get_current_user()

    if user is None:
        return jsonify({"error": "Authentication required"}), 401

    return jsonify({"user": public_user(user)})


@auth_bp.post("/api/auth/logout")
def logout() -> Any:
    header = request.headers.get("Authorization", "")

    if header.startswith("Bearer "):
        token = header.removeprefix("Bearer ").strip()
        TOKENS.pop(token, None)

    return jsonify({"message": "Logged out successfully"})
