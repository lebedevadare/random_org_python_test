import pytest
import logging
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module", params=["chromium", "firefox", "webkit"])
def browser(request):
    with sync_playwright() as p:
        if request.param == "chromium":
            browser = p.chromium.launch(headless=False)
        elif request.param == "firefox":
            browser = p.firefox.launch(headless=False)
        elif request.param == "webkit":
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Неподдерживаемый браузер: {request.param}")
        yield browser
        browser.close()

@pytest.fixture(scope="module")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.random.org/")
    # Установить куки
    # page.context.add_cookies([{"name": "cookie_name", "value": "cookie_value", "domain": ".random.org"}])
    yield page
    context.close()
