import requests

from api_collection.users.payloads_users import Payloads
from api_collection.headers import Headers
from api_collection.users.endpoints_users import Endpoints
from api_collection.users.response_models.create_user_model import UserCreateModel
from api_collection.users.response_models.get_users_list_model import GetUsersListModel
from api_collection.users.response_models.get_user_by_id_model import GetUserByIdModel
from api_collection.users.response_models.edit_exist_user_model import EditExistUserModel

class UsersAPI:

    def __init__(self):
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payload = Payloads()

    def create_user(self, name='John', job='Engineer'):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payload.create_user_payload(name, job)
        )
        assert response.status_code == 201, response.json()
        model = UserCreateModel(**response.json())
        return model

    def get_users_list(self):
        response = requests.get(
            url=self.endpoints.get_users_list,
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        model = GetUsersListModel(**response.json())
        return model

    def get_user_by_id(self, user_id):
        response = requests.get(
            url=self.endpoints.get_user_by_id(user_id),
            headers=self.headers.basic
        )

        if response.status_code == 404:
            return None

        assert response.status_code == 200, response.json()
        model = GetUserByIdModel(**response.json())
        return model

    def edit_exist_user(self, user_id, name='John', job='Engineer'):
        response = requests.put(
            url = self.endpoints.edit_exist_user(user_id),
            headers=self.headers.basic,
            json=self.payload.edit_exist_user(name, job),
        )
        assert response.status_code == 200
        model = EditExistUserModel(**response.json())
        return model

    def delete_user(self, user_id):
        response = requests.delete(
            url=self.endpoints.delete_user(user_id),
            headers=self.headers.basic
        )
        assert response.status_code == 204
