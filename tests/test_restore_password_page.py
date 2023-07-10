from pages.restore_password_page import*
from pages.authorisation_page import*

#тест RT-010 На странице восстановления пароля есть меню, поле для ввода и кнопка "Продолжить"
def test_restore_password_page_main_elements_present(browser, open_restore_password_page, tab_telephone, tab_email, tab_login, tab_ls, button_forgot_password):
    input_field = Field_on_Restore_Page(browser)
    button_continue = Buttons_on_Restore_Page(browser)
    page_title = Title_on_Restore_Page(browser)

    assert "Восстановление пароля" in page_title.get_page_title_name()
    assert tab_telephone.name_tab_telephone() == "Телефон"
    assert tab_email.name_tab_email() == "Почта"
    assert tab_login.name_tab_login() == "Логин"
    assert tab_ls.name_tab_ls() == "Лицевой счёт"
    assert button_continue.name_button_continue() == "Продолжить"
    assert input_field.find_input_field() is not None

# тест RT-011 На странице восстановления пароля есть капча и поле для ввода капчи с подсказкой
def test_restore_password_page_captcha_present(browser, open_restore_password_page):
    captcha = Captcha_on_Restore_Page(browser)
    captcha_input_field = Field_on_Restore_Page(browser)
    captcha_prompt = Field_on_Restore_Page(browser)

    assert captcha.find_captcha() is not None
    assert captcha_input_field.find_input_field() is not None
    assert "Символы" in captcha_prompt.get_text_from_captcha_field_placeholder()

# тест RT-012 Возврат на форму авторизации
def test_return_to_authorisation_page(browser, open_restore_password_page):
    button_reset_back = Buttons_on_Restore_Page(browser)
    page_title = Title_on_Authorisation_Page(browser)

    button_reset_back.click_button_reset_back()
    browser.implicitly_wait(10)

    assert "Авторизация" in page_title.get_page_title_name()