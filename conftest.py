import pytest

from framework.api.client import APIClient
from framework.api.users_api import UsersAPI
from framework.config.settings import Settings


@pytest.fixture(scope="session")
def api_client():
    return APIClient(
        Settings.API_BASE_URL
    )


@pytest.fixture(scope="session")
def users_api(api_client):
    return UsersAPI(api_client)