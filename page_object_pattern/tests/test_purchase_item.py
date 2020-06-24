from time import sleep

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
        product_page.add_to_cart()
        sleep(1)
        product_page.proceed_checkout()
        sleep(1)
        summary_page.scroll_down()
        sleep(1)
        summary_page.proceed_checkout_2()
        sleep(1)
        summary_page.scroll_down()
        sleep(1)
        address_page.additional_message(users.additional_msg)
        sleep(1)
        address_page.proceed_checkout_3()
        sleep(1)
        shipping_page.accept_terms()
        sleep(1)
        shipping_page.proceed_checkout_4()
        sleep(1)
        payment_page.choose_check_payment()
        sleep(1)
        summary_page.scroll_down()
        sleep(1)
        payment_page.confirm_order()
        sleep(1)

        alert = payment_page.check_order_status()
        print(alert)
        # price = product_page.price()
        # print('AAAAAA ' + price)
        shipping_fee = payment_page.shipping_price()
        print(shipping_fee)

        tax_fee = payment_page.tax_fee()
        print(tax_fee)
        total = price + shipping_fee + tax_fee
        payment = payment_page.payment_total()

        if alert == 'Your order on My Store is complete.':
            print('weszlem')
            assert total == payment
            print('cena sie zgadza')

        sleep(5)


