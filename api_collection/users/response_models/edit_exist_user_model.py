from pydantic import BaseModel, field_validator, model_validator

class EditExistUserModel(BaseModel):
    name: str
    job: str
    updatedAt: str
