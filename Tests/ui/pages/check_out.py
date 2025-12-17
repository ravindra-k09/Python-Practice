class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def start_checkout(self):
        self.page.locator('[data-test="checkout"]').click()

    def fill_details(self, first_name, last_name, postal_code):
        self.page.locator('[data-test="firstName"]').click()
        self.page.locator('[data-test="firstName"]').fill(first_name)
        self.page.locator('[data-test="lastName"]').click()
        self.page.locator('[data-test="lastName"]').fill(last_name)
        self.page.locator('[data-test="postalCode"]').click()
        self.page.locator('[data-test="postalCode"]').fill(postal_code)
        self.page.locator('[data-test="continue"]').click()

    def complete_checkout(self):
        self.page.locator('[data-test="finish"]').click()
        self.page.locator('[data-test="back-to-products"]').click()