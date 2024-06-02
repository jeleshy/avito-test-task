import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # Different browsers can be chosen. Tests work for each of them
        browser = p.chromium.launch()
        #browser = p.firefox.launch()
        #browser = p.webkit.launch(headless = False)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser):
    with browser as b:
        page = b.new_page()
        yield page
        page.close()


