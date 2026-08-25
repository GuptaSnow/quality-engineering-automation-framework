import os

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
# Pytest Reporting Hook
# =========================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call":
        item.rep_call = report


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
def context(
    browser: Browser,
    settings,
    request,
) -> BrowserContext:

    context = browser.new_context(
        base_url=settings.WEB_BASE_URL,
        viewport={
            "width": 1440,
            "height": 900,
        },
    )

    # Start Playwright tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    yield context

    # Save trace only when the test fails
    if request.node.rep_call.failed:

        os.makedirs(
            "artifacts/traces",
            exist_ok=True,
        )

        trace_path = (
            "artifacts/traces/"
            f"{request.node.name}.zip"
        )

        context.tracing.stop(
            path=trace_path
        )

    else:
        context.tracing.stop()

    context.close()


@pytest.fixture
def page(
    context: BrowserContext,
    request,
) -> Page:

    page = context.new_page()

    # Default Playwright timeouts
    page.set_default_timeout(10_000)
    page.set_default_navigation_timeout(15_000)

    # Navigate to the configured application
    page.goto("/")

    yield page

    # Capture screenshot when test fails
    if request.node.rep_call.failed:

        os.makedirs(
            "artifacts/screenshots",
            exist_ok=True,
        )

        screenshot_path = (
            "artifacts/screenshots/"
            f"{request.node.name}.png"
        )

        page.screenshot(
            path=screenshot_path,
            full_page=True,
        )

    page.close()