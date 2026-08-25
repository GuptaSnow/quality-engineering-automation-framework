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

    def is_loaded(self) -> bool:
        return self.inventory_container.is_visible()

    def get_product_count(self) -> int:
        return self.inventory_items.count()