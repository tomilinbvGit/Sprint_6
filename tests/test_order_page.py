import allure
import pytest

from data import URLS, TEST_DATA, RENTAL_PERIOD_DICT
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.suite('Тесты страницы заказов')
class TestOrderPage:
    @allure.title('Тест на заказа самоката')
    @allure.description("""
    Для тестов настроена параметризация по ряду полей заполняемых при оформлении заказа. 
    Корректность теста проверяется через отображение сообщения об успешном размещении заказа
    """)
    @pytest.mark.parametrize('button,color,location,rental_period',[
        (MainPageLocators.HEADER_ORDER_BUTTON_LOCATOR,'Черный','Москва, Сокольническая площадь, 4А', 1),
        (MainPageLocators.DOWN_ORDER_BUTTON_LOCATOR, 'Серый', 'Москва, Русаковская улица, 26Бс1', 5)
    ])
    def test_create_order_order_has_been_placed(self, driver, button, color, location, rental_period):
        driver.get(URLS['main_page_url'])
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.cookie_confirm()
        main_page.go_to_order(button)
        order_page.set_order(TEST_DATA['name'],TEST_DATA['surname'],location,TEST_DATA['metro'],TEST_DATA['tel_num'],
                             TEST_DATA['date'],RENTAL_PERIOD_DICT[rental_period],color,TEST_DATA['comment'])
        success_msg = order_page.check_success_order()
        assert success_msg.is_displayed()

    @allure.title('Тест перехода на главную страницу сервиса')
    @allure.description("""
    Тест перехода осуществляется через нажатие на логотип "Самоката". 
    Проверка результата осуществляется через сравнение url со значением из файла data
    """)
    def test_switch_to_main_page_switch_is_completed(self, driver):
        driver.get(URLS['order_page_url'])
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        order_page.go_to_main_page_by_logo()
        assert main_page.get_url() == URLS['main_page_url']
