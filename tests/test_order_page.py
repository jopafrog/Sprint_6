import pytest
import data
import allure


class TestOrderPage:
    @allure.title('Проверка оформления заказа через кнопку {button_position}')
    @pytest.mark.parametrize("button_position", ['up_button', 'down_button'])
    def test_order_success(self, order_page, button_position):
        order_page.click_on_order_button(button_position)

        order_page.fill_name_field(data.TEST_USER_NAME)
        order_page.fill_surname_field(data.TEST_USER_SURNAME)
        order_page.fill_address_field(data.TESS_USER_ADDRESS)
        order_page.fill_metro_field(9)
        order_page.fill_phone_field(data.TEST_USER_PHONE)

        order_page.click_on_next_button()

        order_page.fill_date_field(data.TEST_DATA)
        order_page.fill_rental_time_field(data.RENTAL_TIME[2])

        status_button_text = order_page.confirm_order_and_get_text_status_button()

        assert "Посмотреть статус" == status_button_text
