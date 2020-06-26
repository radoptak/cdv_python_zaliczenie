import allure


class SearchResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_results_xpath = '//li[contains(@class, "ajax_block_product")]'
        self.returned_items_xpath = '//li[contains(@class, "ajax_block_product")]//a[contains(@class, "product-name")]'

    @allure.step('Pobranie liczby przedmiotów')
    def get_item_count(self):
        items = self.driver.find_elements_by_xpath(self.search_results_xpath)
        return items

    @allure.step('Wybór przedmiotu')
    def choose_item(self):
        items = self.driver.find_elements_by_xpath(self.returned_items_xpath)
        items[1].click()

    @allure.step('Pobranie listy przedmiotów')
    def get_item_title(self):
        items = self.driver.find_elements_by_xpath(self.returned_items_xpath)
        items[1].get_attribute('textContent')
        return items
