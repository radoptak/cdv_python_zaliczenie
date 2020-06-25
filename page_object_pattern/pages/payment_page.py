class PaymentPage:

    def __init__(self, driver):
        self.driver = driver
        self.payment_span_xpath = '//*[contains(@class, "order-confirmation")]/span/strong'
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

    def payment_total(self):
        payment_str = self.driver.find_element_by_xpath(self.payment_span_xpath).get_attribute('textContent')
        payment = payment_str[1:]
        payment_float = float(payment)
        return payment_float
