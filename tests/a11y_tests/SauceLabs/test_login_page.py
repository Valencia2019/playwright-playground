from playwright.sync_api import sync_playwright, expect
from axe_playwright_python.sync_playwright import Axe

axe = Axe()
url = "https://www.saucedemo.com"

# Check acccessibility on the login page
def test_login_page_accesibility():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        results = axe.run(page)
        browser.close()
        if results.violations_count > 0:
            report_file = open("a11y_reports/login.json", "w")
            report_file.write(results.generate_report())
            report_file.close()
            print(f"Found {results.violations_count} violations. Full report at a11y_reports/login.json")
        else:
            print("No accessibility violations found.")