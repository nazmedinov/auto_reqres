from pydantic import BaseModel, field_validator, model_validator

class UserDataModel(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

class GetUserByIdModel(BaseModel):
    data: UserDataModel
    support: dict

    @model_validator(mode='after')
    def fields_are_not_empty(cls, values):
        for value in values:
            if value == '' or value is None:
                raise ValueError('Value is empty')
        return values

    @field_validator('data')
    def email_minimum_3_symbols(cls, value):
        if len(value.email) < 3:
            raise ValueError('Email is less than 3 symbols')
        return value
