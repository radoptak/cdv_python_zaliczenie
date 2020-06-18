from time import sleep

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from page_object_pattern.pages.create_account_page import CreatAccountPage
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.pages.my_account_page import MyAccountPage
from page_object_pattern.pages.register_page import SignInPage


class TestRegisterAccount:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_registration(self, setup):
        self.driver.get('http://automationpractice.com/index.php')
        registration_page = CreatAccountPage(self.driver)
        home_page = HomePage(self.driver)
        sign_in_page = SignInPage(self.driver)
        my_account_page = MyAccountPage(self.driver)

        home_page.click_sign_in_button()
        sign_in_page.sign_in('test11123567@wp.pl')
        sign_in_page.create_account_button()

        registration_page.set_title_mr()
        registration_page.set_title_mrs()
        sleep(2)
        registration_page.set_name_last_name('Roman', 'Kowalski')
        registration_page.set_pwd('Pwd123#')
        sleep(3)
        registration_page.set_date_of_birth()
        registration_page.set_newsletter()
        registration_page.set_special_offer()
        sleep(4)

        # registration_page.set_address_user('Roman', 'Kowalski')
        registration_page.set_address_location('Polex', 'Polska 6', 'apart 66', 'Alabama', '11122')
        registration_page.additional_msg('Additional message')
        sleep(4)
        registration_page.set_phone_number('000111222')
        registration_page.set_mobile_number('111222333')
        registration_page.set_alias_email('test22234567@wp.pl')

        registration_page.register()

        header = my_account_page.account_header_class()
        user = my_account_page.account_link_class()

        if header == 'My account':
            assert user == 'Roman Kowalski'
        else:
            print('nope')

        sleep(15)
