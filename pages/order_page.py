from pages.base_page import BasePage
import allure


class OrderPage(BasePage):
    @allure.step('Нажимаем на кнопку заказа')
    def click_on_order_button(self, locator, button_position):
        if button_position == 'down_button':
            self.scroll_to_position(locator)
            self.click_on_element(locator)
        else:
            self.click_on_element(locator)

    @allure.step('Нажимаем на кнопку формы заполнение заказа')
    def click_on_button_order_form(self, locator):
        self.click_on_element(locator)

    @allure.step('Заполняем поле формы заказа')
    def insert_to_field(self, locator, value):
        self.send_keys(locator, value)

    @allure.step('Заполняем форму выбора станции метро')
    def fill_metro_field(self, locator_field, locator_station):
        self.click_on_element(locator_field)
        self.click_on_element(locator_station)

    @allure.step('Выбираем значение из списка поля "Срок аренды" ')
    def fill_time_order_field(self, locator_field, locator_time):
        self.click_on_element(locator_field)
        self.click_on_element(locator_time)

    @allure.step('Подтверждение заказа')
    def confirm_order(self, order_button_locator, confirm_button_locator, status_button_locator):
        self.click_on_element(order_button_locator)
        self.click_on_element(confirm_button_locator)

        return self.get_text_from_element(status_button_locator)
