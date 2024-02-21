from pages.base_page import BasePage


class MainPage(BasePage):
    def click_to_question_and_get_answer_text(self, locator_question, locator_answer, number):
        locator_question = self.locator_number(locator_question, number)
        locator_answer = self.locator_number(locator_answer, number)

        self.scroll_to_position(locator_question)
        self.click_on_element(locator_question)

        return self.get_text_from_element(locator_answer)

    @staticmethod
    def locator_number(locator, number):
        method, locator = locator
        return method, locator.format(number)

    def click_to_scooter_button_and_return_title(self, locator_button, locator_main_title):
        self.click_on_element(locator_button)
        return self.get_text_from_element(locator_main_title)

    def click_to_yandex_button_and_return_dzen_link(self, locator_yandex_button, locator_dzen):
        self.click_on_element(locator_yandex_button)
        self.switch_to_window(1)
        self.find_element_with_wait(locator_dzen)
        return self.current_url()
