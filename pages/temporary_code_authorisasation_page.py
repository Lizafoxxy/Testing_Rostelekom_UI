from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Contact_Input_Field(BasePage):
    LOCATOR_INPUT_FIELD = (By.XPATH, '//*[@id="address"]')

    def find_input_field(self):
        return self.find_element(self.LOCATOR_INPUT_FIELD)

    def click_to_input_field(self):
        return self.find_element(self.LOCATOR_INPUT_FIELD).click()

    def send_keys_input_field(self, param=str):
        return self.find_element(self.LOCATOR_INPUT_FIELD).send_keys(param)

class Button_Get_Code(BasePage):
    LOCATOR_BUTTON_GET_CODE = (By.XPATH, "//button[@id = 'otp_get_code']")

    def name_button_get_code(self):
        return self.find_element(self.LOCATOR_BUTTON_GET_CODE).text

    def click_button_get_code(self):
        return self.find_element(self.LOCATOR_BUTTON_GET_CODE).click()

class Page_Title(BasePage):
    LOCATOR_PAGE_TITLE = (By.XPATH, "//h1[@class = 'card-container__title']")

    def find_page_title(self):
        return self.find_element(self.LOCATOR_PAGE_TITLE)

    def get_page_title_name(self):
        return self.find_element(self.LOCATOR_PAGE_TITLE).text

class Error_Message(BasePage):
    LOCATOR_ERROR_MESSAGE = (By.XPATH, "//span[@class = 'rt-input-container__meta rt-input-container__meta--error']")

    def find_error_message(self):
        return self.find_element(self.LOCATOR_ERROR_MESSAGE)

    def get_error_message_text(self):
        return self.find_element(self.LOCATOR_ERROR_MESSAGE).text