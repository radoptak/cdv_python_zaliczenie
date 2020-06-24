class SummaryPage:

    def __init__(self, driver):
        self.driver = driver
        self.proceed_button_link_class_name = 'standard-checkout'
        self.cancel_purchase_i_class = 'icon-trash'
        self.cancel_alert_p_class = 'alert-warning'

    def proceed_checkout_2(self):
        self.driver.find_element_by_class_name(self.proceed_button_link_class_name).click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def cancel_purchase(self):
        self.driver.find_element_by_class_name(self.cancel_purchase_i_class).click()

    def get_cancel_alert(self):
        cancel_alert_str = self.driver.find_element_by_class_name(self.cancel_alert_p_class).get_attribute('textContent')
        return cancel_alert_str

