import allure

from pages_collection.base_page import BasePage, BasePageLocators
from pages_collection.config import PagesURL
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser, PagesURL.MAIN_PAGE_URL)

    @allure.step('Проверка корректности текущего url адреса')
    def check_current_url(self, url):
        assert self.browser.current_url == url


class MainPageLocators(BasePageLocators):

    ONLINE_TRAINING_BUTTON = (By.XPATH, "//img[@class='banner-image']")
    TRAINING_PAGE_TITLE = (By.XPATH, "//div[@class='enroll__heading']")
    MAIN_PAGE_TITLE = (By.XPATH, "//a[@href='https://demoqa.com']/img")
