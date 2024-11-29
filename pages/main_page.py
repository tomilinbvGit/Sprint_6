import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажимаем по вопросу')
    def click_to_question(self, val):
        self.scroll_to_element(MainPageLocators.FAQ_LOCATOR_TO_SCROLL)
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, val)
        self.click_on_element(locator_q_formatted)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, val):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, val)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверяем ответ')
    def check_question_and_answer(self, val):
        self.click_to_question(val)
        return self.get_answer_text(val)

    @allure.step('Принимаем cookie')
    def cookie_confirm(self):
        self.click_on_element(MainPageLocators.COOKIE_CONFIRM_BUTTON_LOCATOR)

    @allure.step('Переходим к странице заказа скутера')
    def go_to_order(self, locator):
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    @allure.step('Переход на Дзен по лого и получение текста кнопки')
    def switch_to_dzen_by_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOCATOR)
        self.switch_to_window()

    def check_fresh_button(self):
        switch_check = WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.FRESH_BUTTON_LOCATOR))
        return switch_check
