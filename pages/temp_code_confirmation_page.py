from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Confirmation_Page_Title(BasePage):
    LOCATOR_PAGE_TITLE = (By.XPATH, "//h1[@class = 'card-container__title']")

    def find_page_title(self):
        return self.find_element(self.LOCATOR_PAGE_TITLE)

    def get_page_title_name(self):
        return self.find_element(self.LOCATOR_PAGE_TITLE).text

class Contact_Details(BasePage):
    LOCATOR_CONTACT_DETAILS = (By.XPATH, "//*[@class = 'otp-code-form-container__desc']")

    def contact_details_text(self):
        return self.find_element(self.LOCATOR_CONTACT_DETAILS).text


class Change_Contact_Details_Button(BasePage):
    LOCATOR_CHANGE_CONTACT_DETAILS_BUTTON = (By.XPATH, "//button[@class = 'rt-link rt-link--orange otp-code-form__back-btn']")

    def find_button(self):
        return self.find_element(self.LOCATOR_CHANGE_CONTACT_DETAILS_BUTTON)

    def get_change_contact_details_button_name(self):
        return self.find_element(self.LOCATOR_CHANGE_CONTACT_DETAILS_BUTTON).text

class Code_Input_Fields(BasePage):
    LOCATOR_CODE_INPUT_FIELDS = (By.XPATH, "//*[@class = 'rt-input__input sdi-container__input code-input__input rt-input__input--rounded rt-input__input--purple']")

    def count_code_input_fields(self):
        all_fields = self.find_elements(self.LOCATOR_CODE_INPUT_FIELDS)
        return len(all_fields)

class Message_Count_Down(BasePage):
    LOCATOR_MESSAGE_COUNT_DOWN = (By.XPATH, "//*[@class = 'code-input-container__timeout']")

    def find_message(self):
        return self.find_element(self.LOCATOR_MESSAGE_COUNT_DOWN)

    def message_text(self):
        return self.find_element(self.LOCATOR_MESSAGE_COUNT_DOWN).text