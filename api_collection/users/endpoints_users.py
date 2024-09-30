from api_collection.config import HOST

class Endpoints:
    create_user = f'{HOST}/users'
    get_users_list = f'{HOST}/users'
    get_user_by_id = lambda self, user_id: f'{HOST}/users/{user_id}'
    edit_exist_user = lambda self, user_id: f'{HOST}/users/{user_id}'
    delete_user = lambda self, user_id: f'{HOST}/users/{user_id}'
