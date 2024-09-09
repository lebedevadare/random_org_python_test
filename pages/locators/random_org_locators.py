class RandomOrgLocators:
    MIN_INPUT_WITHOUT_VALUE = '//label[contains(text(), "Min:")]/following-sibling::input'
    MAX_INPUT_WITHOUT_VALUE = '//label[contains(text(), "Max:")]/following-sibling::input'
    GENERATE_BUTTON = '//input[@value="Generate"]'
    RESULT_TEXT = '//label[contains(text(), "Result:")]/following-sibling::span/center/span[@style="font-size:100%;font-weight:bold;"]'
