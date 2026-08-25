import pytest

from framework.web.pages.cart_page import CartPage
from framework.web.pages.checkout_page import CheckoutPage
from framework.web.pages.inventory_page import InventoryPage
from framework.web.pages.login_page import LoginPage
from test_data.web_users import VALID_USER


@pytest.fixture
def checkout_page(page):

    login_page = LoginPage(page)

    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"],
    )

    inventory_page = InventoryPage(page)

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory_page.open_cart()

    cart_page = CartPage(page)

    cart_page.checkout()

    return CheckoutPage(page)


@pytest.mark.web
@pytest.mark.smoke
def test_user_can_complete_checkout(checkout_page):

    checkout_page.enter_customer_information(
        first_name="John",
        last_name="Doe",
        postal_code="12345",
    )

    checkout_page.continue_to_overview()

    checkout_page.finish_order()

    assert checkout_page.is_order_complete()


@pytest.mark.web
@pytest.mark.regression
def test_checkout_requires_first_name(checkout_page):

    checkout_page.enter_customer_information(
        first_name="",
        last_name="Doe",
        postal_code="12345",
    )

    checkout_page.continue_to_overview()

    assert checkout_page.is_error_displayed()