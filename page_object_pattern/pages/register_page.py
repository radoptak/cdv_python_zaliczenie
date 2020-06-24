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

    def log_in(self, login, password):
        self.driver.find_element_by_id(self.login_email_input_id).click()
        self.driver.find_element_by_id(self.login_email_input_id).send_keys(login)
        self.driver.find_element_by_id(self.login_pwd_input_id).click()
        self.driver.find_element_by_id(self.login_pwd_input_id).send_keys(password)

    def login_to_account(self):
        self.driver.find_element_by_id(self.login_button_id).click()
