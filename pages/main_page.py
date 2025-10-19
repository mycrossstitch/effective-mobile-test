
import allure
from pages.base_page import BasePage
from pages.locators import MainPageLocators as MPL

class MainPage(BasePage):

    PAGE_URL = 'https://effective-mobile.ru'

    @allure.step("Проверка всех локаторов на главной странице")
    def check_all_locators_exist(self, locators):
        errors = []  # сюда будем собирать сообщения об ошибках

        for name, locator in locators.items():
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
    def check_all_links(self, locators):
        errors = []

        # Перебираем ссылки по ключу
        for name, relative_url in MPL.LINKS.items():
            locator = locators.get(name)
            expected_url = f"{self.PAGE_URL}{relative_url}"

            with allure.step(f"Проверяем элемент: {name}"):
                # Проверяем наличие локатора
                if not locator:
                    errors.append(f"⚠️ Для '{name}' нет локатора в LOCATORS")
                    continue

                # Проверяем, что элемент есть на странице
                if not self.is_element_present(locator):
                    errors.append(f"❌ Элемент '{name}' отсутствует на странице")
                    continue

                try:
                    # Если бургер-меню, нужно открыть
                    if "burger_button" in locators and name not in MPL.PAGE_LINKS:
                        self.click_element(locators["burger_button"])
                    # Кликаем и проверяем переход
                    self.click_element(locator)
                    self.verify_current_url(expected_url)
                except AssertionError as e:
                    errors.append(f"{name}: {e}")
                finally:
                    # Возврат на главную
                    self.driver.back()

        if errors:
            raise AssertionError("\n".join(errors))
