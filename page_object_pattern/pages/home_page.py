class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_product_input_id = 'search_query_top'
        self.submit_button_name = 'submit_search'
        self.contact_link_id = 'contact-link'
        self.sign_in_button_class = 'login'
        self.page_title = driver.title

    def fill_search_input(self, item):
        self.driver.find_element_by_id(self.search_product_input_id).click()
        self.driver.find_element_by_id(self.search_product_input_id).send_keys(item)

    def perform_search(self):
        self.driver.find_element_by_name(self.submit_button_name).click()

    def click_sign_in_button(self):
        self.driver.find_element_by_class_name(self.sign_in_button_class).click()
