import allure

from api_collection.users.api_users import UsersAPI

@allure.epic('Client Endpoints')
@allure.feature('Users')
class TestUsers:

    @allure.title('Создание нового юзера')
    def test_create_user(self):
        api_users = UsersAPI()
        new_user = api_users.create_user()
        user_by_id = api_users.get_user_by_id(new_user.id)
        with allure.step('Юзер не найдется из-за особенностей тестового API'):
            assert user_by_id is None

    @allure.title('Получение списка всех юзеров')
    def test_get_users_list(self):
        users_api = UsersAPI()
        users_list = users_api.get_users_list()
        with allure.step('Пришел список юзеров'):
            assert users_list.total > 0

    @allure.title('Получение юзера по его id')
    def test_get_user_by_id(self, new_user_fixture):
        users_api = UsersAPI()
        user_by_id = users_api.get_user_by_id(new_user_fixture.id)
        with allure.step('Юзер не найдется из-за особенностей тестового API'):
            assert user_by_id is None

    @allure.title('Редактирование существующего юзера')
    def test_edit_exist_user(self, new_user_fixture):
        users_api = UsersAPI()
        edit_user = users_api.edit_exist_user(user_id=new_user_fixture.id, name='Adel')
        with allure.step('Имя юзера успешно изменено'):
            assert edit_user.name == 'Adel'
