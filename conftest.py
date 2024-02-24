import pytest
import data
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
@allure.title('Запуск драйвера (FireFox)')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    driver = webdriver.Firefox(options=options)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
@allure.title('Переход на главную и создание объекта MainPage')
def main_page(driver):
    driver.get(data.MAIN_PAGE_URL)
    return MainPage(driver)


@pytest.fixture(scope='function')
@allure.title('Переход на главную и создание объекта OrderPage')
def order_page(driver):
    driver.get(data.MAIN_PAGE_URL)
    return OrderPage(driver)
