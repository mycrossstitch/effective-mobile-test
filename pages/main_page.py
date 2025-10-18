
import allure
from pages.base_page import BasePage
from pages.locators import MainPageLocators as MPL

class MainPage(BasePage):

    PAGE_URL = 'https://effective-mobile.ru'

    def get_locators(self):
        """Выбираем текущий набор локаторов в зависимости от наличия бургер-меню"""
        if self.is_element_visible(MPL.LOCATORS_BURGER_MENU["burger_button"]):
            return MPL.LOCATORS_BURGER_MENU
        return MPL.LOCATORS_FULL_MENU



    @allure.step("Проверка всех локаторов на главной странице")
    def check_all_locators_exist(self):
        errors = []  # сюда будем собирать сообщения об ошибках
        locators = self.get_locators()

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
    def check_all_links(self):
        errors = []
        locators = self.get_locators()

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
