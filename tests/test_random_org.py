import pytest
import logging
import allure
from tools.allure_helper import AllureHelper

logger = logging.getLogger()

@pytest.mark.parametrize("browser", ["chromium", "firefox", "webkit"], indirect=True)
def test_generate_number_1_to_100(random_org_page):
    try:
        with allure.step("Установить минимальное значение 1"):
            random_org_page.set_min_value('1')
        with allure.step("Установить максимальное значение 100"):
            random_org_page.set_max_value('100')
        with allure.step("Нажать кнопку 'Generate'"):
            random_org_page.click_generate()
        with allure.step("Получить результат"):
            result = random_org_page.get_result()
            logger.debug(f"Сгенерировано число: {result}")
        with allure.step("Проверить, что результат в диапазоне от 1 до 100"):
            assert 1 <= result <= 100
    except Exception as e:
        random_org_page.take_screenshot("screenshot/test_generate_number_1_to_100.png")
        AllureHelper.attach_screenshot(random_org_page.page, "test_generate_number_1_to_100")
        raise e

@pytest.mark.parametrize("browser", ["chromium", "firefox", "webkit"], indirect=True)
def test_generate_number_1_to_1(random_org_page):
    try:
        with allure.step("Установить минимальное значение 1"):
            random_org_page.set_min_value('1')
        with allure.step("Установить максимальное значение 1"):
            random_org_page.set_max_value('1')
        with allure.step("Нажать кнопку 'Generate'"):
            random_org_page.click_generate()
        with allure.step("Получить результат"):
            result = random_org_page.get_result()
            logger.debug(f"Сгенерировано число: {result}")
        with allure.step("Проверить, что результат равен 1"):
            assert result == 1
    except Exception as e:
        random_org_page.take_screenshot("screenshot/test_generate_number_1_to_1.png")
        AllureHelper.attach_screenshot(random_org_page.page, "test_generate_number_1_to_1")
        raise e

@pytest.mark.parametrize("browser", ["chromium", "firefox", "webkit"], indirect=True)
def test_generate_number_23_to_13(random_org_page):
    try:
        with allure.step("Установить минимальное значение 23"):
            random_org_page.set_min_value('23')
        with allure.step("Установить максимальное значение 13"):
            random_org_page.set_max_value('13')
        with allure.step("Нажать кнопку 'Generate'"):
            random_org_page.click_generate()
        with allure.step("Получить минимальное значение"):
            min_value = random_org_page.get_min_value()
        with allure.step("Получить максимальное значение"):
            max_value = random_org_page.get_max_value()
        with allure.step("Получить результат"):
            result = random_org_page.get_result()
            logger.debug(f"Min value: {min_value}, Max value: {max_value}, Сгенерировано число: {result}")
        with allure.step("Проверить, что минимальное значение равно 23"):
            assert min_value == 23
        with allure.step("Проверить, что максимальное значение равно 24"):
            assert max_value == 24
        with allure.step("Проверить, что результат в диапазоне от 23 до 24"):
            assert 23 <= result <= 24
    except Exception as e:
        random_org_page.take_screenshot("screenshot/test_generate_number_23_to_13.png")
        AllureHelper.attach_screenshot(random_org_page.page, "test_generate_number_23_to_13")
        raise e
