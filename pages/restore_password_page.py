from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators import Locators

class Menu_Tab_on_Restore_Page(BasePage):

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


class Field_on_Restore_Page(BasePage):
    LOCATOR_INPUT_FIELD = (By.XPATH, '//*[@id="username"]')
    LOCATOR_CAPTCHA_FIELD = (By.XPATH, '//input[@id="captcha"]')
    LOCATOR_INPUT_FIELD_PLACEHOLDER = (By.XPATH, '//input[@id = "username"]/..//span[@class = "rt-input__placeholder"]')
    LOCATOR_CAPTCHA_FIELD_PlACEHOLDER = (By.XPATH, '//input[@id = "captcha"]/..//span[@class = "rt-input__placeholder"]')

    def find_input_field(self):
        return self.find_element(self.LOCATOR_INPUT_FIELD)

    def click_to_input_field(self):
        return self.find_element(self.LOCATOR_INPUT_FIELD).click()

    def get_text_from_input_field(self):
        return self.find_element(self.LOCATOR_INPUT_FIELD).text

    def get_text_from_input_field_placeholder(self):
        return self.find_element(self.LOCATOR_INPUT_FIELD_PLACEHOLDER).text

    def find_captcha_field(self):
        return self.find_element(self.LOCATOR_CAPTCHA_FIELD)

    def click_to_captcha_field(self):
        return self.find_element(self.LOCATOR_CAPTCHA_FIELD).click()

    def send_keys_input_field(self, param=str):
        return self.find_element(self.LOCATOR_INPUT_FIELD).send_keys(param)

    def get_text_from_captcha_field_placeholder(self):
        return self.find_element(self.LOCATOR_CAPTCHA_FIELD_PlACEHOLDER).text


class Buttons_on_Restore_Page(BasePage):
    LOCATOR_BUTTON_CONTINUE = (By.XPATH, '//button[@id="reset"]')
    LOCATOR_BUTTON_RESET_BACK = (By.XPATH, '//button[@id="reset-back"]')

    def name_button_continue(self):
        return self.find_element(self.LOCATOR_BUTTON_CONTINUE).text

    def click_button_continue(self):
        return self.find_element(self.LOCATOR_BUTTON_CONTINUE).click()

    def name_button_reset_back(self):
        return self.find_element(self.LOCATOR_BUTTON_RESET_BACK).text

    def click_button_reset_back(self):
        return self.find_element(self.LOCATOR_BUTTON_RESET_BACK).click()

class Title_on_Restore_Page(BasePage):

    def find_page_title(self):
        return self.find_element(Locators.LOCATOR_PAGE_TITLE)

    def get_page_title_name(self):
        return self.find_element(Locators.LOCATOR_PAGE_TITLE).text

class Captcha_on_Restore_Page(BasePage):
    LOCATOR_CAPTCHA_ON_RESTORE_PAGE = (By.XPATH, '//img[@class="rt-captcha__image"]')

    def find_captcha(self):
        return self.find_element(self.LOCATOR_CAPTCHA_ON_RESTORE_PAGE)
