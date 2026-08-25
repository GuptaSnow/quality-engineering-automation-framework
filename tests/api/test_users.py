import pytest

from schemas.user_schema import User


@pytest.mark.api
@pytest.mark.smoke
def test_get_existing_user(users_api):

    response = users_api.get_user(1)

    assert response.status_code == 200

    body = response.json()

    user = User.model_validate(body)

    assert user.id == 1
    assert user.name
    assert user.email


@pytest.mark.api
@pytest.mark.regression
def test_get_non_existing_user(users_api):

    response = users_api.get_user(99999)

    assert response.status_code == 404


@pytest.mark.api
@pytest.mark.regression
def test_create_user(users_api):

    payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john@example.com"
    }

    response = users_api.create_user(payload)

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == payload["name"]
    assert body["username"] == payload["username"]
    assert body["email"] == payload["email"]