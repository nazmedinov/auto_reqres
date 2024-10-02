import allure
from pages_collection.main_page import MainPage, MainPageLocators
from pages_collection.config import PagesURL

@allure.epic('Client Pages')
@allure.feature('Main Page')
class TestMainPage:

    @allure.title('Проверка открытия главной страницы')
    def test_open_main_page(self, browser):
        main_page = MainPage(browser)
        with allure.step('Главная страница успешна открыта'):
            main_page.open()
            main_page.wait_for_visibility(MainPageLocators.MAIN_PAGE_TITLE)

    @allure.title('Проверка перехода к получению сертификата с главной страницы')
    def test_go_to_online_training(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.wait_and_click(MainPageLocators.ONLINE_TRAINING_BUTTON)
        main_page.switch_to_window(window_number=1)
        with allure.step('Успешный переход на страницу получения сертификата'):
            main_page.wait_for_visibility(MainPageLocators.TRAINING_PAGE_TITLE)
            main_page.check_current_url(PagesURL.TRAINING_PAGE_URL)
