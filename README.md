README.md
# Automated UI tests — effective-mobile.ru (Selenium)

Проект покрывает тесты для главной страницы сайта `effective-mobile.ru`.

### Технологии:
- Python 3.10
- Selenium WebDriver
- pytest
- allure-pytest

### Требования
- Python 3.10
- Установленный браузер Chrome или Edge
- ChromeDriver, соответствующий версии браузера

### Установка локально
1. Создать виртуальное окружение (Python 3.10):
powershell
 - py -3.10 -m venv venv
 - venv\Scripts\activate
2.	Установить зависимости:
 - pip install -r requirements.txt
3. Установить allure
 - скачать с https://github.com/allure-framework/allure2/releases
 - распаковать в C:\allure
 - добавить путь C:\allure\bin в переменную окружения PATH
 - закрыть все терминалы (чтобы обновился PATH) и проверить: 
allure --version
### Запуск тестов
 - pytest -v --alluredir=allure-results
# Просмотр отчёта
 - allure serve allure-results
# Запуск тестов в Docker
### сборка образа
docker build -t effective-mobile-tests:latest .
### запуск контейнера (монтируем папку с результатами)
 - docker run --rm -v %cd%/allure-results:/app/allure-results effective-mobile-tests:latest

# Что проверяется
 - 	Переходы по основным блокам/ссылкам главной страницы (О нас, Контакты и др.) — локаторы и URL’ы.
 - 	Реализован паттерн Page Object.
 - Интеграция с Allure для удобного анализа результатов.
