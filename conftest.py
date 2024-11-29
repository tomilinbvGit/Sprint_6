import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    # Фикстура для загрузки драйвера
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
