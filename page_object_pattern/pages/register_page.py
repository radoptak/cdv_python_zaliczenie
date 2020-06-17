class SignInPage:

    def __init__(self, driver):
        self.driver = driver
        self.register_email_input_id = 'email_create'
        self.register_button_id = 'SubmitCreate'

        self.login_email_input_id = 'email'
        self.login_pwd_input_id = 'passwd'
        self.login_button_id = 'SubmitLogin'

    def sign_in(self, reg_email):
        self.driver.find_element_by_id(self.register_email_input_id).click()
        self.driver.find_element_by_id(self.register_email_input_id).send_keys(reg_email)

    def create_account_button(self):
        self.driver.find_element_by_id(self.register_button_id).click()