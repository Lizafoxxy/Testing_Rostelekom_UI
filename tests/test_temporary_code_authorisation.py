
from pages.temporary_code_authorisasation_page import*
from pages.temp_code_confirmation_page import*


# тест RT-007 На странице есть поле для ввода телефона или электронной почты
def test_main_objects_present(browser, contact_input_field, button_get_code):
    page_title = Page_Title(browser)

    contact_input_field.go_to_temp_code_authorisation_page()
    browser.implicitly_wait(10)

    assert page_title.get_page_title_name() == "Авторизация по коду"
    assert contact_input_field.find_input_field() is not None
    assert button_get_code.name_button_get_code() == "Получить код"

# тест RT-008 Поле для ввода информации (телефона или электронной почты) не принимает кириллицу
def test_incorrect_data_to_input_field(browser, contact_input_field, button_get_code):
    error_message = Error_Message(browser)

    contact_input_field.go_to_temp_code_authorisation_page()
    browser.implicitly_wait(10)

    contact_input_field.click_to_input_field()
    contact_input_field.send_keys_input_field("Абвгд")
    browser.implicitly_wait(10)
    button_get_code.click_button_get_code()
    browser.implicitly_wait(5)

    assert error_message.find_error_message() is not None
    assert error_message.get_error_message_text() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

# тест RT-009 Переход на форму ввода временного кода
def test_redirect_to_code_enter_page(browser, contact_input_field, button_get_code):
    page_title = Page_Title(browser)
    contact_details = Contact_Details(browser)
    change_email_button = Change_Contact_Details_Button(browser)
    code_input_fields = Code_Input_Fields(browser)
    message_count_down = Message_Count_Down(browser)
    conf_page_title = Confirmation_Page_Title(browser)

    contact_input_field.go_to_temp_code_authorisation_page()
    browser.implicitly_wait(10)

    initial_page = page_title.get_page_title_name()
    contact_input_field.click_to_input_field()
    browser.implicitly_wait(5)
    contact_input_field.send_keys_input_field("pochta@mail.ru")
    browser.implicitly_wait(10)
    button_get_code.click_button_get_code()
    browser.implicitly_wait(10)

    assert initial_page == 'Авторизация по коду'
    assert conf_page_title.get_page_title_name() == 'Код подтверждения отправлен'
    assert "pochta@mail.ru" in contact_details.contact_details_text()
    assert change_email_button.find_button() is not None
    assert change_email_button.get_change_contact_details_button_name() == 'Изменить почту'
    assert code_input_fields.count_code_input_fields() == 6
    assert "Получить код повторно" in message_count_down.message_text()