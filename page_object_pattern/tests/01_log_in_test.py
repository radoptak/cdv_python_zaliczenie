import pytest
import allure
from page_object_pattern.pages.my_account_page import MyAccountPage
from page_object_pattern.pages.register_page import SignInPage
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.tests.utils.base_test import BaseTest
from page_object_pattern.tests.utils.env import env
from page_object_pattern.tests.utils import users


@pytest.mark.usefixtures('setup')
class TestLogIn(BaseTest):

    @allure.title('Test logowania')
    @allure.description('Logowanie istniejącym użytkownikiem')
    def test_log_in(self, setup):

        sign_in_page = SignInPage(self.driver)
        my_account_page = MyAccountPage(self.driver)
        home_page = HomePage(self.driver)

        self.driver.get(env)

        home_page.click_sign_in_button()
        sign_in_page.log_in(users.login_mail, users.pwd)
        sign_in_page.login_to_account()

        header = my_account_page.check_my_account_header()
        user = my_account_page.check_my_account_user()

        if header == 'My account':
            assert user == 'Roman Kowalski'
