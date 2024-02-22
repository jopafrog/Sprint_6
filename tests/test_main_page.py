import allure
import pytest


class TestMainPage:
    @allure.title('Проверка ответов на Вопросы о важном, вопрос {number}')
    @pytest.mark.parametrize(
        "number, expected_text",
        [
            (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
            (1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто '
                'сделать несколько заказов — один за другим.'),
            (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени '
                'аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30,'
                ' суточная аренда закончится 9 мая в 20:30.'),
            (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
            (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
            (5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься '
                'без передышек и во сне. Зарядка не понадобится.'),
            (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
            (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'),
        ])
    def test_question_text_success(self, main_page, number, expected_text):
        text_answer = main_page.click_to_question_and_get_answer_text(number)
        assert text_answer == expected_text

    @allure.title('При нажатии на лого "Самокат" переходим на главную страницу')
    def test_scooter_button_success(self, main_page):
        main_page.click_to_scooter_button()
        page_title = main_page.get_text_tittle()
        assert 'на пару дней' in page_title

    @allure.title('При нажатии на лого "Яндекс" переходим на страницу Дзен')
    def test_go_to_dzen_success(self, main_page):
        main_page.click_to_yandex_button()
        page_link = main_page.switch_to_window_and_return_link()
        assert 'dzen.ru' in page_link
