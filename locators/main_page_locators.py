from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    ANSWER_LOCATOR = By.XPATH, './/div[@id="accordion__panel-{}"]/p'

    MAIN_PAGE_TITLE = By.XPATH, './/div[@class="Home_Header__iJKdX"]'  # Текст с главной страницы сайта

    SCOOTER_LINK = By.XPATH, './/a[@class="Header_LogoScooter__3lsAR"]'
    YANDEX_LINK = By.XPATH, './/a[@class="Header_LogoYandex__3TSOI"]'

    DZEN_LOGO = By.XPATH, './/a[@aria-label="Логотип Бренда"]'  # Логотип Дзена на его главной странице
