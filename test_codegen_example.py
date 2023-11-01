from playwright.sync_api import Playwright, sync_playwright, expect

# This test was made using the codegen feature 
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/")
    page.get_by_text("This is just a demo of TodoMVC for testing, not the real TodoMVC app.").click()
    page.get_by_text("This is just a demo of TodoMVC for testing, not the real TodoMVC app.").click(button="right")
    expect(page.get_by_text("This is just a demo of TodoMVC for testing, not the real TodoMVC app.")).to_be_visible()
    page.get_by_role("heading", name="todos").click()
    expect(page.get_by_placeholder("What needs to be done?")).to_be_visible()
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Here's some text")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_test_id("todo-title").click()
    page.get_by_text("All Active Completed").click()
    page.get_by_role("link", name="Active").click()
    page.get_by_role("link", name="Completed").click()
    page.get_by_role("link", name="All").click()
    page.get_by_test_id("todo-title").click()
    page.get_by_label("Toggle Todo").check()
    page.get_by_role("link", name="Completed").click()
    page.get_by_role("link", name="Active").click()
    page.get_by_role("link", name="All").click()
    page.get_by_role("button", name="Clear completed").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
