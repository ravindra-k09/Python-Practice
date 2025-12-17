
class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.locator('[data-test="username"]').click()
        self.page.locator('[data-test="username"]').fill(username)
        self.page.locator('[data-test="password"]').click()
        self.page.locator('[data-test="password"]').fill(password)
        self.page.locator('[data-test="login-button"]').click()
