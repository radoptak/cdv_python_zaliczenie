import pytest
import allure
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.pages.search_result_page import SearchResultPage
from page_object_pattern.tests.utils.base_test import BaseTest
from page_object_pattern.tests.utils.env import env


@pytest.mark.usefixtures('setup')
class TestItemSearch(BaseTest):

    @allure.title('Test wyszukiwania przedmiotu')
    @allure.description('Wyszukiwanie po frazie "Dress"')
    def test_item_search(self, setup):

        home_page = HomePage(self.driver)
        results_page = SearchResultPage(self.driver)

        self.driver.get(env)

        home_page.fill_search_input('Dress')
        home_page.perform_search()

        result = results_page.get_item_count()
        assert len(result) > 0


