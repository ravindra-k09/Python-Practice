
class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_item_to_cart(self):
        self.page.get_by_text("$29.99Add to cart").click()

    def go_to_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()
