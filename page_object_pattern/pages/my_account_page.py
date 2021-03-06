import allure


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.account_link_class = 'account'
        self.account_header_class = 'page-heading'

    @allure.step('Sprawdzenie poprawnosci nagłówka')
    def check_my_account_header(self):
        account_header = self.driver.find_element_by_class_name(self.account_header_class).get_attribute('textContent')
        return account_header

    @allure.step('Sprawdzenie użytkownika')
    def check_my_account_user(self):
        account_user = self.driver.find_element_by_class_name(self.account_link_class).get_attribute('textContent')
        return account_user
