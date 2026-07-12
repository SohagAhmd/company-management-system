from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class Response_model(BaseModel):
    id: int
    name: str
    email: str


class LoginResponse(BaseModel):
    message: str
    user_details: Response_model

    class Config:
        from_attributes = True
