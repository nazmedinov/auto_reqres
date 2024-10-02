import allure
import pytest

from api_collection.users.api_users import UsersAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@allure.step('Подготовка тестового юзера')
@pytest.fixture
def new_user_fixture():
    users_api = UsersAPI()
    user = users_api.create_user()
    yield user
    users_api.delete_user(user.id)

@allure.step('Открытие браузера')
@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options)
    browser.implicitly_wait(3)

    return browser
