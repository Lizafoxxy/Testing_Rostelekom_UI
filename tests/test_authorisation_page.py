from pages.authorisation_page import*
from pages.credentials_page import*
from pages.decline_request_page import*


# тест RT-001 проверка, что на странице авторизации есть меню авторизации, поля для ввода и кнопка "Войти"
def test_authorisation_page_main_elements(browser, tab_telephone, tab_email, tab_login, tab_ls, input_field, password_field, button_enter):
    tab_telephone.go_to_authorisation_page()
    browser.implicitly_wait(10)

    assert tab_telephone.name_tab_telephone() == "Телефон"
    assert tab_email.name_tab_email() == "Почта"
    assert tab_login.name_tab_login() == "Логин"
    assert tab_ls.name_tab_ls() == "Лицевой счёт"
    assert button_enter.name_button_enter() == "Войти"
    assert input_field.find_input_field() is not None
    assert password_field.find_password_field() is not None


# тест RT-002 При переключении табов меню выбора выбранный способ авторизации становится активным
def test_change_active_tab(browser, tab_telephone, tab_email):
    tab_telephone.go_to_authorisation_page()

    tab_telephone_status_1 = tab_telephone.find_tab_telephone().get_attribute("class")
    tab_email_status_1 = tab_email.find_tab_email().get_attribute("class")
    tab_email.click_to_tab_email()
    browser.implicitly_wait(10)
    tab_email_status_2 = tab_email.find_tab_email().get_attribute("class")
    tab_telephone_status_2 = tab_telephone.find_tab_telephone().get_attribute("class")


    assert tab_telephone_status_1 == "rt-tab rt-tab--small rt-tab--active"
    assert tab_email_status_1 == "rt-tab rt-tab--small"
    assert tab_telephone_status_1 != tab_email_status_1
    assert tab_email_status_2 == tab_telephone_status_1
    #assert '--rt-orange' in tab_email.get_attirbute("style")
    assert tab_telephone_status_2 != tab_telephone_status_1


# тест RT-003 Переключение табов меню выбора способа авторизации меняет текст подсказки в строке для введения информации о способе логирования
def test_input_field_prompt_change_by_tab_switch(browser, tab_telephone, tab_email):
    input_field_placeholder = Field(browser)

    tab_telephone.go_to_authorisation_page()
    browser.implicitly_wait(10)
    tab_telephone.click_to_tab_telephone()
    browser.implicitly_wait(10)
    input_field_prompt_status1 = input_field_placeholder.get_text_from_input_field_placeholder()
    tab_email.click_to_tab_email()
    browser.implicitly_wait(10)
    input_field_prompt_status2 = input_field_placeholder.get_text_from_input_field_placeholder()

    assert input_field_prompt_status1 != input_field_prompt_status2
    assert input_field_prompt_status1 == 'Мобильный телефон'
    assert input_field_prompt_status2 == "Электронная почта"


# тест RT-004 При вводе адреса электронной почты в поле ввода таб "Почта" автоматически становится активным
def test_email_tab_active_by_email_input(browser, tab_telephone, tab_email, input_field, password_field):

    tab_email.go_to_authorisation_page()
    browser.implicitly_wait(10)

    tab_telephone.click_to_tab_telephone()
    browser.implicitly_wait(10)
    tab_email_status1 = tab_email.find_tab_email().get_attribute("class")
    input_field.click_to_input_field()
    browser.implicitly_wait(10)
    input_field.send_keys_input_field("testirov80@mail.ru")
    browser.implicitly_wait(10)
    password_field.click_to_password_field()
    browser.implicitly_wait(10)
    tab_email_status2 = tab_email.find_tab_email().get_attribute("class")

    assert tab_email_status1 == "rt-tab rt-tab--small"
    assert tab_email_status2 == "rt-tab rt-tab--small rt-tab--active"

# тест RT-005 Введение некорректных данных авторизации
def test_incorrect_password_login(browser, tab_email, input_field, password_field, button_enter):
    error_message = Error_Message(browser)

    tab_email.go_to_authorisation_page()
    browser.implicitly_wait(10)

    tab_email.click_to_tab_email()
    browser.implicitly_wait(10)
    input_field.click_to_input_field()
    input_field.send_keys_input_field("testirov80@mail.ru")
    password_field.click_to_password_field
    password_field.send_keys_password_field("577")
    browser.implicitly_wait(5)
    button_enter.click_button_enter()
    browser.implicitly_wait(5)

    assert error_message.find_error_message() is not None
    assert error_message.get_error_message_text() == "Неверный логин или пароль"

#тест RT-006 Чек-бокс "Запомнить меня" по умолчанию активен
def test_check_box(browser):
    check_box = Remember_Me_Check_Box(browser)
    status_checked = Remember_Me_Check_Box(browser)

    check_box.go_to_authorisation_page()
    browser.implicitly_wait(10)

    assert status_checked.status_checked()

#тест RT-007 Работа чекбокса "Запомнить меня", активный при открытии страницы, неактивный после клика
def test_check_box_change(browser):
    check_box = Remember_Me_Check_Box(browser)
    status_not_checked = Remember_Me_Check_Box(browser)

    check_box.go_to_authorisation_page()
    browser.implicitly_wait(10)

    check_box.find_check_box()
    check_box.click_check_box()
    browser.implicitly_wait(10)

    assert status_not_checked.status_not_checked()

#тест RT-00X_0 Проверка на принятие скрипта полем для ввода способа авторизации (XSS-инъекция)
def test_script_in_input_field(browser, tab_login, input_field, password_field, button_enter):
    check_box = Remember_Me_Check_Box(browser)
    decline_request_message = Decline_Request_Message(browser)
    input_field.go_to_authorisation_page()

    tab_login.click_to_tab_login()
    browser.implicitly_wait(10)
    input_field.click_to_input_field()
    browser.implicitly_wait(10)
    input_field.send_keys_input_field('<script>alert("Проверка!")</script>')
    password_field.click_to_password_field()
    browser.implicitly_wait(10)
    password_field.send_keys_password_field("abc123")
    browser.implicitly_wait(10)
    check_box.click_check_box()
    browser.implicitly_wait(10)
    button_enter.click_button_enter()
    browser.implicitly_wait(10)

    assert "Ваш запрос был отклонен из соображений безопасности" in decline_request_message.get_decline_message_text()

# тест RT-00X-1 Введение корректных данных авторизации
def test_correct_password_login(browser, tab_email, input_field, password_field, button_enter):
    page_titles = Credentials_Page_Titles(browser)

    tab_email.go_to_authorisation_page()

    tab_email.click_to_tab_email()
    browser.implicitly_wait(10)
    input_field.click_to_input_field()
    input_field.send_keys_input_field("testirov80@mail.ru")
    browser.implicitly_wait(10)
    password_field.click_to_password_field()
    password_field.send_keys_password_field("my-Password")
    browser.implicitly_wait(10)
    button_enter.click_button_enter()
    browser.implicitly_wait(5)
    titles_elements = page_titles.list_of_card_titles()

    assert "Учетная запись" and "Личные кабинеты" in titles_elements