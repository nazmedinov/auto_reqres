from pydantic import BaseModel, field_validator, model_validator

class UserCreateModel(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str

    @model_validator(mode='after')
    def fields_are_not_empty(cls, values):
        for value in values:
            if value == '' or value is None:
                raise ValueError('Value is empty')
        return values

    @field_validator('name')
    def name_minimum_3_symbols(cls, value):
        if len(value) < 3:
            raise ValueError('Name is less than 3 symbols')
        return value
