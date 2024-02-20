from pages.base_page import BasePage


class MainPage(BasePage):
    def click_to_question_and_get_answer_text(self, locator_question, locator_answer, number):
        locator_question = self.locator_number(locator_question, number)
        locator_answer = self.locator_number(locator_answer, number)

        self.scroll_to_question(locator_question)
        self.click_on_element(locator_question)

        return self.get_text_from_element(locator_answer)

    def scroll_to_question(self, locator):
        self.scroll_to_position(locator)

    @staticmethod
    def locator_number(locator, number):
        method, locator = locator
        return method, locator.format(number)
