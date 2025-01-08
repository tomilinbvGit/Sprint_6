from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Метод ожидает, пока элемент, соответствующий локатору, станет видимым, и возвращает его
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Метод ожидает, пока элемент станет видимым и выполняет клик по элементу
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        self.driver.find_element(*locator).click()

    # Метод ожидает, пока элемент станет видимым, а после вводит в него текст
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Метод ожидает, пока элемент станет видимым, а после возвращает текст, содержащийся в элементе
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Метод ожидает, пока элемент станет видимым, и прокручивает страницу до этого элемента.
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Форматирует локатор, заменяя плейсхолдеры значением, и возвращает обновленный локатор
    def format_locators(self, locator_1, value):
        method, locator = locator_1
        locator = locator.format(value)

        return (method, locator)

    # Переключается на последнюю открытую вкладку
    def switch_to_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    # Возвращает текущий url, открытый в браузере
    def get_url(self):
        return self.driver.current_url
