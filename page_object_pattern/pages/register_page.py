import allure
from allure_commons.types import AttachmentType


class SignInPage:

    def __init__(self, driver):
        self.driver = driver
        self.register_email_input_id = 'email_create'
        self.register_button_id = 'SubmitCreate'

        self.login_email_input_id = 'email'
        self.login_pwd_input_id = 'passwd'
        self.login_button_id = 'SubmitLogin'

    @allure.step('Podanie maila nowego użytkownika')
    def sign_in(self, reg_email):
        self.driver.find_element_by_id(self.register_email_input_id).click()
        self.driver.find_element_by_id(self.register_email_input_id).send_keys(reg_email)

    @allure.step('Kliknięcie Create Account')
    def create_account_button(self):
        self.driver.find_element_by_id(self.register_button_id).click()

    @allure.step('Podanie loginu i hasła')
    def log_in(self, login, password):
        self.driver.find_element_by_id(self.login_email_input_id).click()
        self.driver.find_element_by_id(self.login_email_input_id).send_keys(login)
        self.driver.find_element_by_id(self.login_pwd_input_id).click()
        self.driver.find_element_by_id(self.login_pwd_input_id).send_keys(password)

    @allure.step('Logowanie')
    def login_to_account(self):
        self.driver.find_element_by_id(self.login_button_id).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='logowanie do konta', attachment_type=AttachmentType.PNG)