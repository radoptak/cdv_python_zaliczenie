from time import sleep

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from page_object_pattern.pages.create_account_page import CreatAccountPage
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.pages.register_page import SignInPage
from page_object_pattern.pages.search_result_page import SearchResultPage


class TestItemSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_item_search(self, setup):
        self.driver.get('http://automationpractice.com/index.php')
        home_page = HomePage(self.driver)
        results_page = SearchResultPage(self.driver)

        home_page.fill_search_input('Dress')
        home_page.perform_search()

        result = results_page.get_item_count()
        assert len(result) > 0


