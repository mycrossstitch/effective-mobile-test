
import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    PAGE_URL = 'https://effective-mobile.ru'

    LOCATORS = {
        "logo_header": (By.XPATH, "(//a[@href='#main' and text()='Effective Mobile'])[1]"),
        "logo_footer": (By.XPATH, "(//a[@href='#main' and text()='Effective Mobile'])[2]"),
        "about": (By.XPATH, "//a[@href='#about' and text()='[ О нас ]']"),
        "services" : (By.XPATH, "//a[@href='#moreinfo' and text()='[ Услуги ]']"),
        "cases": (By.XPATH, "//a[@href='#cases' and text()='[ Проекты ]']"),
        "Reviews" : (By.XPATH, "//a[@href='#Reviews' and text()='[ Отзывы ]']"),
        "contacts": (By.XPATH, "//a[@href='#contacts' and text()='[ Контакты ]']"),
        "specialists": (By.XPATH, "//a[@href='#specialists']"),
        "cooperation": (By.XPATH, "(//a[@href='#contacts'])[3]"),
        "moreinfo": (By.XPATH, "//a[@href='#moreinfo' and text()='Подробнее']")
    }

    LINKS = {
        "logo_header": "https://effective-mobile.ru/#main",
        "logo_footer": "https://effective-mobile.ru/#main",
        "about": "https://effective-mobile.ru/#about",
        "services": "https://effective-mobile.ru/#moreinfo",
        "cases": "https://effective-mobile.ru/#cases",
        "Reviews": "https://effective-mobile.ru/#Reviews",
        "contacts": "https://effective-mobile.ru/#contacts",
        "specialists": "https://effective-mobile.ru/#specialists",
        "cooperation": "https://effective-mobile.ru/#contacts",
        "moreinfo": "https://effective-mobile.ru/#moreinfo",
    }

    @allure.step("Проверка всех локаторов на главной странице")
    def check_all_locators_exist(self):
        errors = []  # сюда будем собирать сообщения об ошибках

        for name, locator in self.LOCATORS.items():
            with allure.step(f"Проверяем наличие элемента: {name}"):
                if not self.is_element_present(locator):
                    message = f"❌ Элемент '{name}' не найден. Локатор: {locator}"
                    allure.attach(
                        body=message,
                        name=f"Ошибка локатора: {name}",
                        attachment_type=allure.attachment_type.TEXT
                    )
                    errors.append(message)

        # после цикла — если были ошибки, падаем один раз
        if errors:
            error_text = "\n".join(errors)
            raise AssertionError(
                f"Обнаружены отсутствующие элементы:\n{error_text}"
            )

    @allure.step("Проверка корректности всех ссылок на главной странице")
    def check_all_links(self):
        errors = []

        for name, locator in self.LOCATORS.items():
            expected_url = self.LINKS.get(name)
            with allure.step(f"Проверяем элемент: {name}"):
                if not self.is_element_present(locator):
                    errors.append(f"❌ Элемент '{name}' отсутствует на странице")
                    continue

                try:

                    # Кликаем через уже готовый метод
                    self.click_element(locator)
                    self.verify_current_url(expected_url)

                except AssertionError as e:
                    errors.append(f"{name}: {e}")
                finally:
                    self.driver.back()

        if errors:
            raise AssertionError("\n".join(errors))
