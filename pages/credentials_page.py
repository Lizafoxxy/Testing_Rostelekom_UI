from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Credentials_Page_Titles(BasePage):
    LOCATOR_CARD_TITLE = (By.XPATH, "//h3[@class = 'card-title']")

    def find_card_titles(self):
        return self.find_elements(self.LOCATOR_CARD_TITLE)

    def list_of_card_titles(self):
        all_titles = self.find_elements(self.LOCATOR_CARD_TITLE)
        return [x.text for x in all_titles]

