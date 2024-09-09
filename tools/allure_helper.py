import allure

class AllureHelper:
    @staticmethod
    def attach_screenshot(page, name="Screenshot"):
        """
        Прикрепить скриншот к отчету Allure.

        :param page: Экземпляр страницы Playwright.
        :param name: Имя скриншота в отчете.
        """
        screenshot = page.screenshot()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)