class SearchResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_results_xpath = '//li[contains(@class, "ajax_block_product")]'

    def get_item_count(self):
        items = self.driver.find_elements_by_xpath(self.search_results_xpath)
        return items
