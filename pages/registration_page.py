from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators import Locators

class Title_on_Registration_Page(BasePage):
    def find_page_title(self):
        return self.find_element(Locators.LOCATOR_PAGE_TITLE)

    def get_page_title_name(self):
        return self.find_element(Locators.LOCATOR_PAGE_TITLE).text

class Section_Headers(BasePage):
    LOCATOR_SECTION_HEADERS = (By.XPATH, '//p[@class = "register-form__desc"]')

    def find_section_headers(self):
        return self.find_elements(self.LOCATOR_SECTION_HEADERS)

    def list_of_section_headers_titles(self):
        all_titles = self.find_elements(self.LOCATOR_SECTION_HEADERS)
        return [x.text for x in all_titles]

class Input_Field_on_Registration_Page(BasePage):
    LOCATOR_FIELD_NAME = (By.XPATH, '//input[@name = "firstName"]')
    LOCATOR_FIELD_SURNAME = (By.XPATH, '//input[@name = "lastName"]')
    LOCATOR_FIELD_ADDRESS = (By.ID, "address")
    LOCATOR_FIELD_SET_PASSWORD = (By.ID, "password")
    LOCATOR_FIELD_PASSWORD_CONFIRM = (By.ID, "password-confirm")
    LOCATOR_FIELD_REGION = (By.XPATH, '//span[@class = "rt-input__placeholder rt-input__placeholder--top"]')

    def find_field_name(self):
        return self.find_element(self.LOCATOR_FIELD_NAME)

    def click_to_field_name(self):
        return self.find_element(self.LOCATOR_FIELD_NAME).click()

    def send_keys_to_field_name(self, param=str):
        return self.find_element(self.LOCATOR_FIELD_NAME).send_keys(param)

    def clear_field_name(self):
        return self.find_element(self.LOCATOR_FIELD_NAME).clear()

    def find_field_surname(self):
        return self.find_element(self.LOCATOR_FIELD_SURNAME)

    def click_to_field_surname(self):
        return self.find_element(self.LOCATOR_FIELD_SURNAME).click()

    def find_field_address(self):
        return self.find_element(self.LOCATOR_FIELD_ADDRESS)

    def find_field_region(self):
        return self.find_element(self.LOCATOR_FIELD_REGION)

    def get_header_field_region(self):
        return self.find_element(self.LOCATOR_FIELD_REGION).text

    def find_field_password(self):
        return self.find_element(self.LOCATOR_FIELD_SET_PASSWORD)

    def find_field_confirm_password(self):
        return self.find_element(self.LOCATOR_FIELD_PASSWORD_CONFIRM)

class Logo(BasePage):
    LOCATOR_LOGO = (By.XPATH, '//*[@class = "rt-logo main-header__logo"]')

    def find_logo_on_page(self):
        return self.find_element(self.LOCATOR_LOGO)

class Error_Message(BasePage):
    LOCATOR_ERROR_MESSAGE = (By.XPATH, '//*[@class = "rt-input-container__meta rt-input-container__meta--error"]')

    def find_error_messages(self):
        return self.find_elements(self.LOCATOR_ERROR_MESSAGE)

    def get_list_of_error_messages(self):
        messages_list = self.find_elements(self.LOCATOR_ERROR_MESSAGE)
        return [x.text for x in messages_list]

    def invisibility_of_error_message(self):
        return self.invisibility_of_element(self.LOCATOR_ERROR_MESSAGE)

