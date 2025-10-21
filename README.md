# Automated UI tests — effective-mobile.ru (Selenium)

Проект покрывает тесты для главной страницы сайта `effective-mobile.ru`.

# Что проверяется
 - 	Переходы по основным блокам/ссылкам главной страницы (О нас, Контакты и др.) — локаторы и URL’ы.
 - 	Реализован паттерн Page Object.
 -  Интеграция с Allure для удобного анализа результатов.

# Особенности тестирования
 - Тесты параметризованы для двух типов меню: полноэкранное (1920x1080) и бургер-меню (768x1024)
 - Используется headless режим для CI/CD

### Технологии:
- Python 3.10
- Selenium WebDriver
- pytest
- allure-pytest

### Требования
- Python 3.10
- Установленный браузер Chrome или Edge
- ChromeDriver, соответствующий версии браузера

### Структура проекта

effective-mobile-test/
├── allure/
│ └── environment.properties
├── pages/
│ ├── base_page.py
│ ├── locators.py
│ └── main_page.py
├── tests/
│ └── test_main_page.py
├── __init__.py
├── conftest.py
├── requirements.txt
├── pytest.ini
├── README.md
├── docker-compose.yml
└── Dockerfile

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
 - 
### Запуск тестов
 - pytest -v --alluredir=allure-results
 - запуск только мобильных тестов: pytest -k "burger" -v --alluredir=allure-results
 - запуск только десктопных тестов: pytest -k "full" -v --alluredir=allure-results
 
### Просмотр отчёта (после запуска тестов)
 - allure serve allure-results

# Запуск тестов в Docker

### сборка образа
docker-compose build --no-cache

### запуск контейнера 
docker-compose up

### просмотр отчета
http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html
