class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_name_xpath = '//*[@id="center_column"]//h1'
        self.add_to_cart_button_xpath = '//*[@id="add_to_cart"]/button'
        self.product_price_span_id = 'our_price_display'
        self.proceed_checkout_button_class = 'button-medium'

    def check_product_name(self):
        product_name = self.driver.find_element_by_class_name(self.product_name_xpath).get_attribute('textContent')
        return product_name

    def add_to_cart(self):
        self.driver.find_element_by_xpath(self.add_to_cart_button_xpath).click()

    def proceed_checkout(self):
        self.driver.find_element_by_class_name(self.proceed_checkout_button_class).click()

    def price(self):
        price_str = self.driver.find_element_by_id(self.product_price_span_id).get_attribute('textContent')
        price = price_str[1:]
        price_float = float(price)
        return price_float


