import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import PLACEHOLDER_CONTENT
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Указываем имя клиента')
    def set_name(self, name):
        name_locator_formated = self.format_locators(OrderPageLocators.COMMON_FIELD_LOCATOR,
                                                     PLACEHOLDER_CONTENT['name'])
        self.add_text_to_element(name_locator_formated, name)

    @allure.step('Указываем фамилию клиента')
    def set_surname(self, surname):
        surname_locator_formated = self.format_locators(OrderPageLocators.COMMON_FIELD_LOCATOR,
                                                        PLACEHOLDER_CONTENT['surname'])
        self.add_text_to_element(surname_locator_formated, surname)

    @allure.step('Указываем адрес')
    def set_location(self, location):
        location_locator_formated = self.format_locators(OrderPageLocators.COMMON_FIELD_LOCATOR,
                                                         PLACEHOLDER_CONTENT['location'])
        self.add_text_to_element(location_locator_formated, location)

    @allure.step('Указываем станцию метро')
    def set_metro(self, metro_station):
        metro_locator_formated = self.format_locators(OrderPageLocators.COMMON_FIELD_LOCATOR,
                                                      PLACEHOLDER_CONTENT['metro_station'])
        self.add_text_to_element(metro_locator_formated, metro_station)
        self.click_on_element(OrderPageLocators.NEEDED_STATION_LOCATOR)

    @allure.step('Указываем телефонный номер')
    def set_telephone_number(self, telephone_number):
        tel_num_locator_formated = self.format_locators(OrderPageLocators.COMMON_FIELD_LOCATOR,
                                                         PLACEHOLDER_CONTENT['tel_num'])
        self.add_text_to_element(tel_num_locator_formated, telephone_number)

    @allure.step('Указываем дату заказа')
    def set_date(self, date):
        date_locator_formated = self.format_locators(OrderPageLocators.COMMON_FIELD_LOCATOR,
                                                     PLACEHOLDER_CONTENT['date'])
        self.add_text_to_element(date_locator_formated, date)
        self.driver.execute_script("document.querySelector('.react-datepicker').style.display='none';")

    @allure.step('Указываем срок аренды')
    def set_rental_period(self, rental_period):
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_FIELD_LOCATOR)
        rental_period_formated = self.format_locators(OrderPageLocators.COMMON_RENTAL_PERIOD_LOCATOR, rental_period)
        self.click_on_element(rental_period_formated)

    @allure.step('Выбираем цвет для самоката')
    def set_scooter_color(self, color):
        if color == 'Серый':
            self.click_on_element(OrderPageLocators.GREY_CHECKBOX_LOCATOR)
        elif color == 'Черный':
            self.click_on_element(OrderPageLocators.BLACK_CHECKBOX_LOCATOR)

    @allure.step('Указываем комментарий к заказу')
    def set_comment(self, comment):
        comment_locator_formated = self.format_locators(OrderPageLocators.COMMON_FIELD_LOCATOR,
                                                     PLACEHOLDER_CONTENT['comment'])
        self.add_text_to_element(comment_locator_formated, comment)

    @allure.step('Начало сценария с оформлением заказа')
    def set_order(self, name, surname, location, metro,
                  tel_num, date, rental_period, color, comment):
        self.set_name(name)
        self.set_surname(surname)
        self.set_location(location)
        self.set_metro(metro)
        self.set_telephone_number(tel_num)
        self.click_on_element(OrderPageLocators.CONTINUE_BUTTON_LOCATOR)
        self.set_date(date)
        self.set_rental_period(rental_period)
        self.set_scooter_color(color)
        self.set_comment(comment)
        self.click_on_element(OrderPageLocators.CONFIRM_ORDER_BUTTON_LOCATOR)
        self.click_on_element(OrderPageLocators.APPROVE_ORDER_BUTTON_LOCATOR)

    @allure.step('Проверяем появление сообщения об успешной регистрации')
    def check_success_order(self):
        success_check = WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.SUCCESS_ORDER_LOCATOR))
        return success_check

    @allure.step('Переход на главную страницу сервиса через лого')
    def go_to_main_page_by_logo(self):
        self.click_on_element(OrderPageLocators.SCOOTER_LOGO_LOCATOR)
