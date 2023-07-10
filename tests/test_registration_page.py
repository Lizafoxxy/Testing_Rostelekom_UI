import time

import pytest

from pages.registration_page import*
from pages.authorisation_page import Button

# тест RT-013 Переход на страницу регистрации со страницы авторизации
def test_registration_page_redirect_from_authorisation_page(browser, button_registration):
    registration_page_title = Title_on_Registration_Page(browser)

#в следующих тестах открытие страницы регистрации осуществляется через фикстуру
    button_registration.go_to_authorisation_page()
    browser.implicitly_wait(10)
    button_registration.click_button_registration()
    browser.implicitly_wait(10)

    assert "Регистрация" in registration_page_title.get_page_title_name()

#тест RT-014 На странице "Регистрация" есть раздел "Личные данные" и присутсвуют поля для ввода информации и поле для выбора региона
def test_registration_page_personal_data_section_present(browser, open_registration_page):
    personal_data_section_title = Section_Headers(browser)
    name_input_field = Input_Field_on_Registration_Page(browser)
    surname_input_field = Input_Field_on_Registration_Page(browser)
    region_selection_field = Input_Field_on_Registration_Page(browser)

    assert "Личные данные" in personal_data_section_title.list_of_section_headers_titles()
    assert name_input_field.find_field_name() is not None
    assert surname_input_field.find_field_surname() is not None
    assert region_selection_field.get_header_field_region() == "Регион"

#тест RT-015 На странице "Регистрация" есть раздел "Данные для входа" и присутсвуют поля для ввода информации
def test_registration_page_login_data_section_present(browser, open_registration_page):
    login_data_section_title = Section_Headers(browser)
    address_input_field = Input_Field_on_Registration_Page(browser)
    password_input_field = Input_Field_on_Registration_Page(browser)
    password_confirm_input_field = Input_Field_on_Registration_Page(browser)

    assert "Данные для входа" in login_data_section_title.list_of_section_headers_titles()
    assert address_input_field.find_field_address() is not None
    assert password_input_field.find_field_password() is not None
    assert password_confirm_input_field.find_field_confirm_password() is not None

#тест RT-016 На странице "Регистрация" присутсвует логотип
def test_logo_present_on_registration_page(browser, open_registration_page):
    logo = Logo(browser)

    assert logo.find_logo_on_page() is not None

#тест RT-017 Проверка, что при открытии страницы "Регистрации" на ней нет сообщений об ошибке
def test_no_error_message_initially_on_registration_page(browser, open_registration_page):
    error_message = Error_Message(browser)

    assert error_message.invisibility_of_error_message()

#тест RT-018 Проверка поля "Имя"одним символом кирилицей, появляется сообщение об ошибке
def test_name_input_field_one_cyrilic_symbol(browser, open_registration_page):
    name_input_field = Input_Field_on_Registration_Page(browser)
    surname_input_field = Input_Field_on_Registration_Page(browser)
    error_message = Error_Message(browser)

    name_input_field.click_to_field_name()
    browser.implicitly_wait(10)
    name_input_field.send_keys_to_field_name("И")
    browser.implicitly_wait(10)
    surname_input_field.click_to_field_surname()
    browser.implicitly_wait(10)

    assert len(error_message.get_list_of_error_messages()) == 1
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error_message.get_list_of_error_messages()

#тест RT-019 Проверка поля "Имя" двумя символами кирилицей, не появляется сообщение об ошибке
def test_name_input_field_2_cyrilic_symbols(browser, open_registration_page):
    name_input_field = Input_Field_on_Registration_Page(browser)
    surname_input_field = Input_Field_on_Registration_Page(browser)
    error_message = Error_Message(browser)

    name_input_field.click_to_field_name()
    browser.implicitly_wait(10)
    name_input_field.send_keys_to_field_name("Ия")
    browser.implicitly_wait(10)
    surname_input_field.click_to_field_surname()
    browser.implicitly_wait(10)

    assert error_message.invisibility_of_error_message()

#тест RT-020 Проверка поля "Имя" 30 символами кирилицей, не появляется сообщение об ошибке
def test_name_input_field_30_cyrilic_symbols(browser, open_registration_page):
    name_input_field = Input_Field_on_Registration_Page(browser)
    surname_input_field = Input_Field_on_Registration_Page(browser)
    error_message = Error_Message(browser)

    name_input_field.click_to_field_name()
    browser.implicitly_wait(10)
    name_input_field.send_keys_to_field_name("Абвгдабвгдабвгдабвгдабвгдабвгд")
    browser.implicitly_wait(10)
    surname_input_field.click_to_field_surname()
    browser.implicitly_wait(10)

    assert error_message.invisibility_of_error_message()

#тест RT-021 Проверка поля "Имя" 31 символами кирилицей, появляется  сообщение об ошибке
def test_name_input_field_31_cyrilic_symbols(browser, open_registration_page):
    name_input_field = Input_Field_on_Registration_Page(browser)
    surname_input_field = Input_Field_on_Registration_Page(browser)
    error_message = Error_Message(browser)

    name_input_field.click_to_field_name()
    browser.implicitly_wait(10)
    name_input_field.send_keys_to_field_name("АбвгдабвгдабвгдабвгдабвгдабвгдА")
    browser.implicitly_wait(10)
    surname_input_field.click_to_field_surname()
    browser.implicitly_wait(10)

    assert len(error_message.get_list_of_error_messages()) == 1
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error_message.get_list_of_error_messages()

#тест RT-022 Проверка поля "Имя" 31 символами кирилицей и одним знаком "-", не появляется  сообщение об ошибке
def test_name_input_field_1_dash_symbol(browser, open_registration_page):
    name_input_field = Input_Field_on_Registration_Page(browser)
    surname_input_field = Input_Field_on_Registration_Page(browser)
    error_message = Error_Message(browser)

    name_input_field.click_to_field_name()
    browser.implicitly_wait(10)
    name_input_field.send_keys_to_field_name("Ия-ия")
    browser.implicitly_wait(10)
    surname_input_field.click_to_field_surname()
    browser.implicitly_wait(10)

    assert error_message.invisibility_of_error_message()

#тесты RT-023 - RT-025 Проверка поля "Имя" буквами кирилицей и двумя знаками "-",
# буквами кирилицей и символами кроме знака "-", числовыми значениями, буквами латиницей

@pytest.mark.parametrize("name", ["Ия?!%ия", "12345", "Tomas"], ids=["symbols not '-'", "digits", "latin characters"])
def test_symbols_digits_latin_in_name_field(browser, open_registration_page, name):
    name_input_field = Input_Field_on_Registration_Page(browser)
    surname_input_field = Input_Field_on_Registration_Page(browser)
    error_message = Error_Message(browser)

    name_input_field.click_to_field_name()
    browser.implicitly_wait(10)
    name_input_field.send_keys_to_field_name(name)
    browser.implicitly_wait(10)
    surname_input_field.click_to_field_surname()
    browser.implicitly_wait(10)

    assert len(error_message.get_list_of_error_messages()) == 1
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error_message.get_list_of_error_messages()