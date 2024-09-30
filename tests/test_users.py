from api_collection.users.api_users import UsersAPI

class TestUsers:

    def test_create_user(self):
        api_users = UsersAPI()
        new_user = api_users.create_user()
        user_by_id = api_users.get_user_by_id(new_user.id)
        assert user_by_id is None

    def test_get_users_list(self):
        users_api = UsersAPI()
        users_list = users_api.get_users_list()
        assert users_list.total > 0

    def test_get_user_by_id(self, new_user_fixture):
        users_api = UsersAPI()
        user_by_id = users_api.get_user_by_id(new_user_fixture.id)
        assert user_by_id is None

    def test_edit_exist_user(self, new_user_fixture):
        users_api = UsersAPI()
        edit_user = users_api.edit_exist_user(user_id=new_user_fixture.id, name='Adel')
        assert edit_user.name == 'Adel'