class PaymentPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_price_td_xpath = '//td[contains(@class, "cart_total")]//span[contains(@class, "price")]'
        self.shipping_price_td_xpath = '//*[@id="total_shipping"]'
        self.tax_fee_td_id = 'total_tax'
        self.payment_span_id = 'total_price'

        self.bank_payment_link_class = 'bankwire'
        self.check_payment_link_class = 'cheque'
        self.confirm_order_button_xpath = '//*[@id="cart_navigation"]/button'
        self.order_alert_p_class = 'alert-success'

    def choose_bank_payment(self):
        self.driver.find_element_by_class_name(self.bank_payment_link_class).click()

    def choose_check_payment(self):
        self.driver.find_element_by_class_name(self.check_payment_link_class).click()

    def confirm_order(self):
        self.driver.find_element_by_xpath(self.confirm_order_button_xpath).click()

    def check_order_status(self):
        success_alert = self.driver.find_element_by_class_name(self.order_alert_p_class).get_attribute('textContent')
        return success_alert

    def shipping_price(self):
        shipping_price_str = self.driver.find_element_by_xpath(self.shipping_price_td_xpath)
        # shipping = shipping_price_str[1:]
        # shipping_float = float(shipping)
        return shipping_price_str

    def tax_fee(self):
        tax_fee_str = self.driver.find_element_by_id(self.tax_fee_td_id).get_attribute('textContent')
        tax = tax_fee_str[1:]
        tax_float = float(tax)
        return tax_float

    def payment_total(self):
        payment_str = self.driver.find_element_by_id(self.payment_span_id).get_attribute('textContent')
        payment = payment_str[1:]
        payment_float = float(payment)
        return payment_float
