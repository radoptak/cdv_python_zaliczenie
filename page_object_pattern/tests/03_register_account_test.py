import pytest
import allure
from page_object_pattern.pages.create_account_page import CreatAccountPage
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.pages.my_account_page import MyAccountPage
from page_object_pattern.pages.register_page import SignInPage
from page_object_pattern.tests.utils.base_test import BaseTest
from page_object_pattern.tests.utils.env import env
from page_object_pattern.tests.utils import users

from uuid import uuid4


@pytest.mark.usefixtures('setup')
class TestRegisterAccount(BaseTest):

    @allure.title('Test rejestracji konta')
    @allure.description('Rejestrowanie nowego użytkownika')
    def test_registration(self, setup):

        registration_page = CreatAccountPage(self.driver)
        home_page = HomePage(self.driver)
        sign_in_page = SignInPage(self.driver)
        my_account_page = MyAccountPage(self.driver)

        self.driver.get(env)

        home_page.click_sign_in_button()
        email = f"{str(uuid4())[:5]}test@gmail.com"
        sign_in_page.sign_in(email)
        sign_in_page.create_account_button()

        registration_page.set_title_mr()
        registration_page.set_title_mrs()
        registration_page.set_name_last_name(users.name1, users.last_name1)
        registration_page.set_pwd(users.pwd)
        registration_page.set_date_of_birth()
        registration_page.set_newsletter()
        registration_page.set_special_offer()

        registration_page.set_address_location(users.company, users.address1, users.address2, users.city, users.postal_code)
        registration_page.additional_msg(users.additional_msg)
        registration_page.set_phone_number(users.phone_num)
        registration_page.set_mobile_number(users.mobile_num)
        registration_page.set_alias_email(users.alias_email)

        registration_page.register()

        header = my_account_page.check_my_account_header()
        user = my_account_page.check_my_account_user()

        if header == 'My account':
            assert user == 'Roman Kowalski'
        else:
            print('nope')

