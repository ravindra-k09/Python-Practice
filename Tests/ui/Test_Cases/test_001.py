import re
from playwright.sync_api import Page, expect
from Tests.ui.pages.login_page import LoginPage
from Tests.ui.pages.inventory_page import InventoryPage
from Tests.ui.pages.check_out import CheckoutPage


def test_example(page):
   
    page.goto("https://www.saucedemo.com/")
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)

    login.login("standard_user", "secret_sauce")
    inventory.add_item_to_cart()
    inventory.go_to_cart()
    checkout.start_checkout()
    checkout.fill_details("Ravindra", "K", "12345678")
    checkout.complete_checkout()

def test_example2(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    expect(page.get_by_text("Swag Labs")).to_be_visible()
    expect(page.locator("#root")).to_contain_text("Swag Labs")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("gfshhjabvg")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"username\"]").fill("gfshhjabvgs")
    page.locator("[data-test=\"password\"]").fill("hsjkhdgsjska")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username and password do not match any user in this service")

