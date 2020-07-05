from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == LoginPageLocators.LOGIN_PAGE, f'{self.browser.current_url} is not login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_INPUT)
        email_input.send_keys(email)
        password_1_input = self.browser.find_element(*LoginPageLocators.PASSWORD_1_REGISTER_INPUT)
        password_1_input.send_keys(password)
        password_2_input = self.browser.find_element(*LoginPageLocators.PASSWORD_2_REGISTER_INPUT)
        password_2_input.send_keys(password)
        btn_register_submit = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER_SUBMIT)
        btn_register_submit.click()
