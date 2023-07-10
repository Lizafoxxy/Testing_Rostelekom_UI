import pytest
from selenium import webdriver
from pages.authorisation_page import Menu_Tab, Field, Button
from pages.temporary_code_authorisasation_page import Contact_Input_Field, Button_Get_Code



@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def open_registration_page(browser, button_registration):
    button_registration.go_to_authorisation_page()
    browser.implicitly_wait(15)
    button_registration.click_button_registration()
    browser.implicitly_wait(15)


@pytest.fixture(scope="function")
def open_restore_password_page(browser, button_forgot_password):
    button_forgot_password.go_to_authorisation_page()
    browser.implicitly_wait(15)
    button_forgot_password.click_button_forgot_password()
    browser.implicitly_wait(15)

# фикстуры для инициализации класса и создания экземпляра класса, чтобы не делать это в тестах

@pytest.fixture(scope="session")
def tab_telephone(browser):
    tab_telephone = Menu_Tab(browser)
    return tab_telephone

@pytest.fixture(scope="session")
def tab_email(browser):
    tab_email = Menu_Tab(browser)
    return tab_email

@pytest.fixture(scope="session")
def tab_login(browser):
    tab_login = Menu_Tab(browser)
    return tab_login

@pytest.fixture(scope="session")
def tab_ls(browser):
    tab_ls = Menu_Tab(browser)
    return tab_ls

@pytest.fixture(scope="session")
def input_field(browser):
    input_field = Field(browser)
    return input_field

@pytest.fixture(scope="session")
def password_field(browser):
    password_field = Field(browser)
    return password_field

@pytest.fixture(scope="session")
def button_enter(browser):
    button_enter = Button(browser)
    return button_enter

@pytest.fixture(scope="session")
def button_forgot_password(browser):
    button_forgot_password = Button(browser)
    return button_forgot_password

@pytest.fixture(scope="session")
def button_registration(browser):
    button_registration = Button(browser)
    return button_registration

@pytest.fixture(scope="session")
def contact_input_field(browser):
    contact_input_field = Contact_Input_Field(browser)
    return contact_input_field

@pytest.fixture(scope="session")
def button_get_code(browser):
    button_get_code = Button_Get_Code(browser)
    return button_get_code

