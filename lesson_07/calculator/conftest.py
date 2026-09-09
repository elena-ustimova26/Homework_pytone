import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Фикстура, предоставляющая экземпляр драйвера Chrome
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
