import re
from playwright.sync_api import expect, sync_playwright

# define the url that will be used for tests in this spec file
url = "https://www.saucedemo.com"


def test_log_in():
   with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        expect(page).to_have_title("Swag Labs")
        username = page.locator("#user-name")
        password = page.locator("#password")
        loginBtn = page.locator("#login-button")
        expect(username).to_be_visible()
        username.fill('standard_user')
        password.fill('secret_sauce')
        loginBtn.click()
        page.wait_for_url("**/inventory.html")
        expect(page).to_have_url(re.compile('.*/inventory.html'))
        return