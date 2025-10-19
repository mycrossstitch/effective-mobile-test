import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver(request):
    window_size = getattr(request, "param", (1920, 1080))  # по умолчанию десктоп
    options = Options()
    #options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"--window-size={window_size[0]},{window_size[1]}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    request.cls.driver = driver
    yield
    driver.close()