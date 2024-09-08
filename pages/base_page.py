from playwright.sync_api import Page
import logging


logger = logging.getLogger()

class BasePage:
    def __init__(self, page: Page):
        """
        Инициализация базовой страницы.

        :param page: Экземпляр страницы Playwright.
        """
        self.page = page

    def wait_for_selector(self, locator: str, state: str = "visible", timeout: int = 30000):
        """
        Ожидание появления элемента на странице.

        :param locator: Локатор элемента.
        :param state: Состояние, в котором должен находиться элемент (по умолчанию "visible").
        :param timeout: Время ожидания в миллисекундах (по умолчанию 30000).
        """
        logger.info(f"Ожидание элемента: {locator}")
        self.page.wait_for_selector(locator, state=state, timeout=timeout)
        logger.info(f"Элемент найден: {locator}")

    def fill(self, locator: str, value: str):
        """
        Заполнение поля ввода.

        :param locator: Локатор элемента.
        :param value: Значение для заполнения.
         """
        self.wait_for_selector(locator)
        self.page.fill(locator, value)

    def click(self, locator: str):
        """
        Клик по элементу.

        :param locator: Локатор элемента.
        """
        self.wait_for_selector(locator)
        self.page.click(locator)

    def get_inner_text(self, locator: str) -> str:
        """
        Получение внутреннего текста элемента.

        :param locator: Локатор элемента.
        :return: Внутренний текст элемента.
        """
        self.wait_for_selector(locator)
        return self.page.inner_text(locator)

    def get_input_value(self, locator: str) -> str:
        """
        Получение значения поля ввода.

        :param locator: Локатор элемента.
        :return: Значение поля ввода.
        """
        self.wait_for_selector(locator)
        return self.page.input_value(locator)

    def element_exists(self, locator: str) -> bool:
        """
        Проверка существования элемента на странице.

        :param locator: Локатор элемента.
        :return: True, если элемент существует, иначе False.
        """
        try:
            self.page.wait_for_selector(locator, state="attached", timeout=10000)
            return True
        except:
            return False

    def take_screenshot(self, path: str):
        """
        Сделать скриншот страницы.

        :param path: Путь для сохранения скриншота.
        """
        self.page.screenshot(path=path)

    def wait_for_load_state(self, state: str = "load"):
        """
        Ожидание состояния загрузки страницы.

        :param state: Состояние загрузки (по умолчанию "load").
        """
        logger.info(f"Ожидание состояния загрузки страницы: {state}")
        self.page.wait_for_load_state(state)
