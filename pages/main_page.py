from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    PAGE_URL = 'https://effective-mobile.ru'

    LOGO_HEADER_LOCATOR = ("xpath", "(//a[@href='#main' and text()='Effective Mobile'])[1]")
    LOGO_FOOTER_LOCATOR = ("xpath", "(//a[@href='#main' and text()='Effective Mobile'])[2]")

    ABOUT_LOCATOR = ("xpath", "(//a[@href='#about'])[2]")

