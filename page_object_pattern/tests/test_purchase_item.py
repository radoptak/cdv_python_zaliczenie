import pytest

from page_object_pattern.pages.address_page import AddressPage
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.pages.payment_page import PaymentPage
from page_object_pattern.pages.product_page import ProductPage
from page_object_pattern.pages.register_page import SignInPage
from page_object_pattern.pages.search_result_page import SearchResultPage
from page_object_pattern.pages.shipping_page import ShippingPage
from page_object_pattern.pages.summary_page import SummaryPage
from page_object_pattern.tests.utils.base_test import BaseTest
from page_object_pattern.tests.utils.env import env
from page_object_pattern.tests.utils import users
from page_object_pattern.tests.utils import items


@pytest.mark.usefixtures('setup')
class TestPurchaseItem(BaseTest):

    def test_item_purchase(self, setup):

        home_page = HomePage(self.driver)
        results_page = SearchResultPage(self.driver)
        product_page = ProductPage(self.driver)
        sign_in_page = SignInPage(self.driver)
        address_page = AddressPage(self.driver)
        summary_page = SummaryPage(self.driver)
        shipping_page = ShippingPage(self.driver)
        payment_page = PaymentPage(self.driver)

        self.driver.get(env)

        home_page.click_sign_in_button()
        sign_in_page.log_in(users.login_mail, users.pwd)
        sign_in_page.login_to_account()

        home_page.fill_search_input(items.item1)
        home_page.perform_search()

        results_page.choose_item()
        price = product_page.price()
        product_page.add_to_cart()
        product_page.proceed_checkout()

        summary_page.scroll_down()
        tax_fee = summary_page.tax_fee()
        summary_page.proceed_checkout_2()

        summary_page.scroll_down()
        address_page.additional_message(users.additional_msg)
        address_page.proceed_checkout_3()

        shipping_page.accept_terms()
        shipping_fee = shipping_page.shipping_price()
        shipping_page.proceed_checkout_4()

        payment_page.choose_check_payment()
        summary_page.scroll_down()
        payment_page.confirm_order()

        alert = payment_page.check_order_status()

        total = price + shipping_fee + tax_fee
        payment = payment_page.payment_total()

        if alert == 'Your order on My Store is complete.':
            assert total == payment
