import pytest

from framework.web.pages.inventory_page import InventoryPage
from framework.web.pages.login_page import LoginPage
from test_data.web_users import EMPTY_USER, INVALID_USER, VALID_USER


@pytest.mark.web
@pytest.mark.smoke
def test_valid_user_can_login(page):

    login_page = LoginPage(page)

    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"],
    )

    inventory_page = InventoryPage(page)

    assert inventory_page.is_loaded()
    assert inventory_page.get_product_count() > 0


@pytest.mark.web
@pytest.mark.regression
def test_invalid_user_cannot_login(page):

    login_page = LoginPage(page)

    login_page.login(
        INVALID_USER["username"],
        INVALID_USER["password"],
    )

    assert login_page.is_error_displayed()


@pytest.mark.web
@pytest.mark.regression
def test_empty_credentials_cannot_login(page):

    login_page = LoginPage(page)

    login_page.login(
        EMPTY_USER["username"],
        EMPTY_USER["password"],
    )

    assert login_page.is_error_displayed()