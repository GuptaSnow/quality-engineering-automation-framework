import pytest

from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
)

from framework.api.client import APIClient
from framework.api.users_api import UsersAPI
from framework.config.settings import Settings
from test_data.users import CREATE_USER_PAYLOAD


# =========================
# API Fixtures
# =========================

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


# =========================
# Web Fixtures
# =========================

@pytest.fixture(scope="session")
def browser(
    playwright: Playwright,
    settings,
) -> Browser:
    return playwright.chromium.launch(
        headless=settings.HEADLESS
    )


@pytest.fixture
def context(browser: Browser) -> BrowserContext:

    context = browser.new_context()

    yield context

    context.close()


@pytest.fixture
def page(
    context: BrowserContext,
    settings,
) -> Page:

    page = context.new_page()

    page.goto(settings.WEB_BASE_URL)

    yield page

    page.close()