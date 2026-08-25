import pytest

from framework.web.pages.inventory_page import InventoryPage
from framework.web.pages.login_page import LoginPage
from test_data.web_users import VALID_USER


@pytest.fixture
def inventory_page(page):

    login_page = LoginPage(page)

    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"],
    )

    return InventoryPage(page)


@pytest.mark.web
@pytest.mark.smoke
def test_products_are_displayed(inventory_page):

    assert inventory_page.is_loaded()
    assert inventory_page.get_product_count() > 0


@pytest.mark.web
@pytest.mark.regression
def test_products_can_be_sorted_a_to_z(inventory_page):

    inventory_page.sort_products("az")

    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names)


@pytest.mark.web
@pytest.mark.regression
def test_user_can_open_product(inventory_page):

    product_name = "Sauce Labs Backpack"

    assert inventory_page.is_product_displayed(product_name)

    inventory_page.open_product(product_name)

    assert "inventory-item.html" in inventory_page.page.url