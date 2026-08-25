import pytest

from framework.web.pages.cart_page import CartPage
from framework.web.pages.inventory_page import InventoryPage
from framework.web.pages.login_page import LoginPage
from test_data.web_users import VALID_USER


@pytest.fixture
def logged_in_inventory(page):

    login_page = LoginPage(page)

    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"],
    )

    return InventoryPage(page)


@pytest.mark.web
@pytest.mark.smoke
def test_user_can_add_product_to_cart(logged_in_inventory):

    product_name = "Sauce Labs Backpack"

    logged_in_inventory.add_product_to_cart(
        product_name
    )

    logged_in_inventory.open_cart()

    cart_page = CartPage(logged_in_inventory.page)

    assert cart_page.is_product_in_cart(
        product_name
    )


@pytest.mark.web
@pytest.mark.regression
def test_user_can_remove_product_from_cart(logged_in_inventory):

    product_name = "Sauce Labs Backpack"

    logged_in_inventory.add_product_to_cart(
        product_name
    )

    logged_in_inventory.open_cart()

    cart_page = CartPage(logged_in_inventory.page)

    assert cart_page.is_product_in_cart(
        product_name
    )

    # Go back to inventory
    logged_in_inventory.page.go_back()

    logged_in_inventory.remove_product_from_cart(
        product_name
    )

    logged_in_inventory.open_cart()

    assert cart_page.is_product_not_in_cart(
        product_name
    )