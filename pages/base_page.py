from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver


    def open(self):
        self.driver.get(self.PAGE_URL)


    @allure.step("Проверяем, что элемент присутствует на странице")
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except (NoSuchElementException):
            return False
        return True


    @allure.step("Проверяем, что элемент отсутствует на странице")
    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False


    @allure.step("Ожидание кликабельности и клик по элементу")
    def click_element(self, locator, timeout=5):
        """Ожидает, пока элемент станет кликабельным, и кликает по нему"""
        try:

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            element.click()

        except TimeoutException:
            raise AssertionError(f"⏳ Элемент не кликабелен или отсутствует: {locator}")
        except NoSuchElementException:
            raise AssertionError(f"❌ Элемент не найден: {locator}")


    @allure.step("Проверка корректности URL после перехода")
    def verify_current_url(self, expected_url, timeout=5):
        """Проверяет, совпадает ли текущий URL с ожидаемым"""
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url != "")
        current_url = self.driver.current_url

        if current_url != expected_url:
            allure.attach(
                body=f"Ожидали: {expected_url}\nПолучили: {current_url}",
                name="Несовпадение URL",
                attachment_type=allure.attachment_type.TEXT
            )
            raise AssertionError(
                f"❌ Некорректный URL:\nОжидали: {expected_url}\nПолучили: {current_url}"
            )
