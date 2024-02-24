from selenium.webdriver.common.by import By


class OrderPageLocators:
    UP_BUTTON = By.CLASS_NAME, 'Button_Button__ra12g'  # Кнопка "Заказать" вверху страницы
    DOWN_BUTTON = By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button'  # Кнопка "Заказать" внизу страницы

    # Локаторы полей ввода
    NAME_INPUT = By.XPATH, './/div[text()="Введите корректное имя"]/parent::div/input'
    SURNAME_INPUT = By.XPATH, './/div[text()="Введите корректную фамилию"]/parent::div/input'
    ADDRESS_INPUT = By.XPATH, './/div[text()="Введите корректный адрес"]/parent::div/input'
    PHONE_INPUT = By.XPATH, './/div[text()="Введите корректный номер"]/parent::div/input'

    METRO_INPUT = By.XPATH, './/div[@class="select-search__value"]/input'  # Поле ввода станции метро
    METRO_STATION_NUMBER = By.XPATH, './/li[@class="select-search__row"]/button[@value="{}"]'  # Номер станции метро

    NEXT_BUTTON = By.XPATH, './/button[text()="Далее"]'

    DATA_INPUT = By.XPATH, './/div[@class="react-datepicker__input-container"]/input'  # Поле ввода даты

    DROP_MENU_TIME_ARROW = By.XPATH, './/span[@class="Dropdown-arrow"]'  # Флаг раскрывающий меню выбора времени аренды
    DROP_MENU_RENTAL_TIME = By.XPATH, './/div[@class="Dropdown-menu"]/div[text()="{}"]'  # Элемент в выпадающем списке

    ORDER_BUTTON = By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'
    ACCEPT_BUTTON = By.XPATH, './/button[text()="Да"]'
    STATUS_BUTTON = By.XPATH, './/div[@class="Order_NextButton__1_rCA"]/button'  # Кнопка "Посмотреть статус"
