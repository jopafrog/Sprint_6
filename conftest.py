import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# import data


@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    driver = webdriver.Firefox(options=options)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    return MainPage(driver)
