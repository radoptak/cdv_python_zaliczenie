class CreatAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.mr_title_radiobutton_id = 'id_gender1'
        self.mrs_title_radiobutton_id = 'id_gender2'
        self.first_name_input_id = 'customer_firstname'
        self.last_name_input_id = 'customer_lastname'
        self.email_input_id = 'email'
        self.pwd_input_id = 'passwd'
        self.day_of_birth_select_id = 'days'
        self.month_of_birth_select_id = 'months'
        self.year_of_birth_select_id = 'years'
        self.days = self.day_of_birth_option_xpath = '//*[@id="uniform-days"]//select[@id="days"]//option'
        self.months = self.month_of_birth_option_xpath = '//*[@id="uniform-months"]//select[@id="months"]//option'
        self.years = self.year_of_birth_option_xpath = '//*[@id="uniform-years"]//select[@id="years"]//option'
        self.newsletter_checkbox_id = 'newsletter'
        self.special_offers_checkbox_id = 'optin'

        self.address_first_name_input_id = 'firstname'
        self.address_last_name_input_id = 'lastname'
        self.address_company_input_id = 'company'
        self.address_address1_input_id = 'address1'
        self.address_address2_input_id = 'address2'
        self.address_city_input_id = 'city'
        self.address_state_input_select_id = 'id_state'
        self.states = self.address_state_option_xpath = '//*[@id="uniform-id_state"]//select[@id="id_state"]//option'
        self.address_postal_code_input_id = 'postcode'
        self.address_country_select_id = 'id_country'
        self.country = self.address_country_option_xpath = '//*[@id="uniform-id_country"]//select[@id="id_country"]//option'
        self.address_additional_info_textarea_id = 'other'
        self.address_home_phone_number_input_id = 'phone'
        self.address_mobile_phone_number_input_id = 'phone_mobile'
        self.address_email_alias_input_id = 'alias'

        self.register_button_id = 'submitAccount'

    def set_title_mr(self):
        self.driver.find_element_by_id(self.mr_title_radiobutton_id).click()

    def set_title_mrs(self):
        self.driver.find_element_by_id(self.mrs_title_radiobutton_id).click()

    def set_name_last_name(self, name, last_name):
        self.driver.find_element_by_id(self.first_name_input_id).click()
        self.driver.find_element_by_id(self.first_name_input_id).send_keys(name)
        self.driver.find_element_by_id(self.last_name_input_id).click()
        self.driver.find_element_by_id(self.last_name_input_id).send_keys(last_name)

    def set_email(self, email):
        self.driver.find_element_by_id(self.email_input_id).click()
        self.driver.find_element_by_id(self.email_input_id).send_keys(email)

    def set_pwd(self, pwd):
        self.driver.find_element_by_id(self.pwd_input_id).click()
        self.driver.find_element_by_id(self.pwd_input_id).send_keys(pwd)

    def set_date_of_birth(self):
        self.driver.find_element_by_id(self.day_of_birth_select_id).click()
        day_options = self.driver.find_elements_by_xpath(self.days)
        day_options[5].click()
        self.driver.find_element_by_id(self.month_of_birth_select_id).click()
        month_options = self.driver.find_elements_by_xpath(self.months)
        month_options[6].click()
        self.driver.find_element_by_id(self.year_of_birth_select_id).click()
        year_options = self.driver.find_elements_by_xpath(self.years)
        year_options[21].click()

    def set_newsletter(self):
        self.driver.find_element_by_id(self.newsletter_checkbox_id).click()

    def set_special_offer(self):
        self.driver.find_element_by_id(self.special_offers_checkbox_id).click()

    def set_address_user(self, name, last_name):
        self.driver.find_element_by_id(self.address_first_name_input_id).click()
        self.driver.find_element_by_id(self.address_first_name_input_id).send_keys(name)
        self.driver.find_element_by_id(self.address_first_name_input_id).click()
        self.driver.find_element_by_id(self.address_first_name_input_id).send_keys(last_name)

    def set_address_location(self, company, address1, address2, city, postal_code):
        self.driver.find_element_by_id(self.address_company_input_id).click()
        self.driver.find_element_by_id(self.address_company_input_id).send_keys(company)

        self.driver.find_element_by_id(self.address_address1_input_id).click()
        self.driver.find_element_by_id(self.address_address1_input_id).send_keys(address1)

        self.driver.find_element_by_id(self.address_address2_input_id).click()
        self.driver.find_element_by_id(self.address_address2_input_id).send_keys(address2)

        self.driver.find_element_by_id(self.address_city_input_id).click()
        self.driver.find_element_by_id(self.address_city_input_id).send_keys(city)

        self.driver.find_element_by_id(self.address_state_input_select_id).click()
        state_options = self.driver.find_elements_by_xpath(self.states)
        state_options[1].click()

        self.driver.find_element_by_id(self.address_postal_code_input_id).click()
        self.driver.find_element_by_id(self.address_postal_code_input_id).send_keys(postal_code)

        self.driver.find_element_by_id(self.address_country_select_id).click()
        state_options = self.driver.find_elements_by_xpath(self.country)
        state_options[1].click()

    def additional_msg(self, msg):
        self.driver.find_element_by_id(self.address_additional_info_textarea_id).click()
        self.driver.find_element_by_id(self.address_additional_info_textarea_id).send_keys(msg)

    def set_phone_number(self, number):
        self.driver.find_element_by_id(self.address_home_phone_number_input_id).click()
        self.driver.find_element_by_id(self.address_home_phone_number_input_id).send_keys(number)

    def set_mobile_number(self, mobile_num):
        self.driver.find_element_by_id(self.address_mobile_phone_number_input_id).click()
        self.driver.find_element_by_id(self.address_mobile_phone_number_input_id).send_keys(mobile_num)

    def set_alias_email(self, alias_email):
        self.driver.find_element_by_id(self.address_email_alias_input_id).click()
        self.driver.find_element_by_id(self.address_email_alias_input_id).send_keys(alias_email)

    def register(self):
        self.driver.find_element_by_id(self.register_button_id).click()







