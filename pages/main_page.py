from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step('Нажать на вопрос и вернуть текст ответа')
    def click_to_question_and_get_answer_text(self, question_number):
        locator_question = self.locator_number(MainPageLocators.QUESTION_LOCATOR, question_number)
        self.scroll_to_position(locator_question)
        self.click_on_element(locator_question)

        locator_answer = self.locator_number(MainPageLocators.ANSWER_LOCATOR, question_number)
        return self.get_text_from_element(locator_answer)

    @staticmethod
    def locator_number(locator, number):
        method, locator = locator
        return method, locator.format(number)

    @allure.step('Нажать на лого "Самокат" в шапке сайта')
    def click_to_scooter_button(self):
        self.click_on_element(MainPageLocators.SCOOTER_LINK)

    @allure.step('Получить текст на странице')
    def get_text_tittle(self):
        return self.get_text_from_element(MainPageLocators.MAIN_PAGE_TITLE)

    @allure.step('Нажать на лого "Яндекс" в шапке сайта')
    def click_to_yandex_button(self):
        self.click_on_element(MainPageLocators.YANDEX_LINK)

    @allure.step('Поменять вкладку и вернуть её адрес')
    def switch_to_window_and_return_link(self):
        self.switch_to_window(1)
        self.find_element_with_wait(MainPageLocators.DZEN_LOGO)
        return self.current_url()
