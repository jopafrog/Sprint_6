from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):
    @staticmethod
    def locator_add_value(locator, value):
        method, locator = locator
        return method, locator.format(value)

    @allure.step('Нажимаем на кнопку заказа')
    def click_on_order_button(self, button_position):
        if button_position == 'down_button':
            self.scroll_to_position(OrderPageLocators.DOWN_BUTTON)
            self.click_on_element(OrderPageLocators.DOWN_BUTTON)
        else:
            self.click_on_element(OrderPageLocators.UP_BUTTON)

    @allure.step('Заполнить поле имени (Имя: {name})')
    def fill_name_field(self, name):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)

    @allure.step('Заполнить поле фамилии (Фамилия: {surname})')
    def fill_surname_field(self, surname):
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step('Заполнить поле адреса (Адрес: {address})')
    def fill_address_field(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Заполнить поле телефона (Телефон: {phone})')
    def fill_phone_field(self, phone):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Заполнить поле даты заказа (Дата: {date})')
    def fill_date_field(self, date):
        self.send_keys(OrderPageLocators.DATA_INPUT, date)

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_on_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем форму выбора станции метро (Номер станции в списке: {number})')
    def fill_metro_field(self, number):
        self.click_on_element(OrderPageLocators.METRO_INPUT)
        locator_metro_station = self.locator_add_value(OrderPageLocators.METRO_STATION_NUMBER, number)
        self.click_on_element(locator_metro_station)

    @allure.step('Выбираем значение из списка поля "Срок аренды" (Срок: "{rental_time}")')
    def fill_rental_time_field(self, rental_time):
        self.click_on_element(OrderPageLocators.DROP_MENU_TIME_ARROW)
        locator_rental_time = self.locator_add_value(OrderPageLocators.DROP_MENU_RENTAL_TIME, rental_time)
        self.click_on_element(locator_rental_time)

    @allure.step('Подтверждение заказа')
    def confirm_order_and_get_text_status_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.ACCEPT_BUTTON)

        return self.get_text_from_element(OrderPageLocators.STATUS_BUTTON)
