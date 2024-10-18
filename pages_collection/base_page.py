import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    GLOBAL_TIMEOUT = 30
    GLOBAL_STEP = 3

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    @allure.step('Открытие страницы по URL адресу')
    def open(self, url=None):
        if url is None:
            url = self.url
        self.browser.get(url)

    @allure.step('Ожидаем элемент кликаем по нему')
    def wait_and_click(self, element, timeout=GLOBAL_TIMEOUT, step=GLOBAL_STEP):
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(element))
        self.browser.find_element(*element).click()

    @allure.step('Ожидаем пока элемент появится на экране')
    def wait_for_visibility(self, element, timeout=GLOBAL_TIMEOUT, step=GLOBAL_STEP):
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(element))

    @allure.step('Переключение на другую вкладку браузера')
    def switch_to_window(self, window_number=1):
        self.browser._switch_to.window(self.browser.window_handles[window_number])

class BasePageLocators:
    pass