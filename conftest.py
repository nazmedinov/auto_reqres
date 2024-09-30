import pytest

from api_collection.users.api_users import UsersAPI

@pytest.fixture
def new_user_fixture():
    users_api = UsersAPI()
    user = users_api.create_user()
    yield user
    users_api.delete_user(user.id)
