import pytest

from api import create_app
from data.users import TOKENS, USERS


@pytest.fixture
def client():
    USERS.clear()
    TOKENS.clear()
    return create_app().test_client()


def test_register_user(client):
    response = client.post(
        "/api/auth/register",
        json={
            "name": "Jan Kowalski",
            "email": "jan@example.com",
            "password": "secret123",
        },
    )

    assert response.status_code == 201

    body = response.get_json()

    assert body["user"]["name"] == "Jan Kowalski"
    assert body["user"]["email"] == "jan@example.com"
    assert body["token"]


def test_login_user(client):
    client.post(
        "/api/auth/register",
        json={
            "name": "Jan Kowalski",
            "email": "jan@example.com",
            "password": "secret123",
        },
    )

    response = client.post(
        "/api/auth/login",
        json={
            "email": "jan@example.com",
            "password": "secret123",
        },
    )

    assert response.status_code == 200
    assert response.get_json()["token"]


def test_invalid_login(client):
    response = client.post(
        "/api/auth/login",
        json={
            "email": "unknown@example.com",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401


def test_current_user(client):
    register_response = client.post(
        "/api/auth/register",
        json={
            "name": "Jan Kowalski",
            "email": "jan@example.com",
            "password": "secret123",
        },
    )

    token = register_response.get_json()["token"]

    response = client.get(
        "/api/auth/me",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200
    assert response.get_json()["user"]["email"] == "jan@example.com"


def test_logout(client):
    register_response = client.post(
        "/api/auth/register",
        json={
            "name": "Jan Kowalski",
            "email": "jan@example.com",
            "password": "secret123",
        },
    )

    token = register_response.get_json()["token"]

    response = client.post(
        "/api/auth/logout",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    me_response = client.get(
        "/api/auth/me",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert me_response.status_code == 401
