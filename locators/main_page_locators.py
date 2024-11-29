from selenium.webdriver.common.by import By


# Локаторы для main_page
class MainPageLocators:
    # Общий локатор для вопросов
    QUESTION_LOCATOR = By.XPATH, ".//div[@id='accordion__heading-{}']"
    # Общий локатор для ответов
    ANSWER_LOCATOR = By.XPATH, ".//div[@id='accordion__panel-{}']"
    # Локатор для последнего вопроса (к нему осуществляется скролл)
    FAQ_LOCATOR_TO_SCROLL = By.XPATH, ".//div[@id='accordion__heading-7']"
    # Локатор для кнопки Заказать, которая находится перед секцией вопросов
    DOWN_ORDER_BUTTON_LOCATOR = By.XPATH, ".//*[contains(@class, 'Home_FinishButton')]/button"
    # Локатор для кнопки Заказать, которая находится в хедере
    HEADER_ORDER_BUTTON_LOCATOR = By.XPATH, ".//div[contains(@class, 'Header')]/button[contains(text(), 'Заказать')]"
    # Локатор для кнопки с cookie (если не принимать, то перекрываются необходимые кнопки)
    COOKIE_CONFIRM_BUTTON_LOCATOR = By.XPATH, ".//button[contains(@class, 'App_CookieButton')]"
    # Локатор для логотипа "Самоката"
    MAIN_PAGE_HEADER_LOCATOR = By.XPATH, ".//div[contains(@class, 'Home_Header')]/text()"
    # Локатор для логотипа "Яндекса"
    YANDEX_LOCATOR = By.XPATH, ".//img[@alt='Yandex']"
    # Локатор для кнопки "Свежее" на Дзене, через проверку ее отображения проверяем корректность перехода
    FRESH_BUTTON_LOCATOR = By.XPATH, ".//*[text()='Свежее']"
