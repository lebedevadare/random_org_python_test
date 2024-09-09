import pytest
import logging
import logging.config
from pathlib import Path
from playwright.sync_api import sync_playwright
from pages.random_org_pages import RandomOrgPage

logging.config.fileConfig('settings/logging. conf')
logger = logging.getLogger()

@pytest.fixture(scope="module", params=["chromium", "firefox", "webkit"])
def browser(request):
    """
    Фикстура для запуска браузера. Поддерживает Chromium, Firefox и WebKit
    Логирует запуск и закрытие браузера
    """
    with sync_playwright() as p:
        logger.info(f"Запуск браузера: {request.param}")
        if request.param == "chromium":
            browser = p.chromium.launch(headless=False)
        elif request.param == "firefox":
            browser = p.firefox.launch(headless=False)
        elif request.param == "webkit":
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Неподдерживаемый браузер: {request.param}")
        yield browser
        logger.info(f"Закрытие браузера: {request.param}")
        browser.close()

@pytest.fixture(scope="module")
def page(browser):
    """
    Фикстура для создания новой страницы в контексте браузера
    Логирует открытие страницы
    """
    context = browser.new_context()
    page = context.new_page()
    logger.info("Открытие страницы https://www.random.org/widgets/integers/iframe")
    page.goto("https://www.random.org/widgets/integers/iframe")
    # Ожидание полной загрузки страницы
    page.wait_for_load_state("networkidle")
    # Установить куки
    # page.context.add_cookies([{"name": "cookie_name", "value": "cookie_value", "domain": ".random.org"}])
    yield page
    context.close()

@pytest.fixture(scope="module")
def random_org_page(page):
    """
    Фикстура для создания объекта страницы
    """
    return RandomOrgPage(page)

@pytest.fixture(scope="session", autouse=True)
def setup_screenshot_directory():
    """
    Фикстура для создания директории screenshot перед запуском тестов
    """
    Path("screenshot").mkdir(exist_ok=True)