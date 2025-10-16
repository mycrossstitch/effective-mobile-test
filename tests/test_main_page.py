import time

import pytest
from pages.main_page import MainPage
import allure

class TestMainPage:

    def setup_method(self):
        self.main_page = MainPage(self.driver)

    def test_open_url(self):
        self.main_page.open()
        time.sleep(5)