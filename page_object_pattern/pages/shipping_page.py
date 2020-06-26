import allure


class ShippingPage:

    def __init__(self, driver):
        self.driver = driver
        self.terms_checkbox_id = 'cgv'
        self.shipping_price_div_xpath = '//div[contains(@class, "delivery_option_price")]'
        self.proceed_checkout_further3_name = 'processCarrier'

    @allure.step('Przejście dalej')
    def proceed_checkout_4(self):
        self.driver.find_element_by_name(self.proceed_checkout_further3_name).click()

    @allure.step('Akceptacja warunków')
    def accept_terms(self):
        self.driver.find_element_by_id(self.terms_checkbox_id).click()

    @allure.step('Zwrócenie ceny wysyłki')
    def shipping_price(self):
        shipping_price_str = self.driver.find_element_by_xpath(self.shipping_price_div_xpath).get_attribute('textContent')
        shipping_stripped = shipping_price_str.strip()
        shipping = shipping_stripped[1:]
        shipping_float = float(shipping)
        return shipping_float
