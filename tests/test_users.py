from api_collection.users.api_users import UsersAPI

class TestUsers:

    def test_create_user(self):
        api_users = UsersAPI()
        new_user = api_users.create_user()
        user_by_id = api_users.get_user_by_id(new_user.id)
        assert user_by_id is None

