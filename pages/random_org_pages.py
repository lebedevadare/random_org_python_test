from pages.base_page import BasePage
from pages.locators.random_org_locators import RandomOrgLocators

class RandomOrgPage(BasePage):
    def set_min_value(self, value: str):
        self.wait_for_load_state("networkidle")
        if not self.element_exists(RandomOrgLocators.MIN_INPUT_WITHOUT_VALUE):
            self.take_screenshot("min_input_not_found.png")
            raise Exception(f"Элемент {RandomOrgLocators.MIN_INPUT_WITHOUT_VALUE} не найден")
        self.fill(RandomOrgLocators.MIN_INPUT_WITHOUT_VALUE, value)

    def set_max_value(self, value: str):
        if not self.element_exists(RandomOrgLocators.MAX_INPUT_WITHOUT_VALUE):
            self.take_screenshot("max_input_not_found.png")
            raise Exception(f"Элемент {RandomOrgLocators.MAX_INPUT_WITHOUT_VALUE} не найден")
        self.fill(RandomOrgLocators.MAX_INPUT_WITHOUT_VALUE, value)

    def click_generate(self):
        if not self.element_exists(RandomOrgLocators.GENERATE_BUTTON):
            self.take_screenshot("generate_button_not_found.png")
            raise Exception(f"Элемент {RandomOrgLocators.GENERATE_BUTTON} не найден")
        self.click(RandomOrgLocators.GENERATE_BUTTON)

    def get_result(self) -> int:
        if not self.element_exists(RandomOrgLocators.RESULT_TEXT):
            self.take_screenshot("result_text_not_found.png")
            raise Exception(f"Элемент {RandomOrgLocators.RESULT_TEXT} не найден")
        return int(self.get_inner_text(RandomOrgLocators.RESULT_TEXT))

    def get_min_value(self) -> int:
        if not self.element_exists(RandomOrgLocators.MIN_INPUT_WITHOUT_VALUE):
            self.take_screenshot("min_input_not_found.png")
            raise Exception(f"Элемент {RandomOrgLocators.MIN_INPUT_WITHOUT_VALUE} не найден")
        return int(self.get_input_value(RandomOrgLocators.MIN_INPUT_WITHOUT_VALUE))

    def get_max_value(self) -> int:
        self.wait_for_load_state("networkidle")
        if not self.element_exists(RandomOrgLocators.MAX_INPUT_WITHOUT_VALUE):
            self.take_screenshot("max_input_not_found.png")
            raise Exception(f"Элемент {RandomOrgLocators.MAX_INPUT_WITHOUT_VALUE} не найден")
        return int(self.get_input_value(RandomOrgLocators.MAX_INPUT_WITHOUT_VALUE))




