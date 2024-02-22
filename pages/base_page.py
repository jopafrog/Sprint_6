from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def scroll_to_position(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def send_keys(self, locator, key):
        element = self.find_element_with_wait(locator)
        element.send_keys(key)

    def switch_to_window(self, window_number):
        next_window = self.driver.window_handles[window_number]
        self.driver.switch_to.window(next_window)

    def current_url(self):
        return self.driver.current_url
