from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class BasePage:



    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)

