class ShippingPage:

    def __init__(self, driver):
        self.driver = driver
        self.terms_checkbox_id = 'cgv'
        self.proceed_checkout_further3_name = 'processCarrier'

    def proceed_checkout_4(self):
        self.driver.find_element_by_name(self.proceed_checkout_further3_name).click()

    def accept_terms(self):
        self.driver.find_element_by_id(self.terms_checkbox_id).click()
