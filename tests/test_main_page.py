import allure
import pytest
from data import URLS, VALID_ANSWERS
from pages.main_page import MainPage


@allure.suite('Тесты для главной страницы сервиса')
class TestMainPage:
    @allure.title('Тест на проверку ответов')
    @allure.description("""
    Тест проверяет ответ к каждому из вопросов раздела "Вопросы о важном". 
    Результат проверяется через сравнение с ожидаемым результатом (ответы вынесены в data).
    """)
    @pytest.mark.parametrize('num',[0,1,2,3,4,5,6,7])
    def test_question_and_answer(self, driver, num):
        driver.get(URLS['main_page_url'])
        main_page = MainPage(driver)
        main_page.cookie_confirm()
        assert main_page.check_question_and_answer(num) == VALID_ANSWERS[num]

    @allure.title('Тест для проверки перехода на Дзен')
    @allure.description("""
    Тест проверяет переход на страницу Дзена по клику на лого Яндекса. 
    Результат проверяет, что кнопка "Свежие" отображается на странице.
    """)
    def test_switch_to_dzen(self, driver):
        driver.get(URLS['main_page_url'])
        main_page = MainPage(driver)
        main_page.switch_to_dzen_by_logo()
        main_page.switch_to_window()
        fresh_button = main_page.check_fresh_button()
        assert fresh_button.is_displayed()
