import re, pytest
from playwright.sync_api import expect, Page

# define the url that will be used for tests in this spec file
url = "https://www.saucedemo.com"
pw = "secret_sauce"

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
   print("before the test runs, open page and set variables")
   page.goto(url)
   yield page
    
   print("after the test runs, log out")
   page.close()

# Verify one can login with any user that is not locked out
@pytest.mark.parametrize("login_name", ["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"])
def test_log_in(login_name, before_each_after_each):
   page = before_each_after_each
   expect(page).to_have_title("Swag Labs")
   username = page.locator("#user-name")
   password = page.locator("#password")
   loginBtn = page.locator("#login-button")
   expect(username).to_be_visible()
   username.fill(login_name)
   password.fill(pw)
   loginBtn.click()
   page.wait_for_url("**/inventory.html")
   expect(page).to_have_url(re.compile('.*/inventory.html'))
   return

# Verify locked out user can not log in
def test_locked_out_user(before_each_after_each):
   page = before_each_after_each
   expect(page).to_have_title("Swag Labs")
   username = page.locator("#user-name")
   password = page.locator("#password")
   loginBtn = page.locator("#login-button")
   expect(username).to_be_visible()
   username.fill('locked_out_user')
   password.fill(pw)
   loginBtn.click()
   expect(page.locator('data-test=error')).to_be_visible()
   expect(page.locator('data-test=error')).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
   expect(page).not_to_have_url(re.compile('.*/inventory.html'))
   return
