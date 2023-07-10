from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Locators:
    LOCATOR_TAB_TELEPHONE = (By.ID, "t-btn-tab-phone")
    LOCATOR_TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_TAB_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_TAB_LS = (By.ID, "t-btn-tab-ls")

    LOCATOR_PAGE_TITLE = (By.XPATH, "//h1[@class = 'card-container__title']")