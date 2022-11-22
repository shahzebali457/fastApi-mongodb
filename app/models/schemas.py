from typing import Optional
from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    age: int = Field(..., ge=18, lt=100)
    # year: int = Field(..., gt=0, lt=9)
    # gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "id": 33,
                "name": "John Doe",
                "email": "jdoe@x.edu.ng",
                "team": "backend",
                "age": 22
            }
        }

class UpdateUserModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    age: Optional[int]
    email: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "id": 33,
                "name": "John Doe",
                "email": "jdoe@x.edu.ng",
                "team": "backend",
                "age": 22
            }
    }

def ResponseModel(data,message):
    return {
        "data": [data],
        "code": 200,
        "message": message

    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}



