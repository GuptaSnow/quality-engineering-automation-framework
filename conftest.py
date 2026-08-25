import pytest

from framework.api.client import APIClient
from framework.api.users_api import UsersAPI
from framework.config.settings import Settings
from test_data.users import CREATE_USER_PAYLOAD


@pytest.fixture(scope="session")
def settings():
    return Settings


@pytest.fixture(scope="session")
def api_client(settings):
    return APIClient(
        settings.API_BASE_URL
    )


@pytest.fixture(scope="session")
def users_api(api_client):
    return UsersAPI(api_client)


@pytest.fixture
def create_user_payload():
    return CREATE_USER_PAYLOAD.copy()