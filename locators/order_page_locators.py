from selenium.webdriver.common.by import By


# Локаторы для order_page
class OrderPageLocators:
    # Локатор для поля со станцией метро
    METRO_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    # Локатор станции (для выбора из выпадающего списка)
    NEEDED_STATION_LOCATOR = By.XPATH, ".//*[@class='select-search__options']/li[1]"
    # Локатор для поля с номером телефона
    TEL_NUM_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Локатор для кнопки перехода на вторую часть формы оформления заказа
    CONTINUE_BUTTON_LOCATOR = (By.XPATH, ".//button[contains(text(), 'Далее')]")
    # Локатор для поля с датой
    DATE_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    # Локатор для поля (выпадающего списка) со сроком аренды
    RENTAL_PERIOD_FIELD_LOCATOR = (By.XPATH, ".//div[contains(@class, 'Dropdown-placeholder')]")
    # Локатор для чекбокса черного цвета
    BLACK_CHECKBOX_LOCATOR = By.XPATH, ".//input[@id='black']"
    # Локатор для чекбокса серого цвета
    GREY_CHECKBOX_LOCATOR = By.XPATH, ".//input[@id='grey']"
    # Локатор для поля с комментарием
    COMMENT_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    # Локатор для кнопки "Заказать"
    CONFIRM_ORDER_BUTTON_LOCATOR = (By.XPATH, ".//*[text()='Назад']/following::*[text()='Заказать']")
    # Локатор для кнопки окончательного подтверждения заказа
    APPROVE_ORDER_BUTTON_LOCATOR = (By.XPATH, ".//button[text()='Да']")
    # Локатор для проверки оформления заказа
    SUCCESS_ORDER_LOCATOR = By.XPATH, ".//div[text()='Заказ оформлен']"
    # Общий локатор для полей формы заказа
    COMMON_FIELD_LOCATOR = By.XPATH, ".//input[@placeholder='{}']"
    # Общий локатор для выпадающего меню со временем аренды
    COMMON_RENTAL_PERIOD_LOCATOR = By.XPATH, ".//div[contains(@class, 'Dropdown-menu')]/div[text()='{}']"
    # Локатор для лого "Самокат"
    SCOOTER_LOGO_LOCATOR = By.XPATH, ".//img[@alt='Scooter']"
