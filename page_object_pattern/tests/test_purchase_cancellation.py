import pytest

from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.pages.product_page import ProductPage
from page_object_pattern.pages.register_page import SignInPage
from page_object_pattern.pages.search_result_page import SearchResultPage
from page_object_pattern.pages.summary_page import SummaryPage
from page_object_pattern.tests.utils.base_test import BaseTest

from page_object_pattern.tests.utils.env import env
from page_object_pattern.tests.utils import users
from page_object_pattern.tests.utils import items


@pytest.mark.usefixtures('setup')
class TestPurchaseCancellation(BaseTest):

    def test_item_purchase_cancellation(self, setup):

        home_page = HomePage(self.driver)
        results_page = SearchResultPage(self.driver)
        product_page = ProductPage(self.driver)
        sign_in_page = SignInPage(self.driver)
        summary_page = SummaryPage(self.driver)

        self.driver.get(env)

        home_page.click_sign_in_button()
        sign_in_page.log_in(users.login_mail, users.pwd)
        sign_in_page.login_to_account()
        home_page.fill_search_input(items.item1)
        home_page.perform_search()

        results_page.choose_item()
        product_page.add_to_cart()
        product_page.proceed_checkout()
        summary_page.cancel_purchase()

        cancellation_alert = summary_page.get_cancel_alert()

        assert cancellation_alert == "Your shopping cart is empty."


