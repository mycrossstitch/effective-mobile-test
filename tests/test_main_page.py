import pytest
from pages.main_page import MainPage
import allure

class TestMainPage:

    def setup_method(self):
        self.main_page = MainPage(self.driver)


    @allure.feature("Проверка локаторов главной страницы")
    @pytest.mark.ui
    def test_locators_exist(self):
        self.main_page.open()
        self.main_page.check_all_locators_exist()

    @allure.feature("Проверка корректности переходов по ссылкам на главной странице")
    @pytest.mark.ui
    def test_links_exist_and_work(self):
        self.main_page.open()
        self.main_page.check_all_links()