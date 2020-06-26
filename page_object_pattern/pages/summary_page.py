import allure


class SummaryPage:

    def __init__(self, driver):
        self.driver = driver
        self.tax_fee_td_id = 'total_tax'
        self.proceed_button_link_class_name = 'standard-checkout'
        self.cancel_purchase_i_class = 'icon-trash'
        self.cancel_alert_p_class = 'alert-warning'

    @allure.step('Logowanie')
    def proceed_checkout_2(self):
        self.driver.find_element_by_class_name(self.proceed_button_link_class_name).click()

    @allure.step('Skrollowanie')
    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Anulowanie zakupu')
    def cancel_purchase(self):
        self.driver.find_element_by_class_name(self.cancel_purchase_i_class).click()

    @allure.step('Logowanie')
    def get_cancel_alert(self):
        cancel_alert_str = self.driver.find_element_by_class_name(self.cancel_alert_p_class).get_attribute('textContent')
        return cancel_alert_str

    @allure.step('Zwrócenie ceny podatku')
    def tax_fee(self):
        tax_fee_str = self.driver.find_element_by_id(self.tax_fee_td_id).get_attribute('textContent')
        tax = tax_fee_str[1:]
        tax_float = float(tax)
        return tax_float


