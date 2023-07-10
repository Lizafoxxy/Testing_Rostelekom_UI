from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators import Locators

class Decline_Request_Message(BasePage):
    LOCATOR_DECLINE_REQUEST_MESSAGE = (By.TAG_NAME,'h2')

    def get_decline_message_text(self):
        return self.find_element(self.LOCATOR_DECLINE_REQUEST_MESSAGE).text
