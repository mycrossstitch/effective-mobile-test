import pytest

from pages.main_page import MainPage
from pages.locators import MainPageLocators as MPL
import allure

@pytest.mark.parametrize(
    "menu_type, window_size, locators",
    [
        ("full", (1920, 1080), MPL.LOCATORS_FULL_MENU),
        ("burger", (768, 1024), MPL.LOCATORS_BURGER_MENU),
    ]   )

class TestMainPage:
    @pytest.fixture(autouse=True)
    def setup_method(self, driver, menu_type, window_size, locators):
        self.main_page = MainPage(self.driver)
        self.driver.set_window_size(*window_size)
        self.menu_type = menu_type
        self.locators = locators


    @allure.feature("Проверка локаторов главной страницы")
    @pytest.mark.ui
    def test_locators_exist(self):
        self.main_page.open()
        self.main_page.check_all_locators_exist(self.locators)

    @allure.feature("Проверка корректности переходов по ссылкам на главной странице")
    @pytest.mark.ui
    def test_links_exist_and_work(self):
        self.main_page.open()
        self.main_page.check_all_links(self.locators)