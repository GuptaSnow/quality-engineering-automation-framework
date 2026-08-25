from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator(
            '[data-test="inventory-item"]'
        )

        self.checkout_button = page.locator(
            '[data-test="checkout"]'
        )

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def is_product_in_cart(self, product_name: str) -> bool:
        return self.cart_items.filter(
            has_text=product_name
        ).is_visible()

    def is_product_not_in_cart(self, product_name: str) -> bool:
        return self.cart_items.filter(
            has_text=product_name
        ).count() == 0

    def checkout(self):
        self.checkout_button.click()