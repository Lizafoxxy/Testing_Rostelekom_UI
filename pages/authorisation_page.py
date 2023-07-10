from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators import Locators

class Menu_Tab(BasePage):

    def click_to_tab_telephone(self):
        return self.find_element(Locators.LOCATOR_TAB_TELEPHONE).click()

    def name_tab_telephone(self):
        return self.find_element(Locators.LOCATOR_TAB_TELEPHONE).text

    def find_tab_telephone(self):
        return self.find_element(Locators.LOCATOR_TAB_TELEPHONE)

    def click_to_tab_email(self):
        return self.find_element(Locators.LOCATOR_TAB_EMAIL).click()

    def find_tab_email(self):
        return self.find_element(Locators.LOCATOR_TAB_EMAIL)

    def active_tab_email_color(self):
        return self.get_attirbute(Locators.LOCATOR_TAB_EMAIL, "style")

    def click_to_tab_login(self):
        return self.find_element(Locators.LOCATOR_TAB_LOGIN).click()

    def click_to_tab_personal_account(self):
        return self.find_element(Locators.LOCATOR_TAB_LS).click()

    def name_tab_email(self):
        return self.find_element(Locators.LOCATOR_TAB_EMAIL).text

    def name_tab_login(self):
        return self.find_element(Locators.LOCATOR_TAB_LOGIN).text

    def name_tab_ls(self):
        return self.find_element(Locators.LOCATOR_TAB_LS).text


class Field(BasePage):
    LOCATOR_INPUT_FIELD = (By.XPATH, '//*[@id="username"]')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
    LOCATOR_INPUT_FIELD_PLACEHOLDER = (By.XPATH, "//span[@class = 'rt-input__placeholder']")

    def find_input_field(self):
        return self.find_element(self.LOCATOR_INPUT_FIELD)

    def find_password_field(self):
        return self.find_element(self.LOCATOR_PASSWORD_FIELD)

    def click_to_input_field(self):
        return self.find_element(self.LOCATOR_INPUT_FIELD).click()

    def click_to_password_field(self):
        return self.find_element(self.LOCATOR_PASSWORD_FIELD).click()

    def get_text_from_input_field(self):
        return self.find_element(self.LOCATOR_INPUT_FIELD).text

    def get_text_from_input_field_placeholder(self):
        return self.find_element(self.LOCATOR_INPUT_FIELD_PLACEHOLDER).text

    def send_keys_input_field(self, param=str):
        return self.find_element(self.LOCATOR_INPUT_FIELD).send_keys(param)

    def send_keys_password_field(self, param=str):
        return self.find_element(self.LOCATOR_PASSWORD_FIELD).send_keys(param)


class Button(BasePage):
    LOCATOR_BUTTON_ENTER = (By.XPATH, '//button[@id="kc-login"]')
    LOCATOR_BUTTON_FORGOT_PASSWORD = (By.ID, "forgot_password")
    LOCATOR_BUTTON_REGISTRATION = (By.ID, "kc-register")

    def name_button_enter(self):
        return self.find_element(self.LOCATOR_BUTTON_ENTER).text

    def click_button_enter(self):
        return self.find_element(self.LOCATOR_BUTTON_ENTER).click()

    def click_button_forgot_password(self):
        return self.find_element(self.LOCATOR_BUTTON_FORGOT_PASSWORD).click()

    def click_button_registration(self):
        return self.find_element(self.LOCATOR_BUTTON_REGISTRATION).click()

class Error_Message(BasePage):
    LOCATOR_ERROR_MESSAGE = (By.ID, "form-error-message")

    def find_error_message(self):
        return self.find_element(self.LOCATOR_ERROR_MESSAGE)

    def get_error_message_text(self):
        return self.find_element(self.LOCATOR_ERROR_MESSAGE).text

class Title_on_Authorisation_Page(BasePage):

    def find_page_title(self):
        return self.find_element(Locators.LOCATOR_PAGE_TITLE)

    def get_page_title_name(self):
        return self.find_element(Locators.LOCATOR_PAGE_TITLE).text

class Remember_Me_Check_Box(BasePage):
    LOCATOR_STATUS_CHECKED = (By.XPATH, '//*[@class = "rt-checkbox rt-checkbox--checked"]')
    LOCATOR_STATUS_NOT_CHECKED = (By.XPATH, '//*[@class = "rt-checkbox"]')
    LOCATOR_CHECK_BOX = (By.XPATH, '//*[@class = "rt-checkbox__shape rt-checkbox__shape--circular rt-checkbox__shape--orange"]')

    def find_check_box(self):
        return self.find_element(self.LOCATOR_CHECK_BOX)

    def click_check_box(self):
        return self.find_element(self.LOCATOR_CHECK_BOX).click()

    def status_checked(self):
        return self.find_element(self.LOCATOR_CHECK_BOX)

    def status_not_checked(self):
        return self.find_element(self.LOCATOR_STATUS_NOT_CHECKED)