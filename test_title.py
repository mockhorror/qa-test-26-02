import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.parametrize("browser", ["chromium", "firefox"])
def test_playwright_title(browser):
    with sync_playwright() as p:
        browser_instance = getattr(p, browser).launch(headless=True)
        page = browser_instance.new_page()
        page.goto("https://playwright.dev/")
        expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
        browser_instance.close()