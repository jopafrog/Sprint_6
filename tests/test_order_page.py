import pytest
import data
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:
    @pytest.mark.parametrize(
        "locator, button_position",
        [
            (OrderPageLocators.UP_BUTTON, 'up_button'),
            (OrderPageLocators.DOWN_BUTTON, 'down_button')
        ])
    def test_order_success(self, order_page, locator, button_position):
        order_page.click_on_order_button(locator, button_position)

        order_page.insert_to_field(OrderPageLocators.NAME_INPUT, data.TEST_USER_NAME)
        order_page.insert_to_field(OrderPageLocators.SURNAME_INPUT, data.TEST_USER_SURNAME)
        order_page.insert_to_field(OrderPageLocators.ADDRESS_INPUT, data.TESS_USER_ADDRESS)

        order_page.fill_metro_field(OrderPageLocators.METRO_INPUT, OrderPageLocators.METRO_STATION)

        order_page.insert_to_field(OrderPageLocators.PHONE_INPUT, data.TEST_USER_PHONE)

        order_page.click_on_button_order_form(OrderPageLocators.NEXT_BUTTON)

        order_page.insert_to_field(OrderPageLocators.DATA_INPUT, data.TEST_DATA)
        order_page.fill_time_order_field(OrderPageLocators.DROP_MENU_TIME_ARROW, OrderPageLocators.DROP_MENU_TIME)

        assert "Посмотреть статус" == order_page.confirm_order(
            OrderPageLocators.ORDER_BUTTON, OrderPageLocators.ACCEPT_BUTTON, OrderPageLocators.STATUS_BUTTON)
