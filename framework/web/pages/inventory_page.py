from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        self.inventory_container = page.locator(
            '[data-test="inventory-container"]'
        )

        self.inventory_items = page.locator(
            '[data-test="inventory-item"]'
        )

        self.inventory_item_names = page.locator(
            '[data-test="inventory-item-name"]'
        )

        self.sort_dropdown = page.locator(
            '[data-test="product-sort-container"]'
        )

        self.shopping_cart_link = page.locator(
            '[data-test="shopping-cart-link"]'
        )

    def is_loaded(self) -> bool:
        return self.inventory_container.is_visible()

    def get_product_count(self) -> int:
        return self.inventory_items.count()

    def get_product_names(self) -> list[str]:
        return self.inventory_item_names.all_inner_texts()

    def sort_products(self, option: str):
        self.sort_dropdown.select_option(option)

    def open_product(self, product_name: str):
        self.inventory_item_names.filter(
            has_text=product_name
        ).click()

    def is_product_displayed(self, product_name: str) -> bool:
        return self.inventory_item_names.filter(
            has_text=product_name
        ).is_visible()

    def add_product_to_cart(self, product_name: str):
        product = self.inventory_items.filter(
            has_text=product_name
        )

        product.locator(
            'button[data-test^="add-to-cart"]'
        ).click()

    def remove_product_from_cart(self, product_name: str):
        product = self.inventory_items.filter(
            has_text=product_name
        )

        product.locator(
            'button[data-test^="remove"]'
        ).click()

    def open_cart(self):
        self.shopping_cart_link.click()