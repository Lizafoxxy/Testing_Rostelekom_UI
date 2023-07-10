from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url1 = "https://b2c.passport.rt.ru/"
        self.base_url2 = "https://lk.rt.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def get_element_name(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator)).text

    def get_elements_names(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator)).text

    def invisibility_of_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def go_to_authorisation_page(self):
        return self.driver.get(self.base_url1)

    def go_to_temp_code_authorisation_page(self):
        return self.driver.get(self.base_url2)

    #def get_attirbute(self, locator, attribute=str, time=10):
    #    return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator)).get_attribute(attribute)