from pydantic import BaseModel, field_validator, model_validator

class UserDataModel(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

class GetUsersListModel(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[UserDataModel]
    support: dict

    @model_validator(mode='after')
    def fields_are_not_empty(cls, values):
        for value in values:
            if value == '' or value is None:
                raise ValueError('Value is empty')
        return values

    @field_validator('data')
    def name_minimum_3_symbols(cls, value):
        for user in value:
            if len(user.first_name) < 3:
                raise ValueError('Name is less than 3 symbols')
        return value
