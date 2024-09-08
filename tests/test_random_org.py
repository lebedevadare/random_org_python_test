import pytest
import logging

logger = logging.getLogger()

@pytest.mark.parametrize("browser", ["chromium", "firefox", "webkit"], indirect=True)
def test_generate_number_1_to_100(random_org_page):
    try:
        random_org_page.set_min_value('1')
        random_org_page.set_max_value('100')
        random_org_page.click_generate()
        result = random_org_page.get_result()
        logger.debug(f"Сгенерировано число: {result}")
        assert 1 <= result <= 100
    except Exception as e:
        random_org_page.take_screenshot("screenshot/test_generate_number_1_to_100.png")
        raise e

@pytest.mark.parametrize("browser", ["chromium", "firefox", "webkit"], indirect=True)
def test_generate_number_1_to_1(random_org_page):
    try:
        random_org_page.set_min_value('1')
        random_org_page.set_max_value('1')
        random_org_page.click_generate()
        result = random_org_page.get_result()
        logger.debug(f"Сгенерировано число: {result}")
        assert result == 1
    except Exception as e:
        random_org_page.take_screenshot("screenshot/test_generate_number_1_to_1.png")
        raise e

@pytest.mark.parametrize("browser", ["chromium", "firefox", "webkit"], indirect=True)
def test_generate_number_23_to_13(random_org_page):
    try:
        random_org_page.set_min_value('23')
        random_org_page.set_max_value('13')
        random_org_page.click_generate()
        min_value = random_org_page.get_min_value()
        max_value = random_org_page.get_max_value()
        result = random_org_page.get_result()
        logger.debug(f"Min value: {min_value}, Max value: {max_value}, Сгенерировано число: {result}")
        assert min_value == 23
        assert max_value == 24
        assert 23 <= result <= 24
    except Exception as e:
        random_org_page.take_screenshot("screenshot/test_generate_number_23_to_13.png")
        raise e
